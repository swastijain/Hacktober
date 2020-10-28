list1 = []
print("how many students marks you want to enter" )
n= int(input( ))
for i in range(0,n):
  print("Enter marks of student",(i+1),":")
  marks = int(input())
  list1.append(marks)
   total = 0
 for marks in list1:
   total = total + marks
 Average = total / n
print("Average marks of",n,"students is:",Average)
# end  