# 3D Point Cloud Segmentation for Urban Analysis

[![Compile LaTeX](https://github.com/yourusername/geoai4cities/workflows/Compile%20LaTeX/badge.svg)](https://github.com/yourusername/geoai4cities/actions)
[![Code Quality](https://github.com/yourusername/geoai4cities/workflows/Code%20Quality/badge.svg)](https://github.com/yourusername/geoai4cities/actions)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

This repository contains a comprehensive internship report and implementation code for 3D point cloud segmentation applied to urban environments. The project explores state-of-the-art deep learning techniques for semantic segmentation of urban point clouds, with applications in autonomous driving, urban planning, and smart city development.

## Key Achievements

- **Real-time Performance**: Achieved 28.7 FPS on NVIDIA Jetson Xavier NX
- **Model Comparison**: Evaluated PointNet, PVCNN, SONATA, and RandLA-Net
- **Edge Optimization**: 40-60% memory reduction with <2% accuracy loss
- **Hardware Integration**: ZED 2i camera integration for real-time data acquisition

## Repository Structure

```
├── .github/                                            # GitHub configuration
│   ├── workflows/                                      # CI/CD workflows
│   ├── ISSUE_TEMPLATE/                                 # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md                       # PR template
├── Internship_Report_3D_PointCloud_Segmentation.tex    # Main LaTeX report
├── Internship_Report_3D_PointCloud_Segmentation.pdf    # Compiled PDF report
├── references.bib                                       # Bibliography file
├── logo.png                                            # Institution logo
├── figures/                                            # Screenshots and visualizations
│   ├── development_setup.png
│   ├── pointcloud_visualisation_sonata_demo.png
│   ├── early_experiments.png
│   ├── model_analysis.png
│   ├── real_time_inference.png
│   ├── performance_optimisation.png
│   └── zed_deployment.png
├── open3d/                                             # Open3D implementation files
├── pvcnn/                                              # PVCNN model implementation
├── zed2i/                                              # ZED camera integration
├── frames/                                             # Sample point cloud frames
└── screenshots/                                        # Development screenshots
```

## Technical Specifications

### Hardware Platforms

- **Training**: NVIDIA RTX 3070 (8GB VRAM)
- **Edge Deployment**: NVIDIA Jetson Xavier NX (8GB unified memory)
- **Data Acquisition**: ZED 2i stereo camera

### Software Stack

- **Framework**: PyTorch 1.13.0 with CUDA 11.8
- **3D Processing**: Open3D 0.16.0
- **Camera SDK**: ZED SDK 4.0
- **Optimization**: TensorRT for inference acceleration

## Model Performance Comparison

| Model      | mIoU (%) | Overall Acc (%) | Jetson NX FPS | Memory (GB) |
| ---------- | -------- | --------------- | ------------- | ----------- |
| PointNet   | 73.2     | 89.1            | 28.7          | 0.8         |
| PVCNN      | 78.6     | 91.4            | 16.4          | 1.9         |
| SONATA     | 81.4     | 93.2            | 14.9          | 2.4         |
| RandLA-Net | 76.9     | 90.7            | 20.5          | 1.4         |

## Key Contributions

1. **Comprehensive Benchmarking**: Detailed performance analysis across multiple edge platforms
2. **Optimization Framework**: Memory and computational optimizations for edge deployment
3. **Real-time Integration**: Complete pipeline from ZED camera to semantic segmentation
4. **Practical Deployment**: Real-world validation on NVIDIA Jetson devices

## Results Highlights

- **Real-time Processing**: >20 FPS achieved on Jetson Xavier NX with PointNet
- **Memory Efficiency**: Optimized models fit within 8GB unified memory constraint
- **Accuracy Preservation**: <2% accuracy loss with optimization techniques
- **Hardware Integration**: Seamless ZED camera integration with <100ms latency

## Report Contents

The comprehensive 70-page report includes:

- **Chapter 1**: Introduction and objectives
- **Chapter 2**: Literature review of point cloud deep learning
- **Chapter 3**: Methodology and implementation details
- **Chapter 4**: Results and performance analysis
- **Chapter 5**: Technical implementation specifics
- **Chapter 6**: Discussion and challenges
- **Chapter 7**: Validation and real-world testing
- **Chapter 8**: Personal reflections and learnings

## Usage

### Compiling the Report

```bash
# Compile the LaTeX document
pdflatex Internship_Report_3D_PointCloud_Segmentation.tex
bibtex Internship_Report_3D_PointCloud_Segmentation
pdflatex Internship_Report_3D_PointCloud_Segmentation.tex
pdflatex Internship_Report_3D_PointCloud_Segmentation.tex
```

### Requirements

- LaTeX distribution (TeX Live 2023 or newer)
- Required packages: geometry, fancyhdr, titlesec, amsmath, graphicx, booktabs, listings, hyperref

## Implementation Files

- **`open3d/`**: Point cloud processing and visualization utilities
- **`pvcnn/`**: PVCNN model implementation and training scripts
- **`zed2i/`**: ZED camera integration and calibration code

## Datasets

- **ShapeNet**: Part segmentation benchmark dataset
- **Real-world data**: ZED 2i camera captures for validation

## Optimization Techniques

1. **Mixed Precision Training**: FP16 for memory efficiency
2. **Model Quantization**: INT8 inference acceleration
3. **Memory Management**: Optimized buffer allocation
4. **TensorRT Integration**: Runtime optimization for Jetson platforms

## Future Work

- Temporal consistency for video streams
- Advanced quantization techniques
- Federated learning across edge devices
- Multi-modal sensor fusion

## Author

**Arnav Kapoor**  
Intern, GeoAI4Cities Research Group  
Summer 2025

## Supervision

**Prof. Vaibhav Kumar**  
GeoAI4Cities Research Group

## Acknowledgments

Special thanks to Bhanu Pratap Singh for technical guidance and the GeoAI4Cities team for providing the research infrastructure and support throughout this internship.

---

_This work demonstrates the practical deployment of sophisticated 3D vision capabilities on edge computing platforms, contributing to the democratization of advanced AI technologies._
