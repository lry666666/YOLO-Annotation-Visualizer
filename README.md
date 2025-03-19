# YOLO-Annotation-Visualizer
# YOLOv5 图像标注绘图工具

该项目是一个 Python 脚本，用于读取 YOLOv5 格式的标签文件，并在图像上绘制边界框。 它接受图像目录、标签目录、包含类别信息的 YAML 文件和输出目录作为输入。

## 功能

*   从 YAML 文件加载类别名称。
*   读取 YOLOv5 格式的标签文件（.txt 文件）。
*   在图像上绘制边界框，并使用类别名称标记它们。
*   将带有边界框的图像保存到指定的输出目录。
*   支持批量处理图像目录。
*   错误处理，包括处理丢失的标签文件、格式错误的标签和无效的类别 ID。

## 用法


1.  **安装依赖项：**

    ```bash
    pip install opencv-python pyyaml
    ```

2.  **准备你的数据：**

    *   将你的图像放在一个目录中。
    *   确保你有相应的 YOLOv5 格式的标签文件（`.txt` 文件），并放在另一个目录中。标签文件名必须与图像文件名匹配（不包括扩展名）。标签文件应具有以下格式：

        ```
        class_id center_x center_y width height
        ```

        其中 `class_id` 是一个整数，其余的值是 0 和 1 之间的浮点数。

    *   准备一个 YAML 文件，其中包含类别名称。例如：

        ```yaml
        names:
          - class1
          - class2
          - class3
          # ...
        ```

3.  **配置脚本：**

    打开 `your_script_name.py` 并修改以下变量，使它们指向你的文件和目录：

    ```python
    image_dir = 'path/to/your/images'   # 替换为你的图像目录
    labels_dir = 'path/to/your/labels'    # 替换为你的标签目录
    yaml_path = 'path/to/your/data.yaml'   # 替换为你的 YAML 文件路径
    output_dir = 'path/to/output'       # 替换为你想保存结果的目录
    ```

4.  **运行脚本：**

    ```bash
    python your_script_name.py
    ```

5.  **查看输出：**

    带有边界框的图像将保存在 `output_dir` 中。

## 示例

假设你有以下目录结构：
Use code with caution.
Markdown
├── images/
│ ├── image1.jpg
│ ├── image2.jpg
│ └── ...
├── labels/
│ ├── image1.txt
│ ├── image2.txt
│ └── ...
├── data.yaml

`data.yaml` 文件可能包含：

```yaml
names:
  - cat
  - dog
  - bird
Use code with caution.
并且 image1.txt 文件可能包含：

0 0.5 0.5 0.2 0.3
1 0.8 0.6 0.1 0.2
Use code with caution.
运行该脚本会在 output 目录中生成 image1.jpg 和 image2.jpg 的带有边界框的版本。

依赖
opencv-python

PyYAML
