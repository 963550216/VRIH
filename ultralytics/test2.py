import cv2
import numpy as np


def preprocess_image(image_path, target_size=(640, 640)):
    """将图像预处理为指定大小（640x640）."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("无法读取图像，请检查路径是否正确")

    # 调整图像大小为640x640（使用双线性插值，保持比例缩放后填充黑边，避免变形）
    h, w = img.shape[:2]
    target_h, target_w = target_size

    # 计算缩放比例（取宽和高中的最小比例，确保图像完全放入目标尺寸）
    scale = min(target_w / w, target_h / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # 缩放图像
    resized_img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

    # 创建640x640的空白画布（黑色）
    padded_img = np.zeros((target_h, target_w, 3), dtype=np.uint8)

    # 计算填充位置（居中放置缩放后的图像）
    top = (target_h - new_h) // 2
    left = (target_w - new_w) // 2

    # 将缩放后的图像放入画布
    padded_img[top : top + new_h, left : left + new_w] = resized_img

    return padded_img, (scale, top, left)  # 返回预处理后的图像和缩放/填充信息


def draw_boxes_after_preprocess(image_path, boxes, output_path="output_preprocessed21.jpg"):
    # 预处理图像为640x640
    preprocessed_img, (_scale, _top, _left) = preprocess_image(image_path, (640, 640))
    target_h, target_w = 640, 640  # 目标尺寸

    # 遍历每个边界框
    for box in boxes:
        # 解析框信息：类别ID, 中心点x(归一化), 中心点y(归一化), 宽(归一化), 高(归一化)
        cls_id, cx_norm, cy_norm, w_norm, h_norm = box

        # 基于预处理后的640x640图像计算坐标（归一化坐标直接乘以目标尺寸）
        cx = int(cx_norm * target_w)  # 中心点x（640x640图像中）
        cy = int(cy_norm * target_h)  # 中心点y（640x640图像中）
        box_w = int(w_norm * target_w)  # 框宽度（640x640图像中）
        box_h = int(h_norm * target_h)  # 框高度（640x640图像中）

        # 计算左上角和右下角坐标
        x1 = int(cx - box_w / 2)
        y1 = int(cy - box_h / 2)
        x2 = int(cx + box_w / 2)
        y2 = int(cy + box_h / 2)

        # 绘制矩形框（颜色：红色，线宽：2）
        cv2.rectangle(preprocessed_img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # 绘制类别ID和置信度标签
        label = f"Class: {int(cls_id)}"
        cv2.putText(
            preprocessed_img, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
        )

    # 保存结果
    cv2.imwrite(output_path, preprocessed_img)
    print(f"预处理（640x640）并绘制框后的图像已保存到：{output_path}")

    # 显示图像
    cv2.imshow("Preprocessed Image with Boxes", preprocessed_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 边界框数据（类别ID, 中心点x(归一化), 中心点y(归一化), 宽(归一化), 高(归一化)）
boxes = [
    [1, 0.287, 0.4646666666666667, 0.051333333333333335, 0.04533333333333333],
    [3, 0.36733333333333335, 0.451, 0.044, 0.046],
    [4, 0.20833333333333331, 0.9143333333333333, 0.04733333333333333, 0.048666666666666664],
    [4, 0.059, 0.9333333333333333, 0.046, 0.048],
    [4, 0.13833333333333334, 0.9323333333333333, 0.054, 0.051333333333333335],
]

# 调用函数（替换为你的图像路径）
draw_boxes_after_preprocess(
    image_path="D:/ultralytics-yolov8/this_datasets/images/0000021.jpg",  # 输入图像路径
    boxes=boxes,
)
# # 调用函数绘制框（替换为你的图像路径）
# draw_boxes(
#     image_path="D:/ultralytics-yolov8/this_datasets/images/0000001.jpg",  # 输入图像路径
#     boxes=boxes,
#     output_path="output_with_boxes.jpg"  # 输出图像路径
# )
