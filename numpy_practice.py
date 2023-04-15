# import numpy as np
# a = np.arange(1,10)
# a=a.reshape((3,3))
# b = a[1:3,1:3]
# print(a)
# print(b)


# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()



#Finding time taken by different sorting techniques
# import numpy as np
# import time as t
#
# def bubblesort(a):
#     for i in range(0,len(a)):
#         for j in range(i+1,len(a)):
#             if a[j]<a[i]:
#                 (a[j],a[i])=(a[i],a[j])
#
# a = np.arange(-1000,1001,1000)
# b = np.arange(-1000,1001,1000)
# c = np.arange(-1000,1001,1000)
# d = np.arange(-1000,1001,1000)
#
# t1 = t.perf_counter_ns()
# np.sort(a,kind= "mergesort")
# t2 = t.perf_counter_ns()
# print(t2-t1)
#
# t1 = t.perf_counter_ns()
# np.sort(b,kind= "quicksort")
# t2 = t.perf_counter_ns()
# print(t2-t1)
#
# t1 = t.perf_counter_ns()
# np.sort(c,kind= "heapsort")
# t2 = t.perf_counter_ns()
# print(t2-t1)
#
# t1 = t.perf_counter_ns()
# bubblesort(d)
# t2 = t.perf_counter_ns()
# print(t2-t1)

# a = np.array([1,2,5,4,3])
# n = 10
# m = 20
# print(m,n,sep = " SEPERATINATOR ")


#Encapsulation
# class Meow:
#     def __init__(self):
#         self.__hello = "Hi! Coder!"
#
#     def printer(self):
#         print(self.__hello)
# cat = Meow()
# cat.printer()


# import numpy as np
# p1,p2,p3,p4 = np.array([0,0,0]),np.array([-1,-1,0]),np.array([1,-1,0]),np.array([1,0,1])
#
# answer = np.array([(p4-p1),(p4-p2),(p4-p3)])
# if np.linalg.det(answer)==0:
#     print("True")
# else:
#     print("False")





