import pygame
import os
import View.viewConst as viewConst
import mapConst as mapConst
import const as const 
import time as t
import json as j
import math
class CharObject():
    def __init__(self):
        self.hunger = 60
        self.thirst = 60
        self.spiritValue = 80
        self.points = 10
        self.day = 1
        self.temperature = -12
        self.pressure = 1000

    def renderStatus(self):
        hungerValue = TextObject(viewConst.CHAR_RENDER_POS[self.hunger]
                                 ,self.hunger)
        hungerValue = TextObject(viewConst.CHAR_RENDER_POS[self.hunger]
                                 ,self.hunger)
        hungerValue = TextObject(viewConst.CHAR_RENDER_POS[self.hunger]
                                 ,self.hunger)
        hungerValue = TextObject(viewConst.CHAR_RENDER_POS[self.hunger]
                                 ,self.hunger)
        hungerValue = TextObject(viewConst.CHAR_RENDER_POS[self.hunger]
                                 ,self.hunger)
        hungerValue = TextObject(viewConst.CHAR_RENDER_POS[self.hunger]
                                 ,self.hunger)
class AnimateObject():
    def __init__(self,image_list,time):
        self.imageList = image_list
        self.timeInterval = time
        self.fadeSpeed = 24

    def play(self,view):
        for imageName in self.imageList:
            if(imageName[:1] == "A"):
                view.ViewElements[imageName[1:]].setAttr((0,0))
                fade = FadeObject(start = 0,speed=-self.fadeSpeed)
                view.show()
                pygame.event.get()
                pygame.time.wait(self.timeInterval)
                fade.fade(view)

            elif(imageName[:1] == "B"):
                view.ViewElements[imageName[1:]].setAttr((0,0))
                fade = FadeObject(start = 255,speed=self.fadeSpeed)
                fade.fade(view)

            else:
                view.ViewElements[imageName].setAttr((0,0))
                view.show()
                pygame.event.get()
                pygame.time.wait(self.timeInterval)
            view.resetViewElements()

class FadeObject():
    def __init__(self,speed=4,pos=(0,0),color=(0,0,0),size=viewConst.WINDOW_SIZE,start=255):
        self.speed = speed
        self.pos = pos
        self.color = color
        self.size = size
        self.clock = pygame.time.Clock()
        self.start = start

    def fade(self,view):
        alphaSurface = pygame.Surface(self.size) 
        view.gameScreen.fill(self.color) 
        for i in range(int(255/math.fabs(self.speed))):
            view.show()
            alphaSurface.set_alpha(self.start - i * self.speed)
            view.gameScreen.blit(alphaSurface,self.pos)
            #self.clock.tick()
            pygame.display.flip()
            events = pygame.event.get()
        


class TextObject():
    def __init__(self,rect,text,font = viewConst.DEFAULT_FONT):
        self.rect = rect,
        self.text = text,
        self.font = pygame.font.SysFont(font, 24)
        self.color = viewConst.DEFAULT_COLOR

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
    def __init__(self,name,pic,effPic=None,click=0):
        self.name = name
        self.picture = pic
        self.effectPic = effPic
        self.picSize = pic.get_rect()
        self.rect = pygame.Rect(viewConst.OUT,viewConst.OUT,self.picSize[2],self.picSize[3])
        self.clickable = click
        self.effect = False
        self.type = None
    
    def blit_by_rect(self,screen,rect):
        screen.blit(self.picture,rect)

    def blit(self,screen):
        if not self.effect or self.effectPic is None:
            screen.blit(self.picture,self.rect)
        else:
            screen.blit(self.effectPic,self.rect)

    def detectCollision(self,x,y,level):
        ### if clickable, check if clicked else return false
        if self.clickable >= level:
            return self.rect.collidepoint(x,y)
        else:
            return False

    def setAttr(self,pos,clickable=None,rectSize=None):
        self.rect[0] = pos[0]; self.rect[1] = pos[1]
        if clickable is not None:
            self.clickable = clickable 
        if rectSize is not None:
            self.rect[2] = rectSize[0]; self.rect[3] = rectSize[1]

class View:
    def __init__(self):
        self.ViewElements = {}
        #self.objDict = {}
        self.gameScreen = pygame.display.set_mode(viewConst.WINDOW_SIZE)
        self.mapStat = mapConst.startMap
        self.pageStat = const.OPEN_PAGE
        self.clickLevel = 1

    ### Loads all used png from dir elementsPath,
    ### Store them as pygame Image object in dictionary mapElements.
    ### Init pygame (For selftest)
    def initView(self):
        pygame.init()
        pygame.display.init()
        pygame.font.init()
        print("initializing View Image...")
        for path in [viewConst.ITEM_FULL_SCREEN,viewConst.ITEM_PNG_PATH,
                     viewConst.SHOWDETAIL_PNG_PATH,viewConst.ANIMATION_PATH,
                     viewConst.MOVE_PNG_PATH,viewConst.ACTION_PNG_PATH,
                     viewConst.WINDOW_CONTROLL_PNG_PATH,viewConst.CHOOSE_PNG_PATH]:
            elementsPath = os.listdir(path)
            elementsName = map(lambda x:x.replace(".png",""),elementsPath)
            for name in elementsName:
                self.loadImage(name,path=path)
                print(name, "Loaded")

        start = self.readJson("start.json")
        self.updateObj(start)
    
    ### Loads the png to dictionary
    def loadImage(self,name,path):
        image = pygame.image.load(path + name + ".png")
        if (path == viewConst.ANIMATION_PATH or path == viewConst.ITEM_FULL_SCREEN):
            image = pygame.transform.scale(image, viewConst.WINDOW_SIZE)
        try:
            effImage = pygame.image.load(path + name + "_eff.png")
            #rect = image.get_rect()
            #print(rect)
            #effImage = pygame.transform.scale(image, (rect[2]*1.5,rect[3]*1.5))
            #print("eff",effImage.get_rect())
        except:
            effImage = None
        self.ViewElements[name] = ImageObject(name,image,effImage)
        self.ViewElements[name].type = {
            viewConst.ITEM_PNG_PATH : "item",
            viewConst.MOVE_PNG_PATH : "move",
            viewConst.ACTION_PNG_PATH : "action",
            viewConst.SHOWDETAIL_PNG_PATH : "showDetail",
            viewConst.WINDOW_CONTROLL_PNG_PATH : "windowControll",
            viewConst.CHOOSE_PNG_PATH : "choose"
        }.get(path,None)
    
    def adjustObj(self,name,pos):
        self.ViewElements[name].setAttr(pos)
    ### Create ImageObj if doesn't exist in ObjDict, else update it.
    ### Default type is image

    def updateObj(self,infoList,adjust=False):
        fade = None
        if(not adjust):
            self.resetViewElements()
        for name,info in infoList.items():
            if (info['type'] == "image"):
                self.ViewElements[name].setAttr(info['pos'],info.get('clickable'))
            elif(info['type'] == "fade"):
                fade = FadeObject(info.get('speed'))
            elif(info['type'] == "animation"):
                AnimateObj = AnimateObject(info['image_list'],info['timeInterval'])
                AnimateObj.play(self)
                self.resetViewElements()
        
        if (fade is not None):
            fade.fade(view=self)
        else:
            self.show()

    def update(self,d):
        print(d)

        if(self.mapStat == mapConst.explainMap):
            if(d.get('start')):
                self.mapStat = mapConst.stationMap['ID']
                self.updateObj(self.readJson('station.json'))

        if(self.mapStat == mapConst.chooseMap):
            if (d.get('action') == "showDetail"):
                self.updateObj(self.readJson('showItemDetail.json')[str(d['name'])],adjust=True)
                self.clickLevel = 2
            
            if(d.get('action') == "choose"):
                self.updateObj(self.readJson('choseItem' + str(d['counter']) + '.json'))
                print(d['name'])
                for name in d['name']:
                    self.ViewElements[name].clickable = 0
                self.clickLevel = 1

            if(d.get('start')):
                self.mapStat = mapConst.explainMap
                self.updateObj(self.readJson("explaination.json"))

        if(self.mapStat == mapConst.startMap):
            if(d.get('start')):
                self.updateObj(self.readJson('choseItem.json'))
                self.mapStat = mapConst.chooseMap
        
        
    ### Blit the ImageObj in objDict, clears the screen using the background
    def show(self):
        for name,obj in self.ViewElements.items():
            obj.blit(self.gameScreen)
        pygame.display.flip()


    def checkClickObj(self,x,y):
        for name,obj in self.ViewElements.items():
            if(obj.detectCollision(x,y,self.clickLevel)):
                return obj
        return None

    ### reset the position to const.OUT before loading new frame
    def resetViewElements(self):
        for _, obj in self.ViewElements.items():
            obj.setAttr((viewConst.OUT,viewConst.OUT),False,(obj.picSize[2],obj.picSize[3])) 

    def readJson(self,path):
        jsonFile = open(viewConst.JSON_PATH + path)
        jsonStr = jsonFile.read()
        return j.loads(jsonStr)
        
    ### Wait for user input, if clicked on clickable obj, return it
    def userInput(self):
        effFlag = False
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    clickedObj = self.checkClickObj(x,y)
                    if clickedObj is not None:
                        return self.clickInfo(clickedObj)
                ### changes the pic when mouse on obj
                ### Implemented poorly due to limited time
                """
                if event.type == pygame.MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    clickedObj = self.checkClickObj(x,y)
                    if clickedObj is not None:
                        clickedObj.effect = True
                        clickedObj.blit(self.gameScreen)
                        pygame.display.update()
                        clickedObj.effect = False
                        effFlag = True
                    elif(effFlag):
                        self.show()
                        effFlag = False
                """
                

    def clickInfo(self,clickedObj):
        if clickedObj.type == 'item' or clickedObj.type == 'action':
            return {
                    "map" : self.mapStat,
                    "page" : self.pageStat,
                    "name" : clickedObj.name,
                    "type" : clickedObj.type
            }
        elif clickedObj.type == 'choose':
            return {
                    "map" : self.mapStat,
                    "page" : self.pageStat,
                    "name" : clickedObj.name,
                    "type" : clickedObj.type,
                    "result" : "yes" if clickedObj.name == "pick" else "no"
            }
                    

                        
                    



