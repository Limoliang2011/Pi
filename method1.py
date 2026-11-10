from decimal import Decimal, getcontext
getcontext().prec = int(input("Please set precision:"))
start=1
minos=1
result=0
times=int(input("Deepth:"))
for x in range(times):
    print("after {} ranges,the result is:".format(x+1),end=" ")
    result+=minos*(Decimal('4')/Decimal(str(start)))
    print(result)
    minos=-minos
    start+=2