# დავალება: მომხმარებლის რიცხვების სიის შექმნა და დამუშავება
# შექმენით პროგრამა, რომელიც შემდეგ ნაბიჯებს შეასრულებს:
# მომხმარებლისგან მოითხოვეთ რიცხვების შეყვანა (input()), თითო რიცხვი თითო შეყვანაზე.
# შეყვანილი რიცხვები შეინახეთ სიაში user_numbers.
# შეყვანა უნდა გაგრძელდეს მანამ, სანამ მომხმარებელი არ შეიყვანს ცარიელ ხაზს (ანუ უბრალოდ დააჭერს Enter-ს).
# სიის შექმნის შემდეგ, პროგრამამ უნდა შეამოწმოს:
# თუ სიაში არსებობს რიცხვი, რომელიც 10-ზე მეტია, დაბეჭდოს შეტყობინება: "სიაში არის 10-ზე მეტი რიცხვი".
# წინააღმდეგ შემთხვევაში, დაბეჭდოს შეტყობინება: "სიაში 10-ზე მეტი რიცხვი არ არის".
# ბოლოს, დაბეჭდეთ სია და სიის ელემენტების ჯამი.

user_numbers1 = int(input("please input numbers: "))
user_numbers2 = int(input("please input numbers: "))
user_numbers3 = int(input("please input numbers: "))
user_numbers4 = int(input("please input numbers: "))
user_numbers5 = int(input("please input numbers: "))

GOA = []

GOA.append(user_numbers1)
GOA.append(user_numbers2)
GOA.append(user_numbers3)
GOA.append(user_numbers4)
GOA.append(user_numbers5)


BOMBASTIC = [10]

while GOA == " ": 
   break


if GOA > BOMBASTIC:
   print("სიაში არის 10-ზე მეტი რიცხვი.")
elif GOA < BOMBASTIC:
   print("სიაში არის 10-ზე ნაკლები რიცხვი.")   

print(user_numbers1 + user_numbers2 + user_numbers3 + user_numbers4 + user_numbers5)

# elif user_numbers1 > 10:
#    print("სიაში არის 10-ზე მეტი რიცხვი")    
# elif user_numbers1 < 10:
#    print("სიაში არ არის 10-ზე მეტი რიცხვი")  

# print(user_numbers)