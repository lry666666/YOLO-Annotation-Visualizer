import cv2
import yaml
import os
import random

def draw_boxes(image_path, labels_dir, yaml_path, output_dir):
    """
    在图像上绘制 YOLOv5 格式的框。

    Args:
        image_path (str): 图像文件的路径。
        labels_dir (str): 包含 YOLOv5 格式标签（.txt）文件的目录。  标签文件名要和图片名对应（除了后缀）
        yaml_path (str): 包含类别名称和数量的 YAML 文件的路径。
        output_dir (str): 保存带有框的图像的目录。
    """

    try:
        # 1. 加载 YAML 文件以获取类别信息
        with open(yaml_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)  # 使用safe_load 防止恶意代码执行
        classes = data['names']
        num_classes = len(classes)
        print(f"找到 {num_classes} 个类别: {classes}")

        # 2. 加载图像
        img = cv2.imread(image_path)
        if img is None:
            print(f"错误: 无法加载图像: {image_path}")
            return

        height, width, _ = img.shape

        # 3. 构建标签文件路径
        image_name = os.path.splitext(os.path.basename(image_path))[0]  # 获取不带后缀的文件名
        label_file_path = os.path.join(labels_dir, image_name + '.txt')

        # 4. 读取标签文件
        try:
            with open(label_file_path, 'r') as f:
                labels = f.readlines()
        except FileNotFoundError:
            print(f"警告: 找不到标签文件: {label_file_path}")
            return

        # 5. 在图像上绘制框
        for label in labels:
            try:
                class_id, center_x, center_y, box_width, box_height = map(float, label.strip().split())

                # 验证 class_id
                if not (0 <= int(class_id) < num_classes):
                    print(f"警告: class_id ({class_id}) 超出范围。跳过此框。")
                    continue  # 跳过不正确的 class_id

                # 将归一化坐标转换为像素坐标
                x1 = int((center_x - box_width / 2) * width)
                y1 = int((center_y - box_height / 2) * height)
                x2 = int((center_x + box_width / 2) * width)
                y2 = int((center_y + box_height / 2) * height)

                # 确保坐标在图像边界内
                x1 = max(0, x1)
                y1 = max(0, y1)
                x2 = min(width, x2)
                y2 = min(height, y2)
                
                # 生成随机颜色
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                # 绘制矩形
                cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

                # 添加类别标签
                class_name = classes[int(class_id)]  # 使用 int() 转换 class_id
                label_text = f"{class_name}"  #  可以添加置信度（如果标签文件中包含）
                cv2.putText(img, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            except ValueError:
                print(f"警告: 标签文件格式错误: {label.strip()}。跳过此行。")
                continue #跳过格式错误的行

        # 6. 保存结果图像
        os.makedirs(output_dir, exist_ok=True) # 确保输出目录存在
        output_path = os.path.join(output_dir, os.path.basename(image_path))
        cv2.imwrite(output_path, img)
        print(f"已保存图像到: {output_path}")

    except Exception as e:
        print(f"发生错误: {e}")



if __name__ == '__main__':
    # 示例用法
    image_dir = 'E:/shuju/rubbish-bin/images/train'   # 替换为你的图像目录
    labels_dir = 'E:/shuju/rubbish-bin/labels/train'    # 替换为你的标签目录
    yaml_path = 'E:/shuju/rubbish-bin/data.yaml'   # 替换为你的 YAML 文件路径
    output_dir = 'E:/shuju/rubbish-bin/output'       # 替换为你想保存结果的目录

    # 遍历图像目录中的所有图像文件
    for filename in os.listdir(image_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # 支持的图像格式
            image_path = os.path.join(image_dir, filename)
            draw_boxes(image_path, labels_dir, yaml_path, output_dir)
