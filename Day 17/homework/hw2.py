# დავალება: რიცხვების ნაყარი შეკრებვა
# შექმენით პროგრამა, რომელიც:
# მომხმარებელს სთხოვს ერთი რიცხვის შეყვანას.
# შემდეგ პროგრამა ითხოვს სხვა რიცხვების შეყვანას, მაგრამ ამჯერად აღარ განსაზღვრავს რაოდენობას.
# შეყვანილი რიცხვები უნდა შეინახოთ სიაში numbers.
# საბოლოოდ, პროგრამამ უნდა დაბეჭდოს მხოლოდ თუ რამდენი რიცხვი შეიყვანა მომხმარებელმა.


N1 = int(input("Please input a number: "))
N2 = int(input("Please input a number: "))
N3 = int(input("Please input a number: "))
N4 = int(input("Please input a number: "))
N5 = int(input("Please input a number: "))

Numbers = []

Numbers.append(N1)
Numbers.append(N2)
Numbers.append(N3)
Numbers.append(N4)
Numbers.append(N5)

print(len(Numbers))