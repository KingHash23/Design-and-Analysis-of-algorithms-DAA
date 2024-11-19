def fib_bottom_up(n):
     if n ==1 or n== 2:
      return 1
     bottom_up = [None]*(n+1)
     bottom_up[1] = 1
     bottom_up[2]= 1
     for k in range(3, n+1):
      bottom_up[k] = bottom_up[k-1] + bottom_up[k-2]
      return bottom_up[n]
fib_bottom_up(5)
