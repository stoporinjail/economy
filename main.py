prefix = '!'
import random as r
import sys

money = 0
def help():
  print(f'''Commands:
  -----------------------------------------------------------
  {prefix}help - Displays help.
  {prefix}prefix - Changes prefix
  {prefix}work - Get some money!
  {prefix}crime - Get some money (sometimes a fee)
  {prefix}bet - Bet!
  {prefix}bal''')
help()
while True:
  c = input('What is your command? ')
  if c == prefix+'help':
    help()
  elif c == prefix+'prefix':
    q = input('What to change to? ')
    prefix = q
  elif c == prefix+'work':
    amount = r.randint(50,200)
    print(f'You get ${amount} for working at Pizza Hut!')
    money += amount
  elif c == prefix+'crime':
    outcome = ['good','bad']
    r.shuffle(outcome)
    if outcome[0] == 'good':
      amount = r.randint(50,200)
      print(f'You manage to steal ${amount}')
      money += amount
    else:
      amount = r.randint(50,200)
      print(f'You got caught, and pay ${amount}!')
      money -= amount
  elif c == prefix+'bet':
    qq = input('How much? ')
    qq = int(qq)
    if qq > money:
	    print("You don't have enough money")
	    sys.exit(0)
    outcome = ['good','bad']
    r.shuffle(outcome)
    if outcome[0] == 'good':
      qq += qq
      print(f'You get ${qq}!')
      money += qq
    else:
      print('You lose your money. :(')
      money -= qq
  elif c == 'bal':
    print(f'Your balance is {money}')
    
