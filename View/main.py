import View as view
import pygame
v = view.View()
v.initView()
test = [
        {"name": "c0",
         "pos": (100,100)
    },
        {"name": "c1",
         "pos" : (200,200)
    }
]
v.updateObj(test)
v.show()
pygame.display.update()
while(True):
    pass
