first=int(input('Ведите число 1: '))
second=int(input('Ведите число 2: '))
third=int(input('Ведите число 3: '))
if first==second==third:
    print(3)
elif first==second or first==third or second==third:
    print(2)
#if first!=second and first!=third and second!=third:
else:
    print(0)












