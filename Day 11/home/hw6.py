# პროგრამა მომხმარებელს სთხოვს გამოცდის ქულის შეყვანას და შეფასების განსაზღვრას.
# ინსტრუქციები:
# თუ ქულა 90-ზე მეტია, შეფასება იყოს "A".
# თუ ქულა 80-დან 89-მდეა, შეფასება იყოს "B".
# თუ ქულა 70-დან 79-მდეა, შეფასება იყოს "C".
# თუ ქულა 60-დან 69-მდეა, შეფასება იყოს "D".
# თუ ქულა 60-ზე ნაკლებია, შეფასება იყოს "F".



Exam_points = int(input("Please input your Points: "))
if Exam_points > 90:
    print("Your rating is A")
elif Exam_points >= 80 and Exam_points <= 89:
    print("Your rating is B")    
elif Exam_points >= 70 and Exam_points <= 79:
    print("Your rating is C")    
elif Exam_points >= 60 and Exam_points <= 69:
    print("Your rating is D")
elif Exam_points < 60:
    print("Your rating is F")  

