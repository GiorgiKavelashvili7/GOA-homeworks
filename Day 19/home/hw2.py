# მაქსიმალური ელემენტის პოვნა სიაში
# დავალება: მომხმარებლის მიერ შეყვანილი რიცხვების სიაში იპოვეთ უდიდესი რიცხვი, გარდა ჩაშენებული ფუნქციისა (e.g. max).

numbers = list(map(int, input("შეიყვანეთ რიცხვები მძიმით გამოყოფილი").split(',')))
if len(numbers) == 0:
    print("სია ცარიელია")
else:
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    print(f"უდიდესი რიცხვი არის {max_number}")