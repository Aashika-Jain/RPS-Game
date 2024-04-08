rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
list =[rock,paper,scissors]
a = int(input("What do u choose ? Type \n 0 for rock \n 1 for paper \n 2 for scissors \n your choice ->"))
if a>2:
  print("Invalid choice")
else:  
  print(list[a])
  b = random.randint(0,2)
  print("computer's choice ->",b)
  print(list[b])
  if a== 0 and b == 2:
    print("You win")
  elif a== 1 and b==0:
    print("You win")
  elif a== 2 and b ==1:
    print("You win")
  elif a==b:
    print("Its a   Draw")
  else:
    print("you lose")

