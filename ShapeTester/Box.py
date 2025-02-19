class Box:

   def __init__(self, l ,w, h):
      self.l = l
      self.w = w
      self.h = h
   
   def calcVol(self):
     vol = self.l * self.w * self.h
     return vol

   def calcSA(self):
      sa = 0
      return sa