import face_recognition as fc
import cv2
import numpy as np
import pandas as pd
import time as t
#Data = pd.DataFrame(columns = ['Name','Semail','Pemail','SPhone','PPhone'])
#Data = pd.read_csv('/home/deepak/Techie_data/Attendance/SData.csv')
v = cv2.VideoCapture(0) #'http://100.91.199.131:8080/video'
fd = cv2.CascadeClassifier('/home/deepak/Techie_data/haarcascade_frontalface_default.xml')
#EN =pd.DataFrame(columns=[])
#EN = pd.read_csv('/home/deepak/Techie_data/Attendance/Encodings.csv')
Q=1
while(Q):
    while(1):
        ret,i=v.read()
        if ret:
            j = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
            f = fd.detectMultiScale(j)        
            if (len(f)==1):
                for (x,y,w,h) in f:
                    cv2.rectangle(i,(x,y),(x+w,y+h),(255,0,0),2)
                    crop_img = i[y:y+h, x:x+w]
                    fl = fc.face_locations(crop_img)
                    if(len(fl)>0):
                        print('Say Cheese!!')
                        Fe = fc.face_encodings(crop_img,fl)[0]
                        
                    else:
                        print('fl is empty')
            else:
                print('No/Multiple Face Detected')
            cv2.imshow('Image',i)
            k = cv2.waitKey(5)
            if(k==ord(' ')):
                cv2.destroyAllWindows()
                break
    #v.release()
    name = input("Enter Name \n")
    sid = input("Enter Your Mail ID :\n")
    pid = input("Enter Your Parent Mail ID:\n")
    smob = input("Enter Your Mobile No. : \n")
    pmob = input("Enter Your Parent Mobile No. : \n")
    p = pd.DataFrame(data=[[name,sid,pid,smob,pmob]],columns=['Name','Semail','Pemail','SPhone','PPhone'])
    Data = pd.read_csv('/home/deepak/Techie_data/Attendance/SData.csv',index_col=False)
    Data=pd.concat([Data,p],axis = 0,ignore_index = True)
    Data = Data.to_csv('/home/deepak/Techie_data/Attendance/SData.csv',index=False)
    save = cv2.imwrite('/home/deepak/Techie_data/Attendance/Student Data/'+str(smob)+'.jpeg',crop_img)
    d = pd.read_csv('/home/deepak/Techie_data/Attendance/attend.csv',index_col=False)
    d2 = pd.DataFrame(data=[[name]],columns=['Name'])
    d = d.append(d2,ignore_index=True)
    d.to_csv('/home/deepak/Techie_data/Attendance/attend.csv',index=False)
    #Fe1 = pd.DataFrame(np.array([Fe]))
    
    EN = pd.read_csv('/home/deepak/Techie_data/Attendance/Encodings.csv',index_col=False)
    EN = np.array(EN)
    c = np.concatenate((EN,[Fe]),axis=0)
    c1 = pd.DataFrame(c)
    c1.to_csv('/home/deepak/Techie_data/Attendance/Encodings.csv',index = False)
    print('Registration Completed :'+str(name)) 
    Exit = input('Press Exit/C to TERMINATE/Continue :\n')
    
    if(Exit== 'E'):
        Q = 0
        v.release()
    else:
        Q = 1


