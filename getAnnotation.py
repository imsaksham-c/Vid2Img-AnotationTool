import os
import subprocess

dir = './data_new/'  #path to folder containing videos


listfiles =[]
for img_files in os.listdir(dir):
    if img_files.endswith(".mp4"):
        listfiles.append(img_files)
        
len(listfiles)



for vid in listfiles:
    
    video_file = dir+vid
    base = './data_new/'+vid
    vid_name = os.path.splitext(vid)[0]
    
    run = 'python detect.py --source '+base+' --weights yolov5x6.pt --conf 0.3 --img-size 1080 --device 0 --name '+vid_name+' --save-txt --classes 0'

    
    try:

        subprocess.call(run, shell=True)
        
        print('Done--------------------------------------------------------------------------------------------------------Done')

    except:
        print('Error')
        
        
        
print('*****************************end**************************************')
  
