# A variant of eriklindernoren's PyTorch-YOLOv3
This is a fork of https://github.com/eriklindernoren/PyTorch-YOLOv3.

My initial intent was to get rid of tensorboard and some of torch warnings.
I end up focussing on training with custom data as the original authors code is available at https://github.com/pjreddie/darknet, and comparison with respect to the original performace for pytorch implementation is done by eriklindernoren at https://github.com/eriklindernoren/PyTorch-YOLOv3. 

The codes are tested with Python 3.6.2 and torch 1.2.0.

## Main changes

* Dropped tensorboard and tensorflow dependencies
* Replaced ByteTensor with BoolTensor
* Removed weight loading functionality (pytorch trained model can be loaded fine)
* Removed a common data downloading script

## Installation
Clone and install requirements
```
$ git clone https://github.com/coyote4/PyTorch-YOLOv3.git
$ cd PyTorch-YOLOv3/
$ sudo pip3 install -r requirements.txt
```

## Usage

### Preparing custom dataset

To generate a custom YOLO model for your dataset, move to the configuration folder and create a custom model file.
```
$ cd config
$ bash create_custom_model.sh YOUR_NUMBER_OF_CLASS 
```
It creates a model file named 'yolov3-custom.cfg'.

List all class names in the following file with your favorite text editor or by a script. 
```
$ vim data/custom/classes.names
```
Eg, this file may contain something like below.
```
Cat
Dog
Horse
```
i.e., one class per line. 

Move the images of your dataset to the following folder.
```
$ mv YOUR_IMAGES data/custom/images
```

Move your annotations to the following folder.
```
$ mv YOUR_LABELS data/custom/labels
```
The dataloader expects that the annotation file corresponding to the image 'data/custom/images/train.jpg' has the path 'data/custom/labels/train.txt'. 
Each row in the annotation file should define one bounding box, using the syntax label_idx x_center y_center width height. 
The coordinates should be scaled in [0, 1], and the label_idx should be zero-indexed and correspond to the row number of the class name in 'data/custom/classes.names'.

You can split your datasets into training and validation data by using listFiles.py.
```
$ python listFiles.py 
```
It creates data/custom/train.txt and data/custom/valid.txt.

### Training example

```
$ python train.py --model_def config/yolov3.cfg --data_config config/custom.data
```

### Evaluating example

```
$ python detect.py --image_folder data/samples/ --checkpoint_model checkpoints/yolov3_ckpt_0.pth
```

## YOLOv3 paper

### YOLOv3: An Incremental Improvement
_Joseph Redmon, Ali Farhadi_ <br>

**Abstract** <br>
We present some updates to YOLO! We made a bunch of little design changes to make it better. We also trained this new network that’s pretty swell. It’s a little bigger than last time but more accurate. It’s still fast though, don’t worry. At 320 × 320 YOLOv3 runs in 22 ms at 28.2 mAP, as accurate as SSD but three times faster. When we look at the old .5 IOU mAP detection metric YOLOv3 is quite good. It achieves 57.9 AP50 in 51 ms on a Titan X, compared to 57.5 AP50 in 198 ms by RetinaNet, similar performance but 3.8× faster. As always, all the code is online at https://pjreddie.com/yolo/.

[[Paper]](https://pjreddie.com/media/files/papers/YOLOv3.pdf) [[Project Webpage]](https://pjreddie.com/darknet/yolo/) [[Authors' Implementation]](https://github.com/pjreddie/darknet)

```
@article{yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal = {arXiv},
  year={2018}
}
```
