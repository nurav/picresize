from PIL import Image as image
from os import listdir
import os.path 


for f in listdir(os.path.dirname(os.path.realpath(__file__))):
    
    
    try:
        img=image.open(f)
        width,height=img.size
        newimg=img.resize((width/4,height/4))
        head,tail=os.path.split(f)
        
        tail='.'.join(tail.split('.')[:-1])+'(resize).'+tail.split('.')[-1]
        
        
        print os.path.join(head,tail)
        newimg.save(os.path.join(os.path.dirname(os.path.realpath(__file__)),tail))
        print '%s not an image' %f
    except IOError:
        
        pass
    
    
    
    
    
    
        
        
