import zipfile
import os
import json
import shutil
from opencc import OpenCC

filename = input("輸入材質包壓縮檔路徑(xxx.zip):")
workdir = './zip'
os.mkdir(workdir)
with zipfile.ZipFile(filename, 'r') as ZIP:
    ZIP.extractall(workdir)

converter = OpenCC('s2twp.json')
data = ""

for path in os.listdir(path='./zip/assets'):
    with open(f'./{workdir}/assets/{path}/lang/zh_cn.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for line in data:
            data[line] = converter.convert(data[line])

    with open(f'./{workdir}/assets/{path}/lang/zh_tw.json', 'w', encoding='utf-8') as newfile:
        json.dump(data, newfile, ensure_ascii=False, indent=4)

#參考chatgpt
def zip_dir(directory, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, directory))


newfile = filename[:-4]+"_tw.zip"
zip_dir(workdir, newfile)
shutil.rmtree(workdir)
print("done.")
