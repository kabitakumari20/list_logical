 list1=[[2,3,4],[2,4,5],[4,5,6]]
# i=0
# even=[]
# odd=[]
# c=0
# while i<len(list1):
#     j=0
#     sum=0
#     while j<len(list1[i]):
#         sum=sum+list1[i][j]
#         j=j+1
#         print(sum)
#     c=c+1
#     i=i+1

# sum of list-------------------
# list1=[[2,3,4],[2,4,5],[4,5,6]]
# i=0
# even=[]
# odd=[]
# j=0
# while i<len(list1):
#     c=0
#     sum=0
#     while c<len(list1[i]):
#         sum=sum+list1[i][j]
#         c=c+1
#         print(sum)
#     j=j+1
#     i=i+1
#     if sum%2==0:
#         even.append(sum)
#     if sum%2!=0:
#         odd.append(sum)
# print(even)
# print(odd)


# a=[1,3,4,5]
# # b=["mona","manvi"]
# # print(a+b)
# # a=tuple(b)
# # print(a)
# # a.insert(1,2)
# a[2]="tanjum"
# print(a)

# a=[1,2,3,4,56,7]
# i=0
# b=[]
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
#     b.append(sum)
# if sum%2==0:
#     print(sum,"even")
# else:
#     print(sum,"odd")

# from user input i have to check it is even or odd---------------------

# a=int(input("enter the num="))
# i=1
# b=[]
# while i<=a:
#     num=int(input("enter the num="))
#     b.append(num)
#     i=i+1
# print(b)
# j=0
# even=[]
# odd=[]
# while j<len(b):
#     if b[j]%2==0:
#         even.append(b[j])
#     else:
#         odd.append(b[j])
#     j=j+1
#     # i=i+1
# print(even) 
# print(odd)

# call one funcation to another funcation-----------------------
# def add():
#     a=2
#     b=3
#     c=a+b
#     return c
# def sub():
#     a=9
#     b=7
#     c=a-b
#     return c
# def main():
#     print(add())
#     print(sub())
# main()


# max num---------------------
# list=[[2,3,4,5],[6,7,8,9,10],[3,4,19,20]]
# i=0
# max=0
# c=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         if list[i][j]>max:
#             max=list[i][j]
#         j=j+1
#     c.append(max)
#     i=i+1
# print(c)


# list=[{"a":2,"b":3,"c":7},{"kabita":23,"manvi":23}]
# for i in list:
#     # print(i)
#     for x in list[i]:
#         print(x)


# year=int(input("enter the year="))
# if year%4==0 and year%400==0 or year%100!=0:
#     print(year,"it is leap year")
# else:
#     print(year,"it is not leap yera")

# num=int(input("enter the num="))
# i=0
# while i<=num:
#     if i%2==0:
#         print(i)
#     # else:
#     #     print(i+1)
#     i=i+1



# num=int(input("enter the num="))
# n=num
# sum=0
# while num>0:
#     rem=num%10
#     var=rem*3
#     s=num//10
#     sum=sum+var
# if sum==n:
#     print(n,"it is armstron num")
# else:
#     print(n,"it is not armstron num")

# def add(a,d):
#     c=a+d
#     print(c) 
#     def sub(n,m):
#         b=n-m
#         print(b)
#     print(sub(5,3))
# print(add(2,3))


# def add():
#     i=1
#     while i<5:
#         print(i)
#         i=i+1
# print(add())


# def add(a,b):
#     c=a+b
#     return c
# print(add(4,5))

def even(list1):
    i=0
    b=[]
    c=[]
    while i<len(list1):
        if list1[i]%2==0:
            b.append(list1[i])
        else:
            c.append(list1[i])
        i=i+1
        j=0
        max=0
        while j<len(b):
            if b[j]>max:
                max=b[j]
                # print(max)
            j=j+1
        print(max)
        d=0
        min=0
        while d<len(c):
            if c[d]<min:
                min=c[d]
                # print(min)
            d=d+1
        print(min)
            

    # return b,c
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(even(list1))
even(list1)





