import sys

d = {"a": 1, "b": 4, "y": {"c": 6, "k": {"z": 10}}}
l = [1, 2, 3, {"x": 5}]
# del d["a"]
# print(d)
# print(d.items())


# l1={'foo', 'bar'}
# dl=dict(l1)
# print(dl)
#
# dn = d["y"]["k"]["z"]
# print(dn)
#
# d.update({"s":4})
# print(d)
# # print(dn)
# # print(l[3]["x"])
# # print(d.pop("a"),d)
# d.popitem()
# print(d)
# x = d.values()
# # print(x)
#
#
#
# x = [
#     'a',
#     'b',
#     {
#         'foo': 1,
#         'bar':
#             {
#                 'x': 10,
#                 'y': 20,
#                 'z': 30
#             },
#         'baz': 3
#     },
#     'c',
#     'd'
# ]
# #
# d = x[2]["bar"]["z"]
# # print(d)
# d1={}
# x=d1.fromkeys([1,2,3],"a")
# x1=d.copy()
# x.setdefaul
# print(x1)
# def dict_practice(d):
#     print(d)
# dict_practice(d)
d = {"a": 9, "b": 4}
for i in d:
    print(i, d[i])

# print(d.get("a"))
# print(d["a"])
# a=717
# rcount=sys.getrefcount(a)
# print(rcount)
print(dir(d))
print(d.fromkeys((1, 3, 4), 5))


# l=lambda x,y:x+y
# print(l(4,5))


