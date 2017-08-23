'''
	OOP - Object oriented programming
	AUFA
	05/30/2017
'''
'''
class Cat:
	def __init__(self,color,legs):
		self.color = color
		self.legs = legs
	def bark(self):
		print ("Woof!")

felix = Cat("ginger",4)
print (felix.color)
felix.bark()

class Rectangle:
	def __init__(self,width,height):
		self.width = width
		self.height = height
		self.area = width * height

rect = Rectangle(7,8)
print (rect.area)

class Dog(Cat):
	def bokbok(self):
		print ("Broooo!!!")
	def tiktik(self):
		print ("DOG")

robert = Dog("red",6)
print (robert.color)
robert.bokbok()
robert.bark()

class Beer(Dog):
	def bra(self):
		print ("Braaaa!!!")
		super().bokbok()
		super().bark()
	def tiktik(self):
		print ("BEER")
beer = Beer("brown",2)
beer.bra()
beer.tiktik()

'''
'''
class Vector2D:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __add__(self, other): #__add__ : +
		return Vector2D(self.x+other.x,self.y+other.y)
first = Vector2D(5,8)
second = Vector2D(3,9)
result = first + second
print(result.x)
print(result.y)
'''

class SpecialString:
	def __init__(self,cont):
		self.cont = cont
	def __truediv__(self,other):
		line = "=" * len(other.cont)
		return "\n".join([self.cont,line,other.cont])
spam = SpecialString("spam")
hello = SpecialString("Good morning")
print(spam/hello)


