# EasyOcr Learning
The project structure is as follows.

```
├── /step3
│   ├── /training
│   │   └── /kordata
│   │       ├── data.lmdb
│   │       └── data.lmdb
│   ├── /validation
│   └── /test
│
├── /pre_trained_model
│   # Path of the pre-trained model file to be used in the capstone project
│   └── korean_g2.pth
│
├── /user_network_dir
│   # Storage path for user models and configuration files to be used by EasyOCR project
│   ├── custom.pth
│   ├── custom.py
│   └── custom.yaml
│
└── /demo_images
    # Test images to verify the performance of the learned model
    ├── demo_01.png
    ├── demo_02.png
    └── ...
```
