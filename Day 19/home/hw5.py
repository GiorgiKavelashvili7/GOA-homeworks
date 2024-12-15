# ელემენტის ძებნა სიაში
# დავალება: დაწერეთ პროგრამა, რომელიც გადაამოწმებს, არის თუ არა მოცემული რიცხვი მომხმარებლის მიერ შექმნილ სიაში.


list1 = input("Please input some numbers: ").split()
list2= input("Please enter a number: ")
if list2 in list1:
    print("The number entered by you is in the list!")
else:
    print("The number entered by you is not in the list!")     
