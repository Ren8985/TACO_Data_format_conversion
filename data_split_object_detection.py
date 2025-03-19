import os
import json
import shutil

# 读取 JSON 文件
with open('annotations_0_val.json', 'r') as file:
    data = json.load(file)

# 图像尺寸字典，方便后续查找每个图像的尺寸
image_size_dict = {image["id"]: (image["width"], image["height"]) for image in data["images"]}

# 新建文件夹存储图像和标签
image_dir = r"C:/Users/89857/OneDrive/Desktop/毕业设计/TACO-master/yolo_data_object_detection/val/images"
output_dir = r"C:/Users/89857/OneDrive/Desktop/毕业设计/TACO-master/yolo_data_object_detection/val/labels"

# # 确保目录存在
# os.makedirs(image_dir, exist_ok=True)
# os.makedirs(output_dir, exist_ok=True)

# 遍历图片信息列表，复制图像到新的路径
for image in data["images"]:
    get_image_id = image["id"]
    new_file_name = f"{get_image_id}.jpg"
    get_image_file_local = image["file_name"]

    # 将图像复制到新的目录
    shutil.copy(get_image_file_local, os.path.join(image_dir, new_file_name))

# 遍历标注信息，生成标签文件并进行归一化处理
for annotation in data["annotations"]:
    image_id = annotation["image_id"]
    object_class = annotation["category_id"]
    object_local = annotation["bbox"]

    # 获取图像尺寸（宽度和高度）
    image_width, image_height = image_size_dict[image_id]

    # 获取边界框坐标
    x_min, y_min, width, height = object_local

    # 计算归一化后的坐标
    x_center = (x_min + width / 2) / image_width
    y_center = (y_min + height / 2) / image_height
    width_normalized = width / image_width
    height_normalized = height / image_height

    # 格式化后的目标框体（边界框）数据
    bbox_line = f"{object_class} {x_center} {y_center} {width_normalized} {height_normalized}"

    # 构造图像ID对应的txt文件路径
    txt_file_path = os.path.join(output_dir, f"{image_id}.txt")

    # 判断txt文件是否存在
    if not os.path.exists(txt_file_path):
        # 如果文件不存在，创建文件并写入内容
        with open(txt_file_path, "w") as file:
            file.write(bbox_line + "\n")
    else:
        # 如果文件存在，直接在文件中换行写入内容
        with open(txt_file_path, "a") as file:
            file.write(bbox_line + "\n")

print("数据处理完成！")
