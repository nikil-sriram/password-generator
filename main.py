import random
amountofpasswords = int(input("How many passwords would you like?"))
amountofcharacters = int(input("How many characters would you like?"))
chars = "q Q w W e E r R t T y Y u U i I o O p P a A s S d D f F g G h H j J k K l L z Z x X c C v V b B n N m M ! @ # $ % ^ * ()"

charssplitted = chars.split()

passwords = [[] for i in range(amountofpasswords)]

for i in range(amountofpasswords):
    testing = random.sample(charssplitted, amountofcharacters)
    stringconverter = ','.join(testing)
    new_string = stringconverter.replace(',', '')
    print(new_string)
