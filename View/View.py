import pygame
import os
import View.const as const
import time as t
class ImageObject():
    def __init__(self,pos=None,pic=None):
        self.pos = pos
        self.pic = pic
        self.pic_size = pic.get_rect()

    def blit(self,screen):
        image_rect = (self.pos[0],self.pos[1],
                    self.pic_size[0],self.pic_size[1])
        screen.blit(self.pic,image_rect)

class View:
    def __init__(self):
        self.mapElements = {}
        self.MAP_PATH = "../data/"
        self.state = None
        self.objDict = {}
        self.gameScreen = pygame.display.set_mode(const.WINDOW_SIZE)
    ### Loads the image from MAP_PATH, stores them in map_elements.
    
    def initView(self):
        print("init View...")
        elementsPath = os.listdir(self.MAP_PATH)
        elementsName = map(lambda x:x.replace(".png",""),elementsPath)
        for name in elementsName:
            self.loadImage(name)
            print(name, "Loaded")
        pygame.init()
        pygame.display.init()
    
    ### Loads and rescale the image 
    def loadImage(self,name):
        image = pygame.image.load(self.MAP_PATH + name + ".png")
        self.mapElements[name] = image
    
    def updateObj(self,infoList):
        for info in infoList:
            name = info["name"] 
            if name in self.objDict:
                obj = self.objDict[name] 
                obj[pos] = info['pos']
                obj[pic] = self.mapElements[name]
            else:
                print("init Image",name)
                print("pos",info['pos'])
                self.objDict[name] = ImageObject(info['pos'],self.mapElements[name])

    def show(self):
        for obj,value in self.objDict.items():
            value.blit(self.gameScreen)


v = View()
v.initView()
test = [
        {"name": "c0",
         "pos": (100,100)
    },
        {"name": "c1",
         "pos" : (200,200)
    }
]

test2 = [
        {"name": "c2",
         "pos": (300,300)
    },
        {"name": "c3",
         "pos" : (400,400)
    }
]

v.updateObj(test)
v.show()
pygame.display.update()


