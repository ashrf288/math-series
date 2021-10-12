
    # By recursion
    
def fibonacci(n):
   if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
   elif n==0:
        return 0
    # Second Fibonacci number is 1
   elif n==1:
        return 1
   else:
        return fibonacci(n-1)+fibonacci(n-2)
   



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

    

def mySeries(number,first_number,second_number):
            '''
             call this function create new series which starts with
           first num and then secound num  and return the nth value 
            of that series
            '''
            a = first_number
            b = second_number
     
            if (number == 0) :
              return a
    # generating number
            for i in range(2, number + 1) :
               c = a + b
               a = b
               b = c
            return number

def sum_series(number,first_number=0,second_number=1):
    if first_number==0 or second_number==1:
          fibonacci(number)
    elif first_number==1 or second_number==2 :
          Lucas(number)
    else:
      
        mySeries(number,first_number,second_number)


        # sum_series(number-1,first_number,second_number)+ sum_series(number-2,first_number,second_number)