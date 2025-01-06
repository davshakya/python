# l = [1, 2, 3, 4, 6]
# print(dir(l))
# print(dir(iter(l)))
#
#
# def mu_own_for_loop_using_iterator(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             print(next(iterator))
#         except StopIteration:
#             break
#
#
# mu_own_for_loop_using_iterator(l)
#


##########################################################################################
# class my_range:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return my_own_range_iterator(self)
#
#
# class my_own_range_iterator:
#     def __init__(self, iterable_obj):
#         self.iterable = iterable_obj
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.iterable.start >= self.iterable.end:
#             raise StopIteration
#         current = self.iterable.start
#         self.iterable.start += 1
#         return current
#
#
# for i in my_range(1, 10):
#     print(i)

##############################################################################################


# def my_own_range_using_generator():
#     for i in range(11):
#         yield 1*i
#
#
# print(my_own_range_using_generator())
# print(dir(my_own_range_using_generator()))
#
# for i in my_own_range_using_generator():
#     print(i)


##############################################################################################

def read_file_with_generator(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line


file_nm = "../table.txt"
read_file = read_file_with_generator(file_nm)
for i in read_file:
    print(i)
