A = [1,2,3,4,5,6,]
k = 4
i = 0 ;

while i < len(A) and A[i]!=k:
     i = i+1
     if i < len(A):
         return i
     else:
         return -1
     