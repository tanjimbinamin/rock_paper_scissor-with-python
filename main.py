import random

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
choice=int(input("what do you choose? 0 for rock, 1 for paper, 2 for scissors : \n"))

easy=[rock,paper,scissors]

pc=random.randint(0,2)
me=choice

image_pc=easy[pc]
image_me=easy[choice]

if (me==0 and pc ==1) or(me==2 and pc==0)or(me==1 and pc==2):
  print(f"pc \n {image_pc} \n me \n {image_me} \n I loose" )

elif(me==0 and pc==2)or(me==1 and pc==0) or(me==2 and pc==1):
   print(f"pc \n {image_pc} \n me \n {image_me} \n I win" )
else:
  print(f"pc \n {image_pc} \n me \n {image_me} \n Draw") 
