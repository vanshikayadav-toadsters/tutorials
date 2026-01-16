# Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

# def second_largest(arr):
#     largest = -1
#     second_largest = -1

#     for x in arr:
#         if x > largest:
#             second_largest = largest
#             largest = x
#         elif x != largest and x > second_largest:
#             second_largest = x

#     return second_largest

# arr = [12, 35, 1, 10, 34, 1]
# print(second_largest(arr))  



# Given an array of n integers, the task is to find the third largest element. All the elements in the array are distinct integersthird

# def third_largest(arr):
#     if len(arr) < 3:
#         return -1

    

#     largest=-1
#     second_largest=-1
#     third_largest=-1


#     for num in arr:
#         if num > largest:
#             third_largest=second_largest
#             second_largest=largest
#             largest = num

#         elif num > second_largest:
#             third_largest=second_largest
#             second_largest=num

#         elif num > third_largest:
#             third_largest=num

#     return num 

# arr=[10,35,16,20,34,15]
# print(third_largest(arr))



        


                


