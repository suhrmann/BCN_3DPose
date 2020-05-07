# BCN_3DPose
Bayesian Capsule Networks for 3D human pose estimation from single 2D images
https://www.sciencedirect.com/science/article/pii/S092523121931522X

## Branch ``amass``
Adjustments to test [BCN_3DPose](https://amass.is.tue.mpg.de) agains AMASS dataset. 

## Demo
**_click on the image below for a video demo_**
[![Watch the video](https://img.youtube.com/vi/cJsPnm-T9cA/maxresdefault.jpg)](https://youtu.be/cJsPnm-T9cA)


# Run

### Setup
Extract contents of 
 - ``Data3D.zip`` to project root (see [Download Dataset](#download-dataset))
 - ``Model.zip`` to ``Models/Model_BCN_3D`` (see [Download Trained Model](#download-trained-model))

**Expected structure:**
```bash
$ tree
BCN_3DPose
├── Data3D -> ../Data3D
│   ├── train
│   ├── train2d
│   ├── train2d_bb
│   ├── train_bg
│   ├── train_bg17
│   ├── validation
│   ├── validation2d
│   ├── validation2d_bb
│   ├── validation_bg
│   └── validation_bg17
├── LICENSE
├── main.py
├── Models
│   └── Model_BCN_3D -> ../../Model
│       ├── checkpoint
│       ├── model.ckpt.data-00000-of-00001
│       ├── model.ckpt.index
│       ├── model.ckpt.meta
│       ├── TOTAL_by_activity.npy
│       └── TOTAL.npy
├── plotALL.py
├── README.md
├── train.py
└── utils
    ├── children_b.mat
    └── children.mat

```

### Training
```bash
python main.py train
```

### Test
```bash
python main.py test
```

### Video Test
```bash
python main.py test_video
```


# Download Dataset
https://urjc-my.sharepoint.com/:u:/g/personal/ivan_ramirez_urjc_es/Ec3Xu8zlV_xLkjE4cWPlTpoB_kznscM98bANGyM9Nbhb5Q?e=4%3anXkVj8&at=9
# Download Trained Model
https://urjc-my.sharepoint.com/:f:/g/personal/ivan_ramirez_urjc_es/EsopUGOLPDROn9jfE1DCpBwBMAcSQ2pfaTLqU21FN6K42w?e=5%3aqNQa00&at=9


# Requirements

Project Repository comes with:
 - ~~Python 2~~ Python 3 (project upgraded to Python 3)
 - Tensorflow 1 (TF-2 is work in progress in branch [tf-2](https://github.com/suhrmann/BCN_3DPose/tree/tf-2))

1. [Optional] Create anaconda environment (recommendet) <br/>
    More information about [conda / anaconda [conda.io]](https://docs.conda.io/en/latest/)
    ```bash
    # Create env "BCN_3DPose" with Python 3.7 and PIP
    conda create --name BCN_3DPose python=3.7 pip
    # Activate this environment
    conda activate BCN_3DPose # activate 
    ```

2. Install **Tensorflow** for your platform using ``conda`` <br />
    For other install options see [Install TensorFlow [tensorflow.org]](https://www.tensorflow.org/install)
    ```bash
    # Install Tensorflow 1(!)
    conda install tensorflow-gpu==1.15 # Tensorflow 1
    ```

2. Install project dependencies
    ```bash
    conda install opencv scipy Pillow matplotlib tqdm
    ```


### FAQ

 - **``ffmpeg`` missing** <br>
     Replace conda ``ffmpeg`` with built-in ``ffmpeg`` of Ubuntu
     
    ```bash
    # "disable" conda ffmpeg 
    which ffmpeg  # -> Output: /home/simon/.conda/envs/OpenCV/bin/ffmpeg
    cd /home/simon/.conda/envs/OpenCV/bin
    mv ffmpeg ffmpeg_BAK
    # Replace with Ubuntu ffmpeg
    which ffmpeg  # Expecting path to Ubuntu ffmpeg - Output: /usr/bin/ffmpeg
    ln -s /usr/bin/ffmpeg ffmpeg  # Link conda ffmpeg to built in
    
    ```
    More details in my post in issue [ OpenCV disabling libopenh264 for ffmpeg #131 [Github]](https://github.com/conda-forge/opencv-feedstock/issues/131#issuecomment-625259442)
