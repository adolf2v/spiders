# coding:utf-8
"""
author：xiaoqiang
date:2016-09-22
需要下载pillow的库
需要下载pytesseract的库
需要下载汉字的字体库,chi-sim.traineddata，下载地址：https://pan.baidu.com/s/1pK7jNAj，解压后放到对应的tessdata文件夹即可
用于测试的验证码图片:2.gif
用户测试汉字的验证码图片:sim.png

"""
#从PIL库导入Image,用于生成Image对象
from PIL import Image
#导入image_to_string的方法,并命名为its
from pytesseract import image_to_string as its
#Image.open 2.gif
im1 = Image.open("2.gif")
#打印2.gif图片中的内容
print its(im1)
#Image.opensim.png
im = Image.open("sim.png")
# 打印图片内容
print its(im, lang="chi_sim")
