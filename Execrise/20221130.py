class Animal():
    def __init__(self,name) -> None:
        self.name=name
    def sound():
        pass

class Dog(Animal): #載入要繼承的類別
    def __init__(self,name,foot) -> None:
        super().__init__("小狗狗"+name) #取得
        self.foot=foot
    def sound(self):
        return "BARK"
        
A=Animal("DOG")
D=Dog("Doggy",4)
print(A.name)
print(D.name)
print(D.foot)
print(D.sound())

A="12341"
print(sorted(A))