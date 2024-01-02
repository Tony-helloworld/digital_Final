import os
from PyQt5.QtWidgets import QFileDialog

def read_image_files_from_folder(folder_path):
    image_files = []

    # 使用文件对话框选择文件夹
    dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.Directory)
    if dialog.exec_():
        folder_path = dialog.selectedFiles()[0]

    # 遍历文件夹中的文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # 检查文件是否是图片文件（.bmp、.png、.jpg）
        if os.path.isfile(file_path) and filename.lower().endswith(('.bmp', '.png', '.jpg')):
            image_files.append(file_path)

    return image_files

# 示例用法
folder_path = '/path/to/your/folder'  # 请替换为实际文件夹路径
image_files_list = read_image_files_from_folder(folder_path)
print(image_files_list)
