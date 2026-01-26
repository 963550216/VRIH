import os
from collections import defaultdict

import matplotlib.pyplot as plt

# 中文显示
plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS", "STHeiti"]

# 重新设置负号显示（确保负号正常）
plt.rcParams["axes.unicode_minus"] = False  # 或者 False，根据实际情况调整


def count_classes_from_train_txt(train_txt_path, label_dir, class_names=None):
    class_count = defaultdict(int)

    with open(train_txt_path) as f:
        img_paths = [line.strip() for line in f if line.strip()]

    for img_path in img_paths:
        img_name = os.path.splitext(os.path.basename(img_path))[0]
        label_path = os.path.join(label_dir, img_name + ".txt")

        if not os.path.exists(label_path):
            print(f"警告：标注文件不存在 {label_path}，跳过")
            continue

        with open(label_path) as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue
            class_id = int(line.split()[0])
            class_count[class_id] += 1

    if class_names:
        named_count = {}
        for cid, count in class_count.items():
            if 0 <= cid < len(class_names):
                named_count[class_names[cid]] = count
            else:
                named_count[f"未知类别{cid}"] = count
        return named_count
    return class_count


# 配置路径
train_txt_path = "dataSet/train.txt"
label_dir = "labels"  # 标注文件所在目录
class_names = ["Boeing787", "Boeing737", "A330", "other", "A220", "ARJ21", "A320/321"]  # 替换为你的实际类别名称列表

# 统计类别数量
counts = count_classes_from_train_txt(train_txt_path, label_dir, class_names)

# 打印结果
print("训练集类别数量统计：")
for class_name, count in counts.items():
    print(f"{class_name}: {count} 个标注")

# 可视化（可选）
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(counts.keys(), counts.values(), color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.xlabel("类别名称")
plt.ylabel("标注数量")
plt.title("训练集类别分布")
plt.tight_layout()
plt.show()
