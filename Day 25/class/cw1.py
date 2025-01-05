# დავალება:
# მომხმარებელმა უნდა შეიყვანოს ტექსტი. პროგრამა შეასრულებს შემდეგ ნაბიჯებს:
# ტექსტის ყველა სიმბოლოს მცირე ასოებად გადაკეთება.
# ტექსტის ყველა სიმბოლოს დიდი ასოებად გადაკეთება.
# ტექსტის მხოლოდ პირველი სიმბოლოს გადაქცევა დიდ ასოდ, დანარჩენები დარჩება პატარა ასოებად.
# მოძებნოს მომხმარებლის მიერ შეტანილი სიტყვა ტექსტში და დააბრუნოს მისი ინდექსი.

Bombastic_text = str(input("Please input a text: "))
print(Bombastic_text.lower())
print(Bombastic_text.upper())
print(Bombastic_text.capitalize())
Bombastic_word = str(input("Please input a word: "))
word = Bombastic_text.find(Bombastic_word)
print(word)