import View.View as view
import pygame
import time as t
import Controll as c
pygame.init()
pygame.display.init()
pygame.font.init()
controller = c.Controll()
controller.run()

test2 = {
    "ice": { "type": "image",
             "pos": (0,0) },
    
    "c2": { "type": "image",
            "pos" : (300,300)},
    
    "c3": { "type": "image",
            "pos": (400,400),
            "clickable": True
    }
}

#controller.view.updateObj(view.readJson("choseItem.json"))
#clickedObj = controller.view.userInput()
