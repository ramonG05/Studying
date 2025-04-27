class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"hi, i am", self.name)
        

Ramon = Person('Ramon')
Ramon.talk()

