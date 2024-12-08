# დავალება: სიიდან რიცხვების ჯამი
# შექმენით პროგრამა, რომელიც:
# მომხმარებელს სთხოვს რიცხვების შეყვანას ერთ ხაზზე, მძიმით გამოყოფილი ფორმატით (მაგალითად: 1, 2, 3, 4).
# მიიღებს ამ რიცხვებს, შექმნის სიას numbers.
# გაანგარიშებს და დაბეჭდავს სიის რიცხვების ჯამს.

HI = int(input("Please input numbers: "))
HI2 = int(input("Please input numbers: "))
HI3 = int(input("Please input numbers: "))
HI4 = int(input("Please input numbers: "))

HELLO = []

HELLO.append(HI)
HELLO.append(HI2)
HELLO.append(HI3)
HELLO.append(HI4)

print(sum(HELLO))