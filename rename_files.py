import sys
import os



if __name__ == '__main__':

  cnt_img_dir = str(sys.argv[1])
  Bk_style_dir = str(sys.argv[2])
  Fg_style_dir = str(sys.argv[3])    
  temp_dir = str(sys.argv[4])


  for count, filename in enumerate(os.listdir(cnt_img_dir)): 
    dst = str(count) + ".png"
    src = cnt_img_dir + filename 
    dst = temp_dir + dst 
    os.rename(src, dst)
    os.system(f"mv {temp_dir}* {cnt_img_dir}")

  for count, filename in enumerate(os.listdir(Bk_style_dir)): 
    dst = str(count) + ".png"
    src = Bk_style_dir + filename 
    dst = temp_dir + dst 
    os.rename(src, dst)
    os.system(f"mv {temp_dir}* {Bk_style_dir}")

  for count, filename in enumerate(os.listdir(Fg_style_dir)): 
    dst = str(count) + ".png"
    src = Fg_style_dir + filename 
    dst = temp_dir + dst 
    os.rename(src, dst)
    os.system(f"mv {temp_dir}* {Fg_style_dir}")

  print("Renamed all files which is mentioned in cnt_img, bk_style, fg_style !!!!")
