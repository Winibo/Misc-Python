import math
coneHeight = 1.4914
coneAngle = 61.692 * math.pi/180
coneLateral = coneHeight / math.cos(coneAngle)
coneRadius = math.sqrt(coneLateral**2 - coneHeight**2)
coneVolume = (math.pi * coneRadius**2 * (coneHeight / 3))
b = math.sqrt(coneRadius**2 + coneHeight**2) / coneRadius
sphereRadius = (coneHeight * b)/ (b**2 + b - 2)
print("Cone Volume")
print(coneVolume)
print("Cone Radius")
print(coneHeight*math.tan(coneAngle))
print(coneRadius)
print("Sphere Radius")
print(sphereRadius)
sphereInWaterHeight = sphereRadius*(1-b) + coneHeight
sphereInWaterVolume = math.pi*sphereInWaterHeight**2 * (sphereRadius - (sphereInWaterHeight/3))
print("Displacement")
print(sphereInWaterVolume)
print("Optimal - Current")
print(10.403034252792255 - sphereInWaterVolume)
print("greatest r:")
print(coneHeight * b / (b**2-1))
print("smallest r:")
print(coneHeight/(1+b))
print("Cone Volume - sphereInWaterVolume")
print(coneVolume - sphereInWaterVolume)
# W 114 39.769 (5) N 51 10.403
# W 114 10.403 N 51 39.769
# N 51 039.77 W 114 10.403
# W 114 + Sphere Radius, N 51 + Displacement
