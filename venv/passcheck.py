print("Is you password strong enough?")
print("Special Characters examples: \" !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~\"")

password=str(input('Type your password: '))
special_char=[' ', '!', '"', '#', '$', '%', '&', '\\', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
number_list=['1','2','3','4','5','6','7','8','9','0']

char_count=0
special_count=0
upper_count=0
lower_count=0
number_count=0

for c in password:
    char_count+=1
    if c in special_char:
        special_count+=1
    if c in number_list:
        number_count+=1

for l in password:
    if l.isupper():
        upper_count+=1
    else:
        lower_count+=1

if special_count !=0 and upper_count !=0 and lower_count !=0 and number_count !=0 and char_count <= 8:
    print("Congratulations, your password is strong enough: ")
else:
    print("Your password is weak.")
    print("Password suggestion: i'm going to do this later")

print(char_count)
print(special_count)
print(upper_count)
print(lower_count)
print(number_count)