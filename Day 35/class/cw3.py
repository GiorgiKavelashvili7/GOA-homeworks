"""
  hi
"""

Weight = float(input("Input your weight here: "))
Height = float(input("Input your height here: ")) 
output = " "

formula_height = Height * Height

if Weight / formula_height < 18.5:
    output = "Underweight"
elif Weight / formula_height >= 18.5 and Height / formula_height < 25:
    output = "Normal"
elif Height / formula_height >= 25 and Height / formula_height < 30:
    output = "Overweight"
elif Height / formula_height > 35:
    output = "Obesity"

print(output)
