number=int(input('Enter a value : '))
n=0
while(n*(n+1)<=number):
    if n*(n+1)==number:
        print('Pronic Number')
        break
    n=n+1
else:
    print('Not a Pronic Number')
