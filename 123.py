
from PIL import Image 
n = input("введите путь к фотографии ( а то работать не будет )") 
im = Image.open (n) 
pixels = im.load() 



im.show() 


#это комментарий 
for i in range (im.width): 
    for j in range (im.height): 
        r,g,b = pixels [i,j] 
        #a = (r+5,g-15,b+10) 
        v = (r+g+b)//3
        if g>r and g>b :
            pixels [i,j] = (v,v,v)

            im.show()


 
for i in range (im.width): 
    for j in range (im.height): 
     r,g,b = pixels [i,j] 
     a = (r+5,g-15,b+10) 
     v = (r+g+b)//3 
     if b>r and b>g : 
         pixels [i,j] = (v,v,v) 

    im.save("result.jpg"); 


    

print(im.width) 
print(im.height) 
print(im.mode) 

im.show() 

