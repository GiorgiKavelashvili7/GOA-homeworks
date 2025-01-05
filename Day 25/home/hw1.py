# რიცხვის გამოცნობის თამაში
# სთხოვს მომხმარებელს მოიფიქროს რიცხვი 1-დან 100-მდე და პროგრამა შეეცდება მის გამოცნობას.
# პროგრამა არაერთხელ ცდის გამოცნობას, თუ გამოცნობილი რიცხვი არის მაღალი, მაშინ უნდა გამოიტანოს  'მაღალი'
# თუ გამოცნობილი რიცხვი ძალიან დაბალია, მაშინ უნდა გამოიტანოს  "დაბალი".
# თუ გამოცნობილი რიცხვი სწორია, მაშინ უნდა გამოიტანოს  "სწორია".
# მთლიანობაში უნდა იყვეს 3 მცდელობა.
# თამაში მთავრდება, როდესაც პროგრამა გამოიცნობს სწორ რიცხვს (break)

def something():
    Mystery_number = int(input("Please input a random number from 1 to 100: "))
    number = 55

    if Mystery_number == number:
        return "სწორია" 
    elif Mystery_number > number:
        return "მაღალი" 
    elif Mystery_number < number:
        return "დაბალი"

print(something())
print(something())
print(something())