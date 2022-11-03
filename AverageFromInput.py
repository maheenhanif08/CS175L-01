#Maheen Hanif Ghaffar
#CS175
#AverageFromInput

def main():
    total = 0
    count = 0
    
    try:
        numbers_file = open('numbers.txt','r')
    
        for line in numbers_file:
            try:
                number = float(line)
            
            except ValueError:
                line = line.strip('\n')
                print("Non-numeric data found in the file: " +line)

            else:
                count = count + 1
                total = total + number
                print(f'I read in  {count} number(s) Current number is:    {number: .2f} Total is: {total: .2f}')

    except IOError:
        print('An error occured trying to read the file.')
        
    average = total / count
    print(f'Average: {average: .1f}')
    
    

main()
