#https://www.codechef.com/problems/CHOPRT
#tested
T=int(input())
for i in range(0,T):
    A,B=input().split()
    if A<B:
        print("<")
    elif A>B:
        print(">")
    else:
        print("=")
        
        
