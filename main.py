import random
list1=[]
#Creates a list of 1000 random numbers between 1 and 10000
for i in range(1000):
    x= random.randint(1, 10000)
    list1.append(x)
print(list1)


def recursive_sort(list1):
    #Base case, since if the lengths of elements in the list is one or less than the list is already sorted
    if len(list1) <= 1:
        return list1

    #Turns the first element in the list to the pivot
    pivot = list1[0]
    #list for elements in the list equal to or less than the pivot
    less_than_pivot = [x for x in list1[1:] if x <= pivot]
    #list for elements in the list greater than the pivot
    greater_than_pivot = [x for x in list1[1:] if x > pivot]

    #recursively sort the lists and combines the lists to form a sorted list
    return recursive_sort(less_than_pivot) + [pivot] + recursive_sort(greater_than_pivot)

#Creates a variable for the sorted list
sorted_list = recursive_sort(list1)
#prints the sorted list
print(sorted_list)
