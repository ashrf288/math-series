
    # By recursion
    
def fibonacci(n):
    zero = 0
    one = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return zero
    elif n == 1:
        return one
    else:
        for i in range(2, n):
            c = zero + one
            zero = one
            one = c
        return one
 
   



def Lucas(n):
    a = 2
    b = 1
     
    if (n == 0) :
        return a
  
    # generating number
    for i in range(2, n + 1) :
        c = a + b
        a = b
        b = c
     
    return b


def sum_series(number,first_number=0,second_number=1):
    if first_number==0 or second_number==1:
          fibonacci(number)
   