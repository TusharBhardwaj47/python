n=float(input('Enter your percentage : '))
if n>100 or n<0:
 print('Invalid input from user.')
elif n>85:
 print('GRADE:A+')
elif n>=65 or n<=85:
 print('GRADE:A')
elif n>=45 or n<65:
 print('GRADE:B')
elif n>=25 or n<45:
 print('GRADE:C')
else:
 print('GRADE:D')