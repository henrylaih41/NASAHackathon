###
WINDOW_SIZE = (1080,720)
ITEM_PNG_PATH = "data/png/items/"
MOVE_PNG_PATH = 'data/png/move/'
ACTION_PNG_PATH = 'data/png/action/'
SHOWDETAIL_PNG_PATH = 'data/png/showDetail/'
WINDOW_CONTROLL_PNG_PATH = 'data/png/windowControll/' 
ITEM_FULL_SCREEN = 'data/png/fullscreen/'
CHOOSE_PNG_PATH = 'data/png/choose/' 
JSON_PATH = "data/json/"
ANIMATION_PATH = "data/animation/"

DEFAULT_FONT = 'monospace'
DEFAULT_COLOR = (0,0,0)
OUT = -9999

CHAR_RENDER_POS = {
    'day' : [114,83,80,80],
    'hour' : [70,130,80,80],
    'hunger' : [812,228],
    'thirst' : [812,268],
    'points' : [812,353],
    'pressure' : [152,197,60,60],
    'temperature' : [172,178,60,60],
    'spiritValue' : [812,310]
}

MOVEMENT_LIST = [("K_UP",1,lambda x,y: x - y),("K_DOWN",1,lambda x,y: x + y)
                ,("K_LEFT",0,lambda x,y: x - y),("K_RIGHT",0,lambda x,y: x + y)]

