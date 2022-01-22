
# a="DIVYAKHURANA"
# # b=[]
# # i=0
# # j=5
# # while i<len(a):
# #     if  a[i] not in b:
# #         c=a[i]
# #         b.append(c)
# #         b.append(j)
# #         j+=5
# #     i+=1
# # print(b)

# count={}
# for i in a:
#     if i not in count:
#         count[i]=1
#     else:
#         count[i]=count[i]+1
# print(count)


def even(x):
    if x%2==0:
        return True
    else:
        return False
# even(20)
def odd(y):
    if y%3==0:
        return True
    else:
        return False
print(even(12))