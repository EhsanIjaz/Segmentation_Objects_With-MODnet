# Some basic setup:
# Setup detectron2 logger
import detectron2
from detectron2.utils.logger import setup_logger
setup_logger()

# import some common libraries
import numpy as np
import os, json, cv2, random
from google.colab.patches import cv2_imshow

# import some common detectron2 utilities
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog, DatasetCatalog
import sys

def process(cnt_img_dir,img_name,im):
  cfg = get_cfg()
  # add project-specific config (e.g., TensorMask) here if you're not running a model in detectron2's core library
  cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
  cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
  # Find a model from detectron2's model zoo. You can use the https://dl.fbaipublicfiles... url as well
  cfg.MODEL.WEIGHTS = model_zoo.get_checkpoint_url("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml")
  predictor = DefaultPredictor(cfg)
  outputs = predictor(im)

  i = outputs['instances'].to('cpu')
  mask_img = i.pred_masks[0].numpy()*255
  cv2.imwrite(f"{cnt_img_dir}{img_name}_fg.png", mask_img)
  m_i = np.invert(i.pred_masks[0].numpy())*255
  cv2.imwrite(f"{cnt_img_dir}{img_name}_bk.png",m_i)

  # return 0

# def main():
#   folder_img = os.listdir("./NFTs/cnt_img/")
#   for i in folder_img:
#     img_name = i.split('.')[0]
#     im = cv2.imread(f"./NFTs/cnt_img/{i}")
#     process(img_name,im)
#   return 0

if __name__ == '__main__':
  cnt_img_dir = str(sys.argv[1])
  folder_img = os.listdir(cnt_img_dir)
  for i in folder_img:
    img_name = i.split('.')[0]
    im = cv2.imread(f"{cnt_img_dir}{i}")
    process(cnt_img_dir,img_name,im)
  # return 0

    # main()
