# CCS-Net: Enhancing SAR Aircraft Detection with a Lightweight and Efficient Framework

[![Framework](https://img.shields.io/badge/Framework-PyTorch-red)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Preprint-blue)](https://www.elsevier.com/)
[![Journal](https://img.shields.io/badge/Submitted%20to-Virtual%20Reality%20%26%20Intelligent%20Hardware-orange)](http://www.vrih.net/)

This repository implements **CCS-Net**, a lightweight and efficient framework for aircraft detection in Synthetic Aperture Radar (SAR) imagery, as described in the paper: **"Enhancing SAR Aircraft Detection with CCS-Net: A Lightweight and Efficient Framework for Manned-Unmanned Teaming Reconnaissance"**.

**Authors:** Lei Bao, Dongfang Li, Chaolong Li, Xianzhong Gao
_(National University of Defense Technology)_

## 📖 Abstract

In Manned-Unmanned Teaming (MUM-T) systems, accurate SAR aircraft detection is critical. Existing methods often struggle with background clutter, scale variations, and computational inefficiency. We propose **CCS-Net**, a **Cooperative Context-aware Sensing Network** that achieves state-of-the-art accuracy with an ultra-lightweight design.

Key innovations include:

- **CLAHE Preprocessing:** Enhances contrast and suppresses speckle noise.
- **C2F_LK & MSCA Modules:** Novel feature extraction blocks utilizing large-kernel depthwise separable convolutions and multi-scale context aggregation.
- **SCA-Head:** A Spatial Coordinate Attention Head to improve small target localization.
- **Label Smoothing:** Optimized loss function to handle class imbalance.

Achieves **96.6% mAP@0.5** on the SAR-Aircraft-1.0 dataset with only **0.97M parameters**.

## 🏗️ Model Architecture

The CCS-Net architecture consists of three main stages:

1.  **Feature Extraction:** Incorporates **C2F_LK** (with LarkBlock) and **MSCA** modules to capture multi-scale features efficiently.
2.  **Feature Fusion:** Uses a dual-path **FPN-PAN** structure to integrate semantic and spatial information.
3.  **Detection Head:** The **SCA-Head** applies spatial and coordinate attention mechanisms for precise bounding box regression and classification.

> _Note: See Figure 2 in the paper for the complete graphical abstract._

## 📊 Performance

CCS-Net demonstrates superior performance vs. lightweight models (YOLOv5n/v8n) and large models (Faster R-CNN).

### Results on SAR-Aircraft-1.0 Dataset

| Model              | Precision (%) | Recall (%) | mAP@0.5 (%) | mAP@0.75 (%) | Params (M) | GFLOPs (G) |
| :----------------- | :-----------: | :--------: | :---------: | :----------: | :--------: | :--------: |
| Faster R-CNN       |     90.4      |    87.1    |    89.7     |     55.8     |    41.2    |   135.7    |
| YOLOv5             |     84.7      |    93.7    |    94.3     |     60.8     |    7.03    |    15.8    |
| YOLOv8             |     86.6      |    91.5    |    94.6     |     64.0     |    3.20    |    8.7     |
| YOLOv10            |     85.2      |    87.7    |    93.8     |     66.3     |    2.71    |    8.4     |
| YOLOv11            |     85.5      |    90.4    |    92.8     |     61.2     |    2.58    |    6.3     |
| **CCS-Net (Ours)** |   **93.5**    |  **95.7**  |  **96.6**   |   **73.8**   |  **0.97**  |  **7.7**   |

### Results on SADD Dataset

| Model              | Precision (%) | Recall (%) | mAP@0.5 (%) | mAP@0.75 (%) |
| :----------------- | :-----------: | :--------: | :---------: | :----------: |
| Chen et al. (2024) |     94.0      |    81.2    |    92.0     |     57.1     |
| Guo et al. (2024)  |     93.1      |    91.2    |    85.6     |      -       |
| **CCS-Net (Ours)** |   **95.1**    |  **93.5**  |  **97.7**   |   **58.3**   |

## 🔨 Installation

### Requirements

- Python >= 3.8
- PyTorch >= 1.10
- NVIDIA GPU (Tested on RTX 4060)

```bash
# Clone the repository
git clone https://github.com/your-username/CCS-Net.git
cd CCS-Net
```

## 📂 Datasets

This project evaluates the proposed CCS-Net on two public Synthetic Aperture Radar (SAR) datasets: **SAR-Aircraft-1.0** and **SADD**.

### 1. SAR-Aircraft-1.0

A challenging dataset with fine-grained recognition labels, collected from the Gaofen-3 satellite.

- **Source:** Gaofen-3 (Spotlight mode)
- **Resolution:** 1 meter
- **Images:** 4,368 images (Sizes: 800×800 to 1500×1500)
- **Instances:** 17,943 aircraft
- **Categories (7):** A320/321, A220, ARJ21, A330, Boeing 737, Boeing 787, Other.
- **🔗 Download:** [Website](https://radars.ac.cn/cn/article/doi/10.12000/JR23043)

### 2. SADD (SAR Aircraft Detection Dataset)

A dataset collected from multiple satellite sources, focusing on single-aircraft target detection.

- **Sources:** Gaofen-3 (GF-3) and TerraSAR-X
- **Images:** 2,968 images
- **Size:** Uniformly preprocessed to 224 × 224 pixels
- **Instances:** 7,835 aircraft
- **🔗 Reference:** [Website](https://github.com/hust-rslab/SAR-aircraft-data)

## 📜 Statement

- This project is released under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.
- 本项目采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 协议发布。

- If you have any questions or need additional data, code, and weight files, please contact us at [baolei20@nudt.edu.cn](mailto:baolei20@nudt.edu.cn) or [lidongfang2022@126.com](mailto:lidongfang2022@126.com).
- 如有任何问题或者需要其他数据、代码和权重文件，请通过 [lidongfang2022@126.com](mailto:lidongfang2022@126.com) 联系我们。
