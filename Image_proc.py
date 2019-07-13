from PIL import Image,ImageEnhance   # Import Required Library
import os
import datetime
import threading, time
import _thread

'''
The function that creats list of threads,
this is equal to no_of_thread.
'''
def cr_threads(n):
    ths=[]
    for i in range(n):
        t=threading.Thread(target=proc_image)
        ths.append(t)

    return ths

'''
The function that creats arrary of locks,
this is to ensure that the thread has complted cuuent tasks.
'''
def cr_locks():
    locks = []
    for i in range(no_of_thread):
        lck=_thread.allocate_lock()
        locks.append(lck)

    return locks

'''
The function process the images one at a time.
This would first acquire a lock , start processing and
release the lock at the end.
'''

def proc_image():

    if len(lst)==0:
        return

    img_name=lst.pop()
    try:
        lck=locks[th_idx]
        lck.acquire()
        im_path=os.path.join(img_src_path,img_name)
        im = Image.open(im_path)
        enhancer = ImageEnhance.Sharpness(im)
        im_enhanced=enhancer.enhance(factor)
        im_out_path=os.path.join(tgt_path,img_name)
        im_enhanced.save(im_out_path)
        lck.release()
        im.close()
        im_enhanced.close()
    except:
        print('Error Proceiing the File: '+ img_name)
        lst.append(img_name)

'''
Crate Image lists, threads and locks,
then start processing each image while image list is not empty
'''

factor =2     # Enhancement Factor
no_of_thread =10  # Total No of threads , eqaual to the total no of parallel processing
sleep_time = 1  # Time Gap betweeen each Batch
th_idx=0; # Used to track the thread number
img_src_path = 'images'
img tgt_path = 'output'

lst=os.listdir(path=img_src_path)
threads=cr_threads(no_of_thread)
locks = cr_locks(no_of_thread)

while(len(lst)>0):
    threads=cr_threads(no_of_thread) # Create new thread set
    th_idx=0;
    for t in threads:
        t.start()
        th_idx+=1
