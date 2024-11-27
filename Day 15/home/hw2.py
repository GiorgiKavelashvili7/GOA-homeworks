# დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია

Mystery_number = int(input("Please type a number: "))
if Mystery_number >= 1:
    print("The number you inputed is a positive number!")
elif Mystery_number <= -1:
    print("The number you inputed is a negative number!")
elif Mystery_number == 0:
    print("The number you inputed is just a zero!")        