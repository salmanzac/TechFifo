def count_digits(number):
    number = abs(number)
    
    if number == 0:
        return "sorry enter number grater than 0"
    
    return len(str(number))


print(count_digits(23456))  


    