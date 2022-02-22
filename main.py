arr = [12, 23, 23, 39, 33]

# we can access the elements of the list by index, and
# for each loop in python
for i in range(len(arr)):
    if arr[i] == 12:
        print("Found at index: ", i, "value: ", arr[i])
        break
    else:
        print("Not found")


# time complexity of the above for loop is O(n)
# because it has to iterate through the entire list
# to find the element

# best is big 0(1)
# worst is big O(n)
# average is big O(n)


# ? time complexity is the about of time it takes to complete the task, as the input grows.


# !constant time complexity is when the time to find any element is constant, even the input increses.
# !linear time complexity is when the time to find any element is linear, even the input increses.
# * it generally is big O(1) and worst case is big O(n)

# ? space complexity is the about of space it takes to complete the task, as the input grows.
# !constant space complexity is when the space to find any element is constant, even the input increses.
# !linear space complexity is when the space to find any element is linear, even the input increses.
# * it generally is big O(1) and worst case is big O(n)


