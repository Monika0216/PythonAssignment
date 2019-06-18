class student():
    def register(self,regno,name,standard,section):
        self.regno=regno
        self.name=name
        self.standard=standard
        self.section=section
        
    def information(self):
        print('regno',self.regno,'name',self.name,'standard',self.standard,'section',self.section)

bhavikaa=student()
bhavikaa.register=(82,'Bhavikka','9','B')
bhavikaa.information()


shloka=student()
shloka.register=(104,'shloka','8','A')
shloka.information()

#claculator
class calculator():
    def assig(self,res,a,b):
        self.res=res
        self.a=a
        self.b=b
    def add(self):
        self.res=self.a+self.b
        return self.res
    def sub(self):
        self.res=self.a-self.b
        return self.res
    def mul(self):
        self.res=self.a*self.b
        return self.res
    def div(self):
        self.res=self.a/self.b
        return self.res

first=calculator()
first.assig(0,20,10)
first.add()

#claculator
class calculator():
    def add(self,a,b):
        return (a+b)
    def sub(self,a,b):
        return (a-b)
    def mul(self,a,b):
        return (a*b)
    def div(self,a,b):
        return (a/b)

first=calculator()

print(first.add(20,10))
print(first.sub(30,40))
print(first.mul(30,60))
print(first.div(20,30))

#constructor for car
class car():
    def __init__(self,make,model,color,price):
        print("Car")
        self.make=make
        self.model=model
        self.color=color
        self.price=price
        self.speed=0
    
    def info(self):
        print("Make",self.make,"Model",self.model,"Color",self.color,"price",self.price)
    
    def start(self):
        self.speed=0
        return self.speed
        #print("Speed when started",self.speed)
     
    def move(self):
        self.speed=self.speed+5
        return self.speed
    
    def stop(self):
        self.speed=0
        #print("Speed when stopped",self.speed)
        return self.speed

mycar=car("shift","Dizire","Black",120000)
mycar.info()
print("car in start",mycar.start())
print("car in move",mycar.move())
print("car when stop",mycar.stop())

#creating the main function
print(__name__)
def main1():
    print('Hello world')
    otherfunction()

def otherfunction():
    print('This is annother function')

if(__name__=='__main__'):
    main1()




























