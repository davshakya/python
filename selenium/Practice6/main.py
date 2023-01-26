try:
    a=5
    b="abc"
    c=a+b
    print(c)
except:
    print("Some how excpet block is run.")
finally:
    print("Final block run")
#
# except Exception as e:
#     print(e)

# c=0
# # if c!=0:
# #     raise Exception("exception raised")

# c=0
# assert(c!=0)