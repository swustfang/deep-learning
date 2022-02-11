import os
import random

files_path = '../../data_set/VOCdevkit/VOC2012/Annotations'
if not os.path.exists(files_path):
    print("文件夹不存在")
    exit(1)

val_rate = 0.5
files_name = sorted([file.split(".")[0] for file in os.listdir(files_path)])
files_num = len(files_name)
val_index = random.sample(range(0, files_num), k=int(files_num * val_rate))

train_files = []
val_files = []

for index, file_name in enumerate(files_name):
    if index in val_index:
        val_files.append(file_name)
    else:
        train_files.append(file_name)

try:
    train_f = open("train.txt", "x")
    eval_f = open("val.txt", "x")
    train_f.write("\n".join(train_files))
    eval_f.write("\n".join(val_files))
except FileExistsError as e:
    print(e)
    exit(1)
