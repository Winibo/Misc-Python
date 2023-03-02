import math

circleOneCenter = 0
circlesDistance = float(input("Input distance from point A to B in Kilometers:"))
circlesAngle = float(input("input the angle from point A to B in degrees(0 degrees = true north, heading clockwise):")) - 90
if circlesAngle < 0:
    circlesAngle += 360
circleOneRadius = float(input("Input radius of circle from point A in kilometers:"))
circleTwoRadius = float(input("Input radius of circle from point B in kilometers:"))
circleTwoCenterY = circlesDistance * -math.sin(circlesAngle * math.pi/180)
circleTwoCenterX = circlesDistance * math.cos(circlesAngle * math.pi/180)
# X^2 + Y^2 = r^2 for circle one, convert to Y^2 = r^2 - X^2
# and y = +sqrt(r^2 - x^2)
# and y = -sqrt(r^2 - x^2)
#So when we substitute this in for y^2 and y in circle 2's equation we get
# X^2 - X^2 + r^2 + a*x + b*sqrt(r^2 - x^2) + (a^2 + b^2 - r2^2) = 0
# X^2 - X^2 + r^2 + a*x - b*sqrt(r^2 - x^2) + (a^2 + b^2 - r2^2) = 0
# which simplifies to:
# r^2 + a*x + b*sqrt(r^2 - x^2) + C = 0
# r^2 + a*x - b*sqrt(r^2 - x^2) + C = 0
#solving for x gives:
# a*x + b*sqrt(r^2 - x^2) = -C - r^2
# a*x - b*sqrt(r^2 - x^2) = -C - r^2
# ax^2 - b^2 * (r^2-x^2) = -C^2 - r^2
# ax^2 - br^2 + bx^2 = -C^2 - r^4
# ax^2 + br^2 - bx^2 = -C^2 - r^4
# (ax^2-bx^2) + br^2 + C^2 + r^4

# (ax^2+bx^2) - br^2 + C^2 + r^4 = 0
# and
# (ax^2-bx^2) + br^2 + C^2 + r^4 = 0
# Which can be solved for the x coordinate
# Then solve for Y in either of the 2 equations (for both values of x)
# Y^2 = r^2 - X^2

xSolveAPlus = circleTwoCenterX + circleTwoCenterY
xSolveAMinus = circleTwoCenterX - circleTwoCenterY
xsolveConstantPlus = -(circleTwoCenterY * circleOneRadius) + circleOneRadius**4 + (circleTwoCenterX**2 + circleTwoCenterY**2 - circleTwoRadius**2)
xsolveConstantMinus = (circleTwoCenterY * circleOneRadius) + circleOneRadius**4 + (circleTwoCenterX**2 + circleTwoCenterY**2 - circleTwoRadius**2)
# cx^2 + d = 0
# cx^2 = -d
# cx^2 - d = 0
# cx^2 = d
try:
    x1 = math.sqrt(-xsolveConstantPlus) / math.sqrt(xSolveAPlus)
except:
    x1 = "Invalid"
try:
    x2 = math.sqrt(xsolveConstantMinus) / math.sqrt(xSolveAMinus)
except:
    x2 = "Invalid"
try:
    y1 = math.sqrt(circleOneRadius**2 - x1**2)
except:
    y1 = "Invalid"
try:
    y2 = math.sqrt(circleOneRadius**2 - x2**2)
except:
    y2 = "Invalid"

try:
    angle1 = math.asin((y1/x1) % 1)
except(TypeError):
    angle1 = "Invalid"
except:
    angle1 = "Fuck"
try:
    angle2 = math.asin((y2/x2) % 1)
except(TypeError):
    angle2 = "Invalid"
except:
    angle2 = "Fuck"
try:
    angle1 = ((angle1 * 180) / math.pi) + 270
except:
    pass
try:
    angle2 = ((angle2 * 180) / math.pi) + 270
except:
    pass
try:
    if angle1 > 360:
        angle1 = angle1 - 360
except:
    pass
try:
    if angle2 > 360:
        angle2 = angle2 - 360
except:
    pass
print("The angle from point A to your location is: ")
print(angle1 - 28)
print(" degrees, or ")
print(angle2 - 28)
print(" degrees from point A")
