# მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით(ეს იქნება მისი ქულა). თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A", თუ 80-დან 90-მდე, გამოუტანეთ "Your grade is B", თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", სხვა შემთხვევაში გამოუტანეთ "Your grade is D"

User_points = int(input("please input your score: "))
if User_points > 90  < 100:
   print("Your grade is A")
elif User_points > 80  < 89:
   print("your grade is B") 
elif User_points > 70  < 79:
   print("your grade is C")   
elif User_points > 0  < 69:
   print("your grade is D")