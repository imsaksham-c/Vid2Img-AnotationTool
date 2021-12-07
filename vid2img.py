import cv2
import os

def Vid2Img(path, vid):
    
    cam = cv2.VideoCapture(path)    
    currentframe = 1
    while(True):
        ret,frame = cam.read()

        if ret:
            img_name = base + vid + '_' + str(currentframe) + '.jpg'
            txt_name = base + vid + '_' + str(currentframe) + '.txt'
            cv2.imwrite(img_name, frame)
            
            f = open(txt_name, "a")
            f.close()
            
            
            currentframe += 1
            
        else:
            break
    cam.release()
    cv2.destroyAllWindows()
    
    return("Done................!!", base)



dir = './video_data_folder/'  # path to folder containing videos


listfiles =[]
for img_files in os.listdir(dir):
    if img_files.endswith(".mp4"):
        listfiles.append(img_files)
        
len(listfiles)


for vid in listfiles:
    
    vid_name = os.path.splitext(vid)[0]
    video_file = dir+vid
    base = './custom_data/'
    if not os.path.exists(base):
        os.mkdir(base)
        
    base = './custom_data/'+vid_name+'/'
    
    try:

        if not os.path.exists(base):
            os.mkdir(base)

    except:
        print('Error: Creating directory of data')
        
    
    print(Vid2Img(video_file, vid_name))
