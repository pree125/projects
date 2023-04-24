sum, count = None, None  
check = True
while check:
    try: 
        number = input('Enter a number')
        if number == 'done':
            is_number = False
            check = False
            quit
        else:
            is_number = True
            number = int(number)
    except:
        is_number = False
        print('not a number skipping')

    if is_number: 
        if sum is None and count is None :
            sum = (number)
            count = 1
        else:
            sum += (number)
            count += 1
        
print(f'sum {sum}, count {count}, average {sum/count}')
