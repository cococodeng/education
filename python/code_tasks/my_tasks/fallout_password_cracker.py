# Flt Psw

# [password, isTried, correctLetters]

# CORR PASS = 'OZZIE'

passwords = [
    ['FEZZY', '', 0],
    ['FIZZY', '', 0],
    ['POZZY', '', 0],
    ['FRIZZ', '', 0],
    ['OZZIE', '', 0],
    ['PIZZA', '', 0],
    ]
for password in passwords: password[0] = password[0].upper()
possible_passwords = []
numb_tries = 4
### To do string same letters checker


guess = 'POZZY'
#       'OZZIE'
corr_posns = 1

# Return same letters
def (str1, str2):
    counter = 0
    
    

for password in passwords:
    if password[0] == guess:
        password[1] = 'tried'
        password[2] = corr_posns

for password in passwords: print(password, end='\n')


#### Todo : create square matrix of passwords letters intersection