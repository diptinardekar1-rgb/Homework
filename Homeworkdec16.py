# # Tuple itration using range to create two lists

marks = (45,78,32,90,55,29,68)

# for i in marks:
#     print(i)  
          
# #odd even marks

# even_number = []
# odd_number = []
# for i in marks:
#     for num in marks:
#         if num % 2 ==0:
#             even_number.append(num)
#         else:
#             odd_number.append(num) 
# print("original list of tuple",marks) 
# print("even number",even_number)            #78, 32, 90, 68
# print("odd number"),odd_number              #45,  55


# marks of student pass or fail using tuple

pass_marks=[]
fail_marks=[]

for i in range(len(marks)):
    if marks[i] >= 35:
        pass_marks.append(marks[i])
    else:
        fail_marks.append(marks[i])
print("pass marks",pass_marks)           
print("fail marks",fail_marks)            

# pass marks [45, 78, 90, 55, 68]
# fail marks [32, 29]

