def getmarginal(income):
    brackets = open(r"C:\Users\14038\Desktop\Tax Brackets.txt", "r+")
    read = brackets.readlines()
    linestorage = []
    realtaxes = [0, 0]
    for i in range(len(read)):
        linestorage.append(read[i].split(" "))
    for i in range(len(linestorage)):
        numbstorage = (linestorage[i][1])
        numbstorage = numbstorage[:-1]
        realtaxes.append(linestorage[i][0])
        realtaxes.append(numbstorage)
    totaltax = 0
    for i in range(2, len(realtaxes), 2):
        try:
            if float(income) > float(realtaxes[i]):
                income = float(income) - (float(realtaxes[i]) - float(realtaxes[i-2]))
                totaltax = totaltax + ((float(realtaxes[i]) - float(realtaxes[i-2])) * float(realtaxes[i+1]))
            else:
                totaltax = totaltax + (float(income) * float(realtaxes[i+1]))
                break
        except ValueError:
            totaltax = totaltax + (float(income) * float(realtaxes[i+1]))
    return int(totaltax)