import os
from zipfile import ZipFile

def zip_all(search_dir, extension_list, output_path):
    with ZipFile(output_path, 'w') as output_zip:
        for root, _, files in os.walk(search_dir):
            rel_path = os.path.relpath(root, search_dir)
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in extension_list:
                    output_zip.write(os.path.join(root, file),
                                     arcname=os.path.join(rel_path, file))


# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     zip_all('14/my_stuff', ['.jpg','.txt'], 'my_stuff.zip')
