import os
from pathlib import Path

import cv2


def apply_clahe_to_folder(input_folder, output_folder, clip_limit=2.0, grid_size=(8, 8)):
    """对文件夹中的所有图像应用CLAHE方法.

    参数:
    - input_folder: 输入图像文件夹路径
    - output_folder: 输出图像文件夹路径
    - clip_limit: 对比度限制阈值
    - grid_size: 网格大小，用于局部直方图均衡化
    """
    # 创建输出文件夹（如果不存在）
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # 创建CLAHE对象
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)

    # 支持的图像格式
    supported_formats = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif"}

    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        # 检查是否为图像文件
        if os.path.isfile(file_path) and Path(filename).suffix.lower() in supported_formats:
            try:
                # 读取图像
                img = cv2.imread(file_path)

                if img is None:
                    print(f"无法读取图像: {filename}")
                    continue

                # 将图像转换为LAB颜色空间
                lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

                # 分离LAB通道
                l, a, b = cv2.split(lab)

                # 对L通道（亮度通道）应用CLAHE
                l_clahe = clahe.apply(l)

                # 合并通道
                lab_clahe = cv2.merge([l_clahe, a, b])

                # 转换回BGR颜色空间
                result = cv2.cvtColor(lab_clahe, cv2.COLOR_LAB2BGR)

                # 构建输出文件路径
                output_path = os.path.join(output_folder, filename)

                # 保存处理后的图像
                cv2.imwrite(output_path, result)
                print(f"已处理: {filename}")

            except Exception as e:
                print(f"处理 {filename} 时出错: {e!s}")


# 使用方法
if __name__ == "__main__":
    input_dir = "SAR-aircraft-SADD/images"  # 输入文件夹路径
    output_dir = "SAR-aircraft-SADD/images_clahe"  # 输出文件夹路径

    # 应用CLAHE
    apply_clahe_to_folder(input_dir, output_dir, clip_limit=2.0, grid_size=(8, 8))
