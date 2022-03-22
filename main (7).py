#Nested class 

class Army():
  def __init__(self):
    self.name = 'Lucky'
    self.g = self.Gun()#inner class object
  def show(self):
    print("name:",self.name)

  class Gun:
    def __init__(self):
      self.name = 'AK-47'
      self.capacity = '75 Rounds'
      self.length = '100 cm'
    def disp(self):
      print("name :",self.name)
      print("capacity:",self.capacity)
      print("length :",self.length)

a = Army()
a.show()
g = Army().Gun()#object of nested class
g.disp()
print(a.g.name)#Accecing member 
