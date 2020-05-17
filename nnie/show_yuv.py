from numpy import *
from PIL import Image
import os,sys

def readYuvFile(filename,width,height):
    fp=open(filename,'rb')
    uv_width=width//2
    uv_height=height//2

    Y=zeros((height,width),uint8,'C')
    U=zeros((uv_height,uv_width),uint8,'C')
    V=zeros((uv_height,uv_width),uint8,'C')

    for m in range(height):
        for n in range(width):
            Y[m,n]=ord(fp.read(1))
            #print("{0},{1}".format(m,n))
    for m in range(uv_height):
        for n in range(uv_width):
            V[m,n]=ord(fp.read(1))
            U[m,n]=ord(fp.read(1))

    fp.close()
    return (Y,U,V)

def yuv2rgb(Y,U,V,width,height):
    U=repeat(U,2,0)
    U=repeat(U,2,1)
    V=repeat(V,2,0)
    V=repeat(V,2,1)
    rf=zeros((height,width),float,'C')
    gf=zeros((height,width),float,'C')
    bf=zeros((height,width),float,'C')

    rf=Y+1.14*(V-128.0)
    gf=Y-0.395*(U-128.0)-0.581*(V-128.0)
    bf=Y+2.032*(U-128.0)

    for m in range(height):
        for n in range(width):
            if(rf[m,n]>255):
                rf[m,n]=255;
            if(gf[m,n]>255):
                gf[m,n]=255;
            if(bf[m,n]>255):
                bf[m,n]=255;

    r=rf.astype(uint8)
    g=gf.astype(uint8)
    b=bf.astype(uint8)
    return (r,g,b)

if __name__=='__main__':
	width=416
	height=416
	filename = sys.argv[1]
	print(filename)
	data=readYuvFile(filename, width, height)
	#Y=data[0]
	#im=Image.frombytes('L',(width,height),Y.tostring())
	#im.save('y.jpg')
	#im.show()

	RGB=yuv2rgb(data[0],data[1],data[2],width,height)
	im_r=Image.frombytes('L',(width,height),RGB[0].tostring())
	im_g=Image.frombytes('L',(width,height),RGB[1].tostring())
	im_b=Image.frombytes('L',(width,height),RGB[2].tostring())
	im_rgb=Image.merge('RGB',(im_r,im_g,im_b))
	im_rgb.save('temp.jpg')
	#im_rgb.show()
