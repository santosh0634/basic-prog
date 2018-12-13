ref=lambda  no1,no2,no3:no1 if no1<no2 and no1<no3 else no2 if no2<no1 and no2<no3 else no3
a=int(input("enter no1 val="))
b=int(input("enter no2 val="))
c=int(input("enter no3 val="))
print("small number",ref(a,b,c))
