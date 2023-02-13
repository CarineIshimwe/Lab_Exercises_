list_of_students={'carine ishimwe':53,'davina uwera':45,'cynthia musawu':67,'rebeca ndinayo':95,'thuku christian':98}
print('the name of five different students and their respective grades')
print('NAMES              GRADE')
sum=0
count=0
for x,y in list_of_students.items():
    count=count+1
    sum=sum+y
    print(x,'     ',y)
b = max(list_of_students, key=list_of_students.get)
average=sum/count

print(' the student with the highest grade is called ',b)
print(' the average of the five grades is ',average)

