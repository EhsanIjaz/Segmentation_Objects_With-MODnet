import tensorflow as tf
import numpy as np 
import scipy.io  
import argparse 
import struct
import errno
import time                       
import cv2
import os
import sys

from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))


def main():
    # content_dir = "./NFTs/cnt_img/"
    # Fr_style_dir = "./NFTs/style/Fg_style/"    
    # Bk_style_dir = "./NFTs/style/Bk_style/"
    # result_dir = "./NFTs/cnt_img/"

    content_dir = str(sys.argv[1])
    Bk_style_dir = str(sys.argv[2])
    Fr_style_dir = str(sys.argv[3])    
    result_dir = str(sys.argv[4])
    
    content_img_list = os.listdir(content_dir)
    fr_style_img_list = os.listdir(Fr_style_dir)
    bk_style_img_list = os.listdir(Bk_style_dir)

    # generated_fr_imges = os.listdir(result_dir)
    # print(generated_fr_imges)
    # print(len(generated_fr_imges))
    
    # content_img = "1.jpg"
    # style_mask_imgs = "1_fg.jpg"
    # style_img = "fg_1.jpg"


    # Firstly we created a code for foreground mask 

    content_img_list_final = []

    for i in content_img_list:
        ftr = i.split('.')[0].split('_')[0]
        content_img_list_final.append(ftr)
    
    content_img_list_final = sorted(set(content_img_list_final))
    # print(content_img_list_final)

    for i in content_img_list_final:
        content_img = i + '.png'
        style_mask_imgs = i + '_fg.png'

        content_img_val = content_img.split('.')[0]
        # print(content_img_val)
        for j in fr_style_img_list:
            style_img = j
            style_img_val = str(style_img.split('.')[0])
            
            if os.path.isfile(f'{content_dir}/{content_img_val}_{style_img_val}.png'):
                pass
            else :
                os.system(f'python neural_style_bydefault.py --content_img_dir {content_dir} \
                            --img_output_dir {content_dir} \
                            --style_imgs_dir {Fr_style_dir} \
                            --content_img {content_img} \
                            --style_imgs {style_img} \
                            --max_size 1000 \
                            --max_iterations 200 \
                            --style_mask \
                            --style_mask_imgs {style_mask_imgs} \
                            --verbose;')

    # After created stylized foreground content images we will build a code for background mask.
    
    for i in content_img_list_final:
        # content_img = i + '_output.png'
        style_mask_imgs = i + '_bk.png'

        for j in bk_style_img_list:
            style_img = j
            style_img_val = str(j.split('.')[0])
            content_img = i +'_'+style_img_val+'.png'

            if os.path.isfile(f'{content_dir}{i}_{style_img_val}.png'):
                os.system(f'python neural_style_bydefault.py --content_img_dir {content_dir} \
                        --img_output_dir {result_dir} \
                        --style_imgs_dir {Bk_style_dir} \
                        --content_img {content_img} \
                        --style_imgs {style_img} \
                        --max_size 1000 \
                        --max_iterations 200 \
                        --style_mask \
                        --style_mask_imgs {style_mask_imgs} \
                        --verbose;')    
            else :
                pass
        
    # return 0 

if __name__ == '__main__':
    main()

# python neural_style_bydefault.py --content_img "./NFTs/cnt_img1/24.jpg" --style_imgs "./NFTs/cnt_style_1/8.jpg" --max_size 1000 --max_iterations 200 --original_colors --style_mask --style_mask_imgs "./NFTs/cnt_img1/23_mask.jpg" --verbose