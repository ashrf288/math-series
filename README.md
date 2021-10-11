
## fibonacci

[x]Create a function called `fibonacci`.
 [x]The function should have one parameter `n`.
  [x]The function should return the **nth** value in the fibonacci series. 
  [x]You may implement the function using recursion or iteration. 
  []If you are feeling particularly frisky, do both as separate functions.

  ## Lucas Numbers

  [x]Create a function called `Lucas`
  [x]The function should have one parameter `n`.
  [x]The function should return the **nth** value in the lucas series.
  [x]You may implement the function using recursion or iteration. 


  ## sum_series

  [x]`sum_series` with one required parameter and two optional parameters.
   []The required parameter will determine which element in the series to print.
    The two optional parameters will have default values of 0 and 1 and will determine the first two values for the series to be produced
[x]Calling this function with no optional parameters will produce numbers from the fibonacci series

[x]Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. 
    ( else:
        
    if number==0:
        return first_number
    if number==1:
        return second_number
    return (sum_series(number-1)+sum_series(number-2)))