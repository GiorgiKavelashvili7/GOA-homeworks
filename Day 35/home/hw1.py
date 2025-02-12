"""
გაიმეორეთ PY - ს ყველა საკითხი და გააკეთეთ 3 მაგალითი თითო საკითხზე.
"""

# კონკატინაცია:
print("Hello" + "World")
print("Goal-oriented" + "Academy")
print("Face" + "Book")

# დამატება:
print(10 + 10)
print(20 + 45)
print(1098 + 76)

# გამოკლება:
print(10 - 10)
print(20 - 45)
print(1098 - 76)

# გამრავლება:
print(10 * 10)
print(20 * 45)
print(1098 * 76)

# გაყოფა: 
print(10 / 10)
print(20 / 45)
print(1098 / 76)
print(10 // 10)
print(20 // 45)
print(1098 // 76)

# ინპუტები:
messege_1 = str(input("Input a string: "))
messege_2 = int(input("Input an integer: "))
messege_3 = float(input("Input a float: "))

# პირობითი განცხადებები:
num = 1
if num == 1:
    print("num is one")
elif num == 0:
    print("num isnt one")
else:
    print("I dont know")

# ლოგიკური განცხადებები:
string = "text"
integer = "number"
if string and integer == "HIYA":
    print("BOMBASTIC SIDE EYEEEE")
if string or integer == "HUYA":
    print("FANTASTIC SIDE EYE")
if not string:
    print("KUNG FU PANDAAAA")

# ფუნქციები:
def BOMBASTIC(one, two):
    return "BOMBASTIC"
BOMBASTIC(1, 2)
def FANTASTIC (three, four):
    PHRASE = "???"
    return PHRASE
FANTASTIC(3, 4)
def INTER_DIMENSIONAL_TRAVELER(TH3, onE):
    TRAVEL = "100 COINS"
    TRAVEL = "1 LIFE"
    return TRAVEL
INTER_DIMENSIONAL_TRAVELER(9, 9)

# სიები:
LIST = ["hello", 1, True, 3.3]
LIST.append("HI")
LIST.remove("hello")
LIST.reverse()
LIST.insert(0, "Hello")
print(len(LIST))
print(LIST.count("hello"))

