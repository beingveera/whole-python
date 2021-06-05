import string
class stack:
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def pop(self):
		self.items.pop(0)
	def show(self):
		return self.items
	def peek(self):
		if self != None:
			return self.items[-1]
s=stack()
s.push("A")
print(s.show())
s.push("B")
s.pop()
s.push("C")
print(s.show())
print(s.peek())


		