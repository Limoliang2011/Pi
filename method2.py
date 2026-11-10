from decimal import Decimal, getcontext
getcontext().prec = int(input("Please set precision:"))
start=2
minos=1
result=3
times=int(input("Deepth:"))
for x in range(times):
    print("after {} ranges,the result is:".format(x+1),end=" ")
    result+=minos*(Decimal('4')/Decimal(str(start*(start+1)*(start+2))))
    print(result)
    minos=-minos
    start+=2