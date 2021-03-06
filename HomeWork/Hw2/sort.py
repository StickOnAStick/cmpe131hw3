my_list = [2, 10, 9, 3, 2, 8]
str_list = ["hello", "gaming", "killer"]

def sort_list(list):
    n = len(list)
    i = 0

    #Data type checking 
    if(n==0):
        return []
    elif( (type(list[0]) is not int) and (type(list[0]) is not float) and (type(list[0]) is not str) ):
        #if not int or float array, exit function
        print("ERROR: Wrong data type for sorting, please enter int or float values")
        return 
    elif((type(list[0]) == str)):
            list.sort() #inbuilt sort function can sort lexigraphically and alphanumerically

    #if list is an array of ints or floats sort manually via below
    while i < n:
        j = i+1
        #print("Itteration: " + str(i) + " of the outer loop")
        while j < n:
            #print("--Itteration: " + str(j) + " of the inner loop")
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
            j = j + 1
        i = i + 1
    return list

print(sort_list(my_list))
print(sort_list(str_list))

new_list = []
print(sort_list(new_list))