#CS175
#Maheen Hanif Ghaffar
#rainfall.py

month_rainfall = 0
year = 0

years = int(input('Enter the number of years (1, 2, or 3)? '))

while years < 1 or years > 3:
    print("Invalid number of years, please enter again.")
    years = int(input('Enter the number of years (1, 2, or 3)? '))
    
if years == 1:
    year = 0

for x in range (1,  years + 1):
    year = year +1
    print("For year", year,":")
    for y in range (1, 13):
        rainfall_inch = float(input('Enter the rainfall amount for the month: '))
        month_rainfall = rainfall_inch + month_rainfall

months = years * 12
average_monthly_rainfall = month_rainfall / months

print('For', months, 'months')
print(f'Total rainfall:{month_rainfall: .2f} inches')
print(f'Average monthly rainfall:{average_monthly_rainfall: .2f} inches')
