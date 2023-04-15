# class Numfun:
#     def __init__(self,n=0):
#         self.num = n
#     def get_square_upto_n(self, n) :
#         square = (x**2 for x in range(self.num,n+1))
#         return square
import numpy
import numpy as np

#GENERATORS
# square = (x**2 for x in range(1, 11))
#
# try:
#     while(1):
#        print(next(square))
# except StopIteration:
#     print("Holy shit that's a lot of number I'm done")


#SPIRAL ARRAY
# import numpy as np
# a = np.arange(1,10)
# b = a.reshape((3,3))
# temp = []
# key = True
# while key:
#     if b.size == 1:
#         # t = b
#         # for i in range(len(t[0])):
#         #     print(t[0][i])
#         key = False
#
#     t = b[0:1]
#     for i in range(len(t[0])):
#         temp.append(t[0][i])
#     dim = b.shape[0]
#     b = b[1:dim]
#     b = np.rot90(b)
#
# yo = np.array(temp)
# print(yo)



#TRACE
# import numpy as np
# import codecs
# a = np.arange(1,10)
# b = np.append(a,[10,11,12])
# a = a.reshape((3,3))
# a = np.append(a,[10,11,12])
# a = a.reshape((4,3))
# c = a.flatten()
# print(b)
# print(a)
# print(c)
# print(np.linalg.norm([[1,0],[0,0]]))
# new_string = 'Let\'s meet today at 9:00pm'
# coded = codecs.encode(new_string, encoding="cp037",errors="ignore")
# print(coded)
# decoded = codecs.decode(coded, encoding="cp037",errors="ignore")
# print(decoded)

# class Meow:
#     def __init__(self,name):
#         self.__name = name
#
# a = Meow("Hello")
# print(a._Meow__name)



#USING THE GLOBAL NAMESPACE
# count = 0
# # def counter():
# #     print("Increasing count")
# #     globals()["count"] +=1
# #     print(f"count changed to {globals()['count']}")
# for i in range(0,10):
#     counter()



# count = 0
# def counter():
#     print("Increasing count")
#     global count
#     count +=1
#     print(f"count changed to {count}")
# for i in range(0,10):
#     counter()
#

class dumbfellow:
    '''Hellooooooooowooooooooo'''
    x=0
    def hello(self):
        print("Meow")

print(dumbfellow.__dict__)

