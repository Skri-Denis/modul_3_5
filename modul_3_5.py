def get_multiplied_digits (number):
    while number % 10 == 0: # убираем 0 в конце number
        number = int (number /10)
   # print (number)
    str_number = str (number)
    first = int (str_number [0])
   # print (str_number)
   # print (first)
    if len (str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
