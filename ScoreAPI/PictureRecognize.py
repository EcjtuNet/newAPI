#coding:utf-8
from PIL import Image,ImageEnhance,ImageFilter,ImageDraw
import pytesser
import re

def captchaRecognize(img):
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
    #识别修改后的图片
    text = pytesser.image_to_string(img)
    #使用正则表达式过滤除数字以外的识别数据
    captcha = re.findall('[0-9]',text)
    captcha =  ''.join(captcha)
    print captcha
    return captcha

def getCaptcha(picture):
        local = open('cod.jpg', 'wb')
        local.write(picture)
        local.close()
        # 保存验证码到本地
        img = Image.open('cod.jpg')
        captcha = captchaRecognize(img)
        return captcha
