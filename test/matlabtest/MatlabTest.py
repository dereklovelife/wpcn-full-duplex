#_*_ coding:utf8 _*_

## Import matlab 包
import matlab.engine
import os

## 切换工作目录（必须保证我们写的matlab的.m文件在工作目录下）
## 在这里我将我自己写的InitChannel.m放在了D:\wpcn-full-duplex\mat

os.chdir("D:\wpcn-full-duplex\mat")

## 获取到matlab engine，之后调用matlab文件，就通过这个engine调用

eng = matlab.engine.start_matlab()

## 调用matlab函数（InitChannel)
## 其中，nargout参数表示matlab函数的返回值是几个参数（matlab函数可以返回多个值）
## 这里是一个，如果是两个可以写成： a,b = eng.InitChannel(3, 4, nargout = 2)  利用python的自动拆包
a = eng.InitChannel(3, 4, nargout = 1)

## 打印下最后的结果
for line in a:
    print line

