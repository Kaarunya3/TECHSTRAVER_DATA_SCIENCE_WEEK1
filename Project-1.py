import random
import array

NUMBERS=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWER_CASE=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
UPPER_CASE=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
SYMBOL=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  '*', '(', ')', '<']
Max_length=8
LIST=NUMBERS+LOWER_CASE+UPPER_CASE+SYMBOL
password=""
password+=random.choice(UPPER_CASE)
password+=random.choice(LOWER_CASE)
password+=random.choice(NUMBERS)
password+=random.choice(SYMBOL)
for i in range(Max_length-4):
    password=password+random.choice(LIST)
    password_list = array.array('u', password)
    random.shuffle(password_list)

password=""
for i in password_list:
    password+=i
    
print(password)