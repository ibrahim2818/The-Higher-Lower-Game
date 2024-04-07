from art import logo, vs
from game_data import data
import random
import os


def account_formate(account):
    accountName= account['name']
    accountdescription= account['description']
    accountCountry= account['country']
    return(f'''{accountName}, a {accountdescription}, from {accountCountry} ''')


print(logo)
accountA=random.choice(data)
accountB=random.choice(data)
if accountA==accountB:
    accountB=random.choice(data)
playGame= True
count=0
while playGame:
    print(f'''compare A : {account_formate(accountA)}''')

    print (vs)

    print (f'''Against B : {account_formate(accountB)}''')
    x= input('''Who has more followers? Type 'A' or 'B'\n ''')
    if accountA['follower_count']> accountB['follower_count']:
        Y='A'
    else:
        Y='B'
    if x==Y:
        count+=1
        os.system('cls')
        print(f'''you are right! current score {count}''')
        accountA= accountB
        accountB= random.choice(data)
    else:
        print(f'''you are wrong! Total score {count}''')
        playGame= False

