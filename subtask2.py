# In first 4 lines we create our list
list_a = [] 
 
list_a = [int(item) for item in input("Enter the list items : ").split()]
 
for i in list_a:
    if i==-1:
        list_a.remove(i)

number_of_elements = len(list_a)

if number_of_elements == 0:
    print("m=-1, a=-1")
    
total=0
    
for ele in range(0, len(list_a)):
    total = total + list_a[ele]
    
if number_of_elements != 0:
    a=total/number_of_elements

list_a.sort()

if number_of_elements > 1:
    print("Number of elements:",number_of_elements,"/Sum of the elements:",total,"/The minimum:",*list_a[:1],"/Their mean:",a,)
    
    #it looks  it looks like I learned how to use git today
