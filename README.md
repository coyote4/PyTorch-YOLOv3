# A variant of eriklindernoren's PyTorch-YOLOv3
This is a fork of https://github.com/eriklindernoren/PyTorch-YOLOv3.

My initial intent was to get rid of tensorboard and some of torch warnings.
I end up focussing on training with custom data as the original authors' code is available at https://github.com/pjreddie/darknet, and comparison with respect to the original performace for pytorch implementation is done by eriklindernoren at https://github.com/eriklindernoren/PyTorch-YOLOv3. 

The codes are tested with Python 3.6.2 and torch 1.2.0.

## Main changes

* Dropped tensorboard and tensorflow dependencies
* Replaced ByteTensor with BoolTensor
* Removed weight loading functionality (pytorch trained YOLO model file can be loaded)
* Removed a common data downloading script

## Installation
Clone the code and install required libraries.
```
$ git clone https://github.com/coyote4/PyTorch-YOLOv3.git
$ cd PyTorch-YOLOv3/
$ sudo pip install -r requirements.txt
```

## Sanity check
Let us see if the code works.
```
$ python listFiles.py
$ python train.py
$ python detect.py
```
If no error is printed out, the code works! 

## Usage

### Preparing custom dataset

To generate a custom YOLO model for your dataset, move to the configuration folder and create a custom model file.
```
$ cd config
$ bash create_custom_model.sh YOUR_NUMBER_OF_CLASSES 
```
It creates a model file named 'yolov3-custom.cfg'.

Check 'config/custom.data' file and make it matched to your dataset.
```
$ vim config/custom.data
```

List all class names in the following file with your favorite text editor (or you may write a simple script to dump your class names into the file). 
```
$ cd ..
$ vim data/custom/classes.names
```
e.g., this file may contain something like below.
```
Cat
Dog
Horse
```
i.e., one class per line. 

Clear example files and move the images of your dataset to the following folder.
```
$ rm data/custom/images/*jpg
$ mv YOUR_IMAGES data/custom/images
```

Clear example files and move your label files to the following folder.
```
$ rm data/custom/labels/*txt
$ mv YOUR_LABELS data/custom/labels
```

When the image data are loaded in, the label files are also loaded by locating them in 'data/custom/labels/YOUR_FILE.txt'.
i.e., the names of image files are already matched to the names of lable files. 'data/custom/images/YOUR_FILE.jpg' and 'data/custom/labels/YOUR_FILE.txt'. 

Each row in the label file contains one bounding box; 'label_idx x_center y_center width height', scaled in [0,1].
The label_idx is zero-indexed (the smallest class-name index is 0 instead of 1) and corresponds to the row number of the class name in 'data/custom/classes.names'. 
e.g.,
```
0 0.5 0.5 0.2 0.3
```
means that a cat is at the center of an image with width of 0.2 and height of 0.3. 

You can split your datasets into training and validation data by using listFiles.py.
```
$ python listFiles.py 
```
It creates data/custom/train.txt and data/custom/valid.txt.

### Training example

Pick the number of training epochs, batch size, and checkpoints. 
Then run the training code.
```
$ python train.py --epochs YOUR_EPOCHS  --batch_size YOUR_BATCH_SIZE --checkpoint_interval YOUR_CHECK --model_def yolov3-custom.cfg --data_config config/custom.data
```

### Evaluating example

Check checkpoint files in checkpoints folder and pick one for evaluation.
Clear example files and place few images in data/samples for testing your trained model.
```
$ rm data/samples/*jpg
$ mv YOUR_TEST data/samples
$ python detect.py --image_folder data/samples/ --checkpoint_model checkpoints/yolov3_ckpt_YOUR_CHECKPOINT.pth
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
