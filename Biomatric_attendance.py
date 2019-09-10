import face_recognition as fc
import cv2
import numpy as np
import pandas as pd
from datetime import date
import smtplib as s
import random as rd
today=date.today()
def mail_student(student_name):
    c=name.index(student_name)
    #otp=rd.randint(1000,9999)
    e=str(student_name)+' your otp is '+str(otp)
    m=s.SMTP('smtp.gmail.com',587)
    m.starttls()
    m.login('itsmesender@gmail.com','sender123')
    m.sendmail('itsmesender@gmail.com',emailid[c],e)
    m.close()
def mail_parents(student_name):
    c=name.index(student_name)
    x=student_record(student_name)
    m=s.SMTP('smtp.gmail.com',587)
    m.starttls()
    m.login('itsmesender@gmail.com','sender123')
    m.sendmail('itsmesender@gmail.com',parents_emailid[c],x)
    m.close()
def student_record(student_name):
    c=name.index(student_name)
    f=list(atd.iloc[c])
    total_present=f.count('p')
    total_absent=f.count('a')
    patd=total_present*100/(total_present+total_absent)
    percentage_attendance=patd
    daily_atd=atd.iloc[c]
    h='Dear parents attendance rec of your ward is as follows'+'\n'+'total_present='+str(total_present)+'\n'+'total_absent='+str(total_absent)+'\n'+'percentage_attendance='+str(percentage_attendance)+'\n'+'daily_atd='+str(daily_atd)
    return h
v=cv2.VideoCapture(0)
en=pd.read_csv('/home/deepak/Techie_data/Attendance/Encodings.csv')
data=pd.read_csv('/home/deepak/Techie_data/Attendance/SData.csv')
name=list(data['Name'])
emailid=list(data['Semail'])
parents_emailid=list(data['Pemail'])
contact=list(data['PPhone'])

en_array=np.array(en)
fe=[]
for r in range(0,en.shape[0]):
    fe.append(en_array[r])
q=1
p=[]
z=[]
while(q<10):
    ret,i=v.read()
    fl=fc.face_locations(i)
    #cv2.imshow('image',i)
    if (len(fl)>0):
        print(fl)
        Fe=fc.face_encodings(i,fl)
        #print(Fe)
        Flc=fc.compare_faces(fe,Fe[0])
        if(True in Flc):
            ind=Flc.index(True)
            b=name[ind]
            print(name[ind])
            if(b in p):
                pass
            else:
                p.append(b) 
            for(x1,y2,x2,y1)in fl:
                cv2.rectangle(i,(x1,y1),(x2,y2),(0,0,255),5)
           
        elif(False in Flc):
            print('face not recognized')
    elif(len(fl)==0):
        print('face is not available')
    q=q+1
atd=pd.read_csv('/home/deepak/Techie_data/Attendance/attnd_reg.csv')
#d=pd.DataFrame({'name':['Raunak','Obama','Trump']})
for j in range(0,len(name)):
    if(atd['name'][j] in p):
        otp=rd.randint(1000,9999)
        mail_student(atd['name'][j])
        n=int(input(str(atd['name'][j])+' enter otp'))
        if(n==otp):
            z.append('p')
            print('attendance marked successfully')
        else:
            print('otp incorrect')
            z.append('a')
    else:
        z.append('a')
today_atd=pd.DataFrame({today.strftime('%d/%m/%y'):z})
atd=atd.join(today_atd)
print(atd)
atd.to_csv('/home/deepak/Techie_data/Attendance/attnd_reg.csv',index=False)
o=1
while(o):
    w=int(input('''choose the operation you want to perform:
    1.view student record
    2.send student record to parents
    3.quit \n'''))
    if(w==1):
        t=input('enter student name ')
        b1=student_record(t)
        print(b1)
    elif(w==2):
        u=input('enter student name ')
        mail_parents(u)
    elif(w==3):
        o=0

k=cv2.waitKey(1)
if(k==ord('q')):
      
    v.release()
