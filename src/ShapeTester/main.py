from Box import Box

# get three values from the user
tempL = input("Enter length:")
tempW = input("Enter width:")
tempH = input("Enter height:")

# instantiate the box
b1 = Box(tempL,tempW,tempH)
print(b1.calcVol())