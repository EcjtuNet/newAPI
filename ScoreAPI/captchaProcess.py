#coding:utf-8
from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
import pytesser
import re
# 处理图片便于进行识别，返回处理后的图片
def pictureProcess(img):
    #无限中值过滤噪点
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    img = img.filter(ImageFilter.MedianFilter())
    #锐化等处理图片
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img = img.convert('L')
    enhancer=ImageEnhance.Color(img);
    enhancer=enhancer.enhance(0);   #变成黑白
    enhancer=ImageEnhance.Contrast(enhancer);
    enhancer=enhancer.enhance(8);   #提高对比度
    img = enhancer
    return img

# 识别验证码，并返回验证码识别结果
def captchaRecognize(captchaImg):
    #识别修改后的图片
    text = pytesser.image_to_string(captchaImg)
    #使用正则表达式过滤除数字以外的识别数据
    captcha = re.findall('[0-9]',text)
    captcha =  ''.join(captcha)
    if len(captcha)!=4:
        return 0
    else:
        return captcha

def openImg(imgName):
    img = Image.open('cod.jpg')
    return img
