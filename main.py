class empolye:
   def __init__(self , n ,d):
      self.name = n
      self.designation = d


    def __del__(self):
      print("the object")

obj = empolye("talha", "work")