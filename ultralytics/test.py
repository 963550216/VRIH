import time
from ultralytics import YOLO

# 加载模型权重
model = YOLO('D:/ultralytics-yolov8/ultralytics/runs/detect/train9/weights/best.pt')  # 模型路径

# 进行推理（可以直接在推理时指定保存，也可以后续手动保存）
results = model('D:/ultralytics-yolov8/this_datasets/images/0000021.jpg')  # 输入图片路径

t1 = time.time()

# 处理结果
if isinstance(results, list):
    result = results[0]  # 取第一个结果
else:
    result = results

# 保存图像（核心步骤）
# 方法1：直接保存到默认路径（runs/detect/predict/）
result.save()  # 默认文件名会自动生成，如 '0000002.jpg'

# 方法2：指定保存路径和文件名（推荐）
save_path = 'D:/ultralytics-yolov8/detection_result21.jpg'  # 自定义路径
result.save(filename=save_path)  # 保存到指定路径

# 显示图像（可选）
result.show()

# 获取检测框坐标和类别名称
boxes = result.boxes  # 检测框
names = result.names  # 类别名称

for i in range(len(boxes)):
    box = boxes[i]
    class_id = box.cls  # 类别ID
    coordinates = box.xyxy[0]  # [x1, y1, x2, y2]（像素坐标）
    confidence = box.conf  # 置信度

    if len(coordinates) == 4:
        x1, y1, x2, y2 = coordinates
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2  # 中心点
        w, h = x2 - x1, y2 - y1  # 宽高

        # 打印信息
        print(f"Class: {names[int(class_id)]}")
        print(f"Coordinates: {coordinates}")
        print(f"Center: ({cx}, {cy})")
        print(f"Width: {w}, Height: {h}")
        print(f"Confidence: {confidence}")
        print('-' * 50)
    else:
        print(f"Invalid coordinates format: {coordinates}")

# 打印时间信息
print(f"开始时间: {t1}")
print(f"推理+保存耗时: {time.time() - t1:.4f} 秒")