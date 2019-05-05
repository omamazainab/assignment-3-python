# event_venue= input('where is event?')
# if event_venue == 'phupho home':
#     print('I am busy cannot go')
# elif event_venue == 'mamu home':
#     print('OK I am coming')
# elif event_venue == 'cacha home':
#     print('OK I can go')
# else :
#     print('surely I will go, how can I miss a party')
number1 = input('enter number1 ')
number1= int(number1)

number2 = input('enter number2 ')
number2= int(number2)

operator = input('enter operator ')

if operator == '+':
    print('the addition of'+ str(number1)+' and '+str(number2)+' is ' + str(number1 + number2) )
elif operator == '-':
    print('the difference of'+ str(number1)+' and '+str(number2)+' is ' + str(number1 - number2) )
elif operator == '*':
    print('the multiplication of'+ str(number1)+' and '+str(number2)+' is ' + str(number1 * number2) )
elif operator == '/':
    print('the division of'+ str(number1)+' and '+str(number2)+' is ' + str(number1 / number2) )
elif operator == '%':
    print('the remainder of'+ str(number1)+' and '+str(number2)+' is ' + str(number1 % number2) )
else :
    print('invalid operator')

