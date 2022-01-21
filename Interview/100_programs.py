# class Student():
#     def __init__(self, name, age, school):
#         self.name=name
#         self.age=age
#         self.school=school
        
# std=Student("Manan",8,"SN_Gupta")
# std1=Student("Manav",8,"SN_Gupta")

# print(std.name)
# print(std.age)
# print(std.school)
# print(std1.name)
# print(std1.age)
# print(std1.school)

# import array as arr
# My_Array=arr.array('i',[1,2,3,4])
# # My_list=[1,'abc',1.20]
# print(My_Array)
# # print(My_list)
# # Array1=arr.array(1,4)
# # print(Array1)

# def hello():
#     a=2+4
#     return a
# print(hello())

# def hello():
#     a=2+4
#     return a
# print(hello())

# d=[6,4,2,3,5]
# d2=[5,6,7,8]
# d.append(5)
# d.extend(d2)
# print(d)
# print(d.count(1))
# print(len(d))
# print(d.index(1))
# print(sorted(d))
# print(min(d))
# print(max(d))
# d.remove(6)
# print(d)

a=5
for i in range (a):
    # i=i+1
    i=i*1
    if i<100000:
        print(i)
    else:
        continue