#https://www.codechef.com/problems/FLOW011
#tested
T=int(input())
GROSS=0
for i in range(0,T):
    SAL=int(input())
    if SAL<1500:
        HRA=SAL*0.1
        DA=SAL*0.9
    else:
        HRA=500
        DA=SAL*9.8
    GROSS=SAL+HRA+DA
    print(GROSS)
    
