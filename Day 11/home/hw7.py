# პროგრამა სთხოვს მომხმარებელს რიცხვის შეყვანას და შემდეგ ადგენს, არის თუ არა რიცხვი დადებითი, უარყოფითი თუ ნული. 
# ინსტრუქციები:
# თუ რიცხვი ნულია, დაბეჭდე „ნულია“.
# თუ რიცხვი ნულზე მეტია, დაბეჭდე „დადებითი რიცხვია“.
# თუ რიცხვი ნულზე ნაკლებია, დაბეჭდე „უარყოფითი რიცხვია“

Number = int(input("თუ შეიძლება შემოიყვანე რიცხვი: "))
if Number == 0:
    print("შენ მიერ შემოტანილი რიცხვი ნულია")
elif Number > 0:
    print("შენ მიერ შემოტანილი რიცხვი დადებითია")  
elif Number < 0: 
    print("შენ მიერ შემოტანილი რიცხვი უარყოფითია")     
     
       