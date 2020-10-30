#https://www.codechef.com/problems/FLOW013
T=int(input())
for i in range (0,T):
    A,B,C=input().split()
    if A+B+C==180:
        print("YES")
    else:
        print("NO")
        
