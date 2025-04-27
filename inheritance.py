class Mammal:
    def walk(self):
        print('walk')
        
class Dog(Mammal):
        pass
    

class Cat(Mammal):
    def meow(self):
        print('meow')
        

cat1 = Cat()
cat1.meow()

    