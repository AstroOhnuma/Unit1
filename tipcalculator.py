#Astro Ohnuma
#9/1/17
#tipcalculator.py - finding how much to tip

price = float(input('Enter the price of a meal: '))
tip = float(input('Enter what % you would like to tip: '))
print('You should tip',round(price*tip/100,2),'dollars')

