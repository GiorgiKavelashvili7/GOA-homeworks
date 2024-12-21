# დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. გამოიყენეთ while loop. (ვინც არ იცით არითმეტიკული, მაშინ მოიძიეთ ინფორმაცია.

number = 2
sum_even = 0
count_even = 0

while number <= 100:
    sum_even += number
    count_even += 1
    number += 2
    arithmatical= sum_even / count_even
    
    
print(arithmatical)