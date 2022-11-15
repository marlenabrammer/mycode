class Cat:
	def __init__(self, name):
	    self.name = name

    def speak(self): 
        return 'meow'

mycat=Cat("Misty")
print(mycat)
print(type(mycat))
print(dir(mycat))
print(mycat.speak())

