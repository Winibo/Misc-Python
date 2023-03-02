seconds = 10000

hours = int(seconds/3600)
seconds = seconds % 3600
minutes = int(seconds/60)
seconds = seconds % 60

print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
