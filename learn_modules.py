#modules
"""
modules =  collection of functions,variables,class -> math,random,calendar,webbrowser,pywhatkit,time,datetime
package = collction of modules ->numpy,pandas,scipy,matplotlib
"""
import datetime
import datetime as dt
# ct = datetime.datetime.now()
# print(ct)
# print(ct.year)
# print(ct.month)
# print(ct.day)
# print(ct.hour)
# print(ct.minute)
# tt = dt.datetime(2027,1,1,0,0,0,000000)
# print(tt)
# print(tt.year)
# print(tt.month)
#
# #find nw year date
# print(tt-ct)



import pywhatkit as pk

# pk.search("Vijay")
# pk.playonyt("TVK")
# pk.sendwhatmsg_instantly("+91 9442546863","Hello Kasinathan")
#pk.show_history()


import webbrowser as wb
# wb.open_new("https://ugc.vinayakamission.com/university")
# wb.open_new_tab("https://livewiresalem.com/gallery.php")


import time as t

# print("Bye Java")
# t.sleep(5)
# print("Hello Python")
# print(t.ctime())

# print(t.strftime("%d-%m-%y %H:%M:%S"))



#pillow
from PIL import Image

# img = Image.open(r"C:\Users\prave\OneDrive\Pictures\MSD.jpg")
# img=img.resize((400,700))
# img.show()


import pygame as pg
import time
pg.init()
ps = pg.display.set_mode((600,500))#to initiate frame
ps1 = pg.image.load(r"C:\Users\prave\OneDrive\Pictures\demo1.jpg")#initate the image
ps.blit(ps1,(50,50))#to combaine the frame and image
pg.display.update()
time.sleep(5)#to hold the process
pg.quit()


















