#Astro Ohnuma
#8/31/17
#nameage.py - asking for a users name and age. Then print how many characters are in each name and then how old they will be next year

name = input('Enter your first and last name: ')
age = int(input('Enter your age: '))
fname,lname=name.split()
print('Your first name has',len(fname),'letters')
print('Your last name has',len(lname),'letters')
print('Next year you will be',age+1,'years old')



