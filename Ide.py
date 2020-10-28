#Program to create a dictionary which stores names of employees and their income
n =  int(input("Enter the number of employees: "))
count = 1
employee = dict()    #create an empty dictionary
for count in range (n):
 name = input("Enter the name of the Employee:")
 income  = int(input("Enter the income:"))
 employee[name] = income 
print("\n\nEMPLOYEE_NAME\tincome")
for k in employee:
  print(k,'\t\t',employee[k])
# end 

