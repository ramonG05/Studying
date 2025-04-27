name = input('enter your name: ')
if len(name) < 3:
    print('name is too short')
elif len(name) > 50:
    print('name is too long')
else:
    print('name looks good')
    
weight = int(input('enter your weight: '))
unit = input('(L)bs or (K)g: ')

if unit == 'l' or unit == 'L':
        converted = weight * 0.45
        print(f'You are {converted:.2f} kilos')
elif unit == 'k' or unit == 'K': 
        converted = weight / 0.45
        print(f'You are {converted:.2f} pounds')
