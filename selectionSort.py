def selection (A):
    for i in range(len(A)):
        minpos = i
        for j in range (i +1, len(A)):
            if A[j] < A[minpos]:
                minpos = j
        swap(A,i,minpos)
def swap (lst, i, j):
    temp = lst[i]
    lst[i]= lst[j]
    lst[j] = temp
    return 
A = [2,3,4,5,7,8,9]
result = selection(A)
print (result)
