import View as view
import pygame
import time as t
v = view.View()
v.initView()
test = {
    "ice": { "type": "image",
             "pos": (0,0) },

    "c0": { "type": "image",
            "pos": (100,100),
            "clickable": True
    },

    "c1": { "type": "image", 
            "pos" : (200,200)},

    "text1": { "type": "text",
               "contend": "I was in the passenger seat of my mom’s lime-green Opel Manta on the way home from work. It was summer between my junior and senior year in high school. Mom had found me a job in the mailroom of her employer, Southwestern School of Law. She managed the secretarial pool, and we carpooled together between downtown LA and our home in Westwood. ",
               "rect": (200,200,200,500)
    }       
}

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

v.updateObj(test)
v.show()
pygame.display.flip()
clickedObj = v.input()
v.clearObjDict()
print("CLICKEDDD")
print(clickedObj.name)
#v.gameScreen.fill((0,0,0))
v.updateObj(test2)
v.show()
pygame.display.flip()
clickedObj = v.input()