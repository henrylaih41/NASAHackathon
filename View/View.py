import pygame
import os
import const
import time as t
class TextObject():
    def __init__(self,rect,text,font = const.DEFAULT_FONT):
        self.rect = rect,
        self.text = text,
        self.font = pygame.font.SysFont(font, 24)
        self.font.set_italic(True)
        self.color = const.DEFAULT_COLOR

    def blit(self,screen):
        self.textBlit(screen,self.text[0],self.color
                      ,self.rect,self.font)
    
    def detectCollision(self,x,y):
            return False

    def textBlit(self,surface, text, color, rect, font, aa=True):
        rect = pygame.Rect(rect)
        y = rect.top
        lineSpacing = -2

        # get the height of the font
        fontHeight = font.get_height()
        print("fontHeight is ", fontHeight)
        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + fontHeight > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word      
            if i < len(text): 
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            image = font.render(text[:i], aa, color)

            surface.blit(image, (rect.left, y))
            y += fontHeight + lineSpacing

            # remove the text we just blitted
            text = text[i:]

        return text

class ImageObject():
    def __init__(self,name,pos,pic,click=False):
        self.name = name
        self.pos = pos 
        self.picture = pic
        self.picSize = pic.get_rect()
        self.rect = pygame.Rect(pos[0],pos[1],self.picSize[2],self.picSize[3])
        self.clickable = click
        print("rect is ",self.rect)

    def blit(self,screen):
        screen.blit(self.picture,self.rect)

    def detectCollision(self,x,y):
        ### if clickable, check if clicked else return false
        if self.clickable:
            return self.rect.collidepoint(x,y)
        else:
            return False

class View:
    def __init__(self):
        self.mapElements = {}
        self.MAP_PATH = const.MAP_PATH
        self.objDict = {}
        self.gameScreen = pygame.display.set_mode(const.WINDOW_SIZE)
    
    ### Loads all used png from dir elementsPath,
    ### Store them as pygame Image object in dictionary mapElements.
    ### Init pygame (For selftest)
    def initView(self):
        print("init View...")
        elementsPath = os.listdir(self.MAP_PATH)
        elementsName = map(lambda x:x.replace(".png",""),elementsPath)
        for name in elementsName:
            self.loadImage(name)
            print(name, "Loaded")
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        # To Menu
    
    ### Loads the png to dictionary
    def loadImage(self,name):
        image = pygame.image.load(self.MAP_PATH + name + ".png")
        self.mapElements[name] = image

    ### Create ImageObj if doesn't exist in ObjDict, else update it.
    ### Default type is image
    def updateObj(self,infoList):
        for name,info in infoList.items():
            if( info['type'] == "image"):
                self.objDict[name] = ImageObject(name,info['pos'],self.mapElements[name],
                                                 info.get("clickable"))
            else:
                self.objDict[name] = TextObject(info['rect'],info['contend'],info.get('font'))
            

    ### Blit the ImageObj in objDict
    def show(self):
        for name,obj in self.objDict.items():
            obj.blit(self.gameScreen)

    def checkClickObj(self,x,y):
        for name,obj in self.objDict.items():
            if(obj.detectCollision(x,y)):
                return obj
        return None

    def clearObjDict(self):
        self.objDict.clear()

    ### Wait for user input, if clicked on clickable obj, return it
    def input(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    print("Button up")
                    x, y = pygame.mouse.get_pos()
                    print(x,y)
                    clickedObj = self.checkClickObj(x,y)
                    if clickedObj is not None:
                        return clickedObj

                        
                    



