# @Time   ：2023/9/5 13:36
# @Author : Chao
# @File   : demo3.py


# 批量修改文件夹名称


import os

def replace_folder_name(folder_path, old_name, new_name):
    try:
        # 获取文件夹路径下所有子文件夹和文件
        items = os.listdir(folder_path)

        for item in items:
            item_path = os.path.join(folder_path, item)

            # 判断是否为文件夹
            if os.path.isdir(item_path):
                # 替换文件夹名称
                new_folder_name = item.replace(old_name, new_name)
                new_folder_path = os.path.join(folder_path, new_folder_name)

                # 递归调用，替换子文件夹名称
                replace_folder_name(item_path, old_name, new_name)

                # 重命名文件夹
                os.rename(item_path, new_folder_path)

    except Exception as e:
        print(f"Error occurred: {e}")


# 指定文件夹路径、旧名称和新名称
folder_path = "C:/Users/iyunwen/Desktop/webaikn"
old_name = "old_name"
new_name = "new_name"

# 调用函数替换文件夹名称
replace_folder_name(folder_path, old_name, new_name)