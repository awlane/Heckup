import random
import csv
import webbrowser
def threeCoins():
    hexagram = []
    for x in range(0, 6):
        coinA = random.randint(2, 3)
        coinB = random.randint(2, 3)
        coinC = random.randint(2, 3)
        line = coinA + coinB + coinC
        if line == 6:
            print("Line " + str(x + 1) + ": Old yin")
            hexagram.append(0)
        if line == 7:
            print("Line " + str(x + 1) + ": Young yang")
            hexagram.append(1)
        if line == 8:
            print("Line " + str(x + 1) + ": Young yin")
            hexagram.append(0)
        if line == 9:
            print("Line " + str(x + 1) + ": Old yang")
            hexagram.append(1)
    return str.join("", (str(x) for x in hexagram))

ichingfile = open("ichingdict.csv", "r", encoding="UTF-8")
csvreader = csv.reader(ichingfile, delimiter=",")
ichingDict = {}
for line in csvreader:
    ichingDict[line[0]] = (line[1], line[2], line[3])
divination = threeCoins()
drawnHexagram = ichingDict[divination]
hexagramURL = "http://ctext.org/book-of-changes/" + drawnHexagram[0]
hexagramName = drawnHexagram[0].replace("1", "").replace("-"," ").capitalize()
if " " in hexagramName:
    temp = hexagramName.split(" ")
    temp[1] = temp[1].capitalize()
    hexagramName = str.join(" ", temp)
print("Hexagram " + drawnHexagram[1] + ": " + drawnHexagram[2] + " " + hexagramName)
webBool = input("Would you like to open the relevant information in a webpage? (y/n) ")
if webBool == "y":
    webbrowser.open(hexagramURL, new=1, autoraise=True)
    print("May fortune favor you.")
elif webBool == "n":
    print("May fortune favor you.")
else:
    print("Invalid input. Exiting. May fortune favor you.")