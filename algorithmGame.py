# my_list1 = [range(100,1000)]
# my_list2 = [range(100, 1000)]
# my_added_list = []

# for i in my_list1:
#     for j in my_list2:
#         new_num = i * j
#         my_added_list.append(new_num)

# my_added_list.sort(reverse = True)

# def find_palindrome(lists):
#     for i in lists:
#         num_string = str(i)
#         if num_string[0] == num_string[-1] and num_string[1] == num_string[-2] and num_string[2] == num_string[-3]: 
#             return num_string

# print(find_palindrome(my_added_list))

def var1(x,y):
    return y and var1(y, x % y) or x
def var2(x,y): 
    return x * y / var1(x,y)

n = 1
for i in range(1, 21):
     n = var2(n, i)
print(n)
