import numpy as np


class temp_press:

    def __init__(self):
        self.temp = np.load("src/pre_temp.npy")
        self.press = np.load("src/pre_press.npy")
        self.cold = 0
        self.cold_count = 11
        self.cold_bool = True
        self.time = 0 ### ask 
    
    def set_basic(self, time, longtitude, altitude): ###Called When time change, time is float 0~365
        self.time = time                             
        self.basic_temp = self.predict_temp(longtitude, altitude)
        self.basic_press = self.predict_press(longtitude, altitude)

    def upgrade(self, longtitude, altitude):     ### Called when move character
        temp = self.predict_temp(longtitude, altitude)
        press = self.predict_press(longtitude, altitude)
        Frostbite = False

        
        if self.cold_bool == False :
            if temp<self.basic_temp-abs(self.basic_temp)*0.02 :
                Frostbite = True
                self.cold_bool = True
                self.cold_count = 0
        else :
            self.cold_count+=1
            if self.cold_count >= 13:
                self.cold_bool = False
                self.cold_count = 0
        return {"temperature": temp, "pressure": press, "Frostbite" : Frostbite}


    def predict_temp(self, longtitude, latitude) : 
        x = [[self.time, longtitude, latitude]]
        O1 = np.maximum(np.matmul(x,self.temp[0])+self.temp[1], 0)
        O2 = np.maximum(np.matmul(O1,self.temp[2])+self.temp[3], 0)
        O3 = np.maximum(np.matmul(O2,self.temp[4])+self.temp[5], 0)
        pred = np.matmul(O3,self.temp[6])+self.temp[7]
        if pred==955 :
            pred = pred + np.random.normal(50, 25, 1)
        elif pred==1015 :
            pred = pred + np.random.normal(-40, 25, 1)
        return pred

    def predict_press(self, longtitude, latitude) :
        x = [[self.time, longtitude, latitude]]
        O1 = np.maximum(np.matmul(x,self.press[0])+self.press[1], 0)
        O2 = np.maximum(np.matmul(O1,self.press[2])+self.press[3], 0)
        O3 = np.maximum(np.matmul(O2,self.press[4])+self.press[5], 0)
        pred = np.matmul(O3,self.press[6])+self.press[7]
        if pred==-24 :
            pred = pred + np.random.normal(10, 10, 1)
        elif pred==18 :
            pred = pred + np.random.normal(-10, 8, 1)
        return pred

"""
x = temp_press()
a = np.random.normal(170,100,1)
x.set_basic(a,140,-65)
randb = np.random.normal(-0.05, 0.2 , 100)
randc = np.random.normal(-0.05, 0.2 , 100)
b = 140.3
c = -64.3
for i in range(20):
    b+=randb[i]
    c+=randc[i]
    print(x.upgrade(b,c))
"""