# A variant of eriklindernoren's PyTorch-YOLOv3
This is a fork of https://github.com/eriklindernoren/PyTorch-YOLOv3.

My initial intent was to get rid of tensorboard and some of torch warnings.
I end up focussing on training with custom data as the original authors code is available at https://github.com/pjreddie/darknet, and comparison with respect to the original performace for pytorch implementation is done by eriklindernoren at https://github.com/eriklindernoren/PyTorch-YOLOv3. 

The codes are tested with Python 3.6.2 and torch 1.2.0.

## Main changes

* Dropped tensorboard and tensorflow dependencies
* Replaced ByteTensor with BoolTensor
* Removed weight loading functionality (pytorch trained model can loaded fine)
* Removed a common data downloading script

## Installation
Clone and install requirements
   $ git clone https://github.com/coyote4/PyTorch-YOLOv3.git
   $ cd PyTorch-YOLOv3/
   $ sudo pip3 install -r requirements.txt

## Usage

### Preparing custom dataset
to be filled

### Training example
to be filled

### Testing example
to be filled

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
