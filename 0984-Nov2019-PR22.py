# 0984/22 Pre Release
# Tom Walford

# Import Modules

import math

# Constants

global slabColours, basePrice, slabPercent, slabDepth, slabShape, squareSize, rectSize, roundSize, customSetupFee

slabColours = ['Grey','Red','Green','Custom']
unitPrice = 0.05
unitVolume = 100000
slabPercent = [0,10,10,15]
slabDepth = [38,45]
slabShape = ['Square','Rectangle','Round']
squareSize = [600,450]
rectSize = ['600x700','600x450']
roundDiameter = [300,450]
customSetupFee = 5

# Functions and Constants

# Lookup Check

def lookupCheck(prompt, list):

    valid = False

    while valid is False:

        print(prompt,": ",sep='',end='')
        temp = input()

        try:
            temp = int(temp)
        except:
            pass
        print(temp)
        if temp in list:
            valid = True
        else:
            print('Data not in list of valid inputs')

    return temp

# Main

# Task 1

colour = lookupCheck('Slab colour',slabColours)
depth = lookupCheck('Slab depth', slabDepth)
shape = lookupCheck('Slab shape', slabShape)

if shape == "Square":

    length = lookupCheck('Enter length of slab in mm',squareSize)
    surfaceArea = length ** 2

elif shape == "Rectangle":
    size = lookupCheck('Enter slab size (lengthxwidth) in mm',rectSize)
    temp = size.split('x')
    surfaceArea = int(temp[0]) * int(temp[1])

else:

    diameter = lookupCheck('Enter slab diameter in mm',roundDiameter)
    surfaceArea = math.pi * (diameter/2)**2

slabVolume = surfaceArea * depth

numberSlabsOrdered = 20 # Replace with input routine in Task 2

totalVolumeConcrete = slabVolume * numberSlabsOrdered

print("Colour Choice:", colour)
print("Slab depth:", depth)
print("Slab shape:", shape)
print("Slab surface area: ", surfaceArea)
print("Slab volume: mm3:", slabVolume)
print("Slabs ordered:", numberSlabsOrdered)
print("Slab total volume:", totalVolumeConcrete)

numUnits = totalVolumeConcrete // unitVolume
remainder = totalVolumeConcrete % unitVolume

if remainder > 0:

    numUnits = numUnits + 1

price = numUnits * unitPrice
colourIndex = slabColours.index(colour)
multiplier = slabPercent[colourIndex]

price = price * ((100+multiplier)/100)
customFee = 0

print("Basic price: $",price)
if colour == "Custom":

    colour = input('Enter custom colour: ')
    customFee = customSetupFee

price = price + customFee
    
print("Price multiplier: ", multiplier,"%")
print("Final colour: ", colour)
print("Setup fee if custom: $", customFee)
print("Final price: $", price)
