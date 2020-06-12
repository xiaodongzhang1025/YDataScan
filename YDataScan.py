#coding:utf-8
__author__ = 'zhangxd18'
import sys
import os
import codecs
import re
import Tkinter
import tkMessageBox
import tkFileDialog
import Canvas
from PIL import Image
from PIL import ImageTk

width = 640
height = 480
def select_file_path():
    path = tkFileDialog.askopenfilename()
    dstFilePath.set(path)
    
def start_analyze():
    global img
    global canvas_img
    print dstFilePath.get()
    #print dir(canvas_dst)
    img = Image.new('L', (width, height), 128)
    
    data = []
    with open(dstFilePath.get(), "rb") as file:
        data = file.read(width*height)
        print len(data)
    print '------------------------'
    for i in range(width):
        for j in range(height):
            img.putpixel( (i, j), ord(data[j*width+i]) )
    #img.show()
    
    canvas_img = ImageTk.PhotoImage(img)  
    canvas_dst.create_image(2, 2, anchor='nw', image=canvas_img)
    
    #canvas_dst.update()
    root.update()
    root.after(10)
    #tkMessageBox.showinfo('tips', '分析结束')
    
if "__main__" == __name__:
    #print sys.argv[1]
    canvas_img = None
    img = None
    
    root = Tkinter.Tk()
    dstFilePath = Tkinter.StringVar()
    
    #root.withdraw()
    Tkinter.Label(root, text = '目标文件：').grid(row = 0, column = 0)
    Tkinter.Entry(root, textvariable = dstFilePath).grid(row = 0, column = 1)
    Tkinter.Button(root, text = '文件选择', command = select_file_path).grid(row = 0, column = 2)
   
    Tkinter.Button(root, text = '开始分析', command = start_analyze).grid(row = 1, column = 2)
    #'''
    canvas_dst = Tkinter.Canvas(root, width=width, height=height, bg='blue')  # 设置画布
    canvas_dst.grid(row = 2, column = 1)
    canvas_dst.create_line(0, 100, width, 100, width=5, fill='red')
    canvas_dst.create_line(0, 200, width, 200, width=15, fill='green')
    
    #'''
    root.mainloop()
