grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_0 = (sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]), sum(grades[2]) / len(grades[2]),
            sum(grades[3]) / len(grades[3]), sum(grades[4]) / len(grades[4]))
print(grades_0)

sort = sorted(students)
print(sort)
#a = zip(sort,grades_0)
#print(a)

gpa = dict(zip(sort, grades_0))
print(gpa)

#вариант с циклом

grades_1 = []
for i in grades:
    n = sum(i)/len(i)
    grades_1.append(n)
print(grades_1)
sort = sorted(students)
print(sort)
gpa = dict(zip(sort, grades_0))
print(gpa)
