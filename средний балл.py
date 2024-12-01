#Исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#Упорядочить по алфавиту
print(sorted ({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}))
#Ищем средний балл
a=grades[0]
print(a)
b=grades[1]
print(b)
c=grades[2]
print(c)
d=grades[3]
print(d)
e=grades[4]
print(e)
average_a=sum(a)/len(grades[0])
print(average_a)
average_b=sum(b)/len(grades[1])
print(average_b)
average_c=sum(c)/len(grades[2])
print(average_c)
average_d=round(sum(d)/len(grades[3]),1)
print(average_d)
average_e=sum(e)/len(grades[4])
print(average_e)
#соотношение ученика с его средним баллом
students={"Aaron":average_a, "Bilbo":average_b, "Johnny":average_c,"Khendrik":average_d,"Steve":average_e}
print(students)



