#Maheen Hanif Ghaffar
#CS175
#AverageFromInput

def main():
    total = 0
    count = 0
    numbers_file = open('numbers.txt','r')
    
    for line in numbers_file:
        number = float(line)
        count = count + 1
        total = total + number
        print(f'I read in  {count} number(s) Current number is:    {number: .2f} Total is: {total: .2f}')
        
    average = total / count
    print(f'Average: {average: .1f}')

main()
