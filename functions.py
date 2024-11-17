def Factorial(num):  # Creating a function to find the factorial of the given number.
    if num==0:  # Checking whether the given number is zero.
        return 1  # Returns 1 since 0!=1. This return is important as this statement will terminate the recursion.
    return num*Factorial(num-1)  # Returns num*Factorial(num-1) because num!=num*(num-1)!. This line is executed when num is not 0.
def Fibonacci(num):  # Creating a function to find the nth Fibonacci number.
    if num in (1,2):  # Checking whether user wants the 1st, 2nd Fibonacci number.
        return num-1  # 1st Fibonacci number is 0 and 2nd Fibonacci number is 1. This can be combined into the nth 
                      # fibonacci number is n-1 when n is either 1 or 2.
    return Fibonacci(num-1)+Fibonacci(num-2)  # Returning the sum of n-1 and n-2 fibonacci number because the nth 
                                              # fibonacci number is the sum of (n-1)th and (n-2)th number.
def Power(num,pow):  # Creating a function to find the value of a number num to the power pow (num**pow or num^pow).
    if pow==0:  # Checking whether the power is given as 0.
        return 1  # Any number to the power zero is 1.
    return num*Power(num,pow-1)  # num**pow can be written as num*(num**(pow-1)) or num*Power(num,pow-1).
def LCM(x,y):  # Creating a function to find the lcm of given two numbers.
    z=x%y  # Storing the value of x%y to a third variable z. z actually plays an important part in the recursive 
           # process so that the code terminates.
    if z==0:  # When z is equal to 1.
        return x  # When z=1, this shows that y is a factor of x. Therefore, x will be the lcm of x and y. 
    return x*(LCM(y,z))//z  # If z is not equal to 0, it means that y is not a factor of x. 
                            # To understand the given line, one should remember the given formula: 
                            # LCM(x,y)=x*y/HCF(x,y)
                            # Also, HCF(x,y)=HCF(y,x%y) | If HCF=p, x=mp and y=np where m,n are co-primes. 
                            # Then x%y=mp%np which is equal to kp where k is m%n.
                            # Also HCF of y and z will be p only because HCF of np and kp is p where k=m%n.
                            # Therefore, HCF(x,y)=HCF(mp,np)=HCF(np,mp%np)=HCF(np,kp)=HCF(y,z).
                            # Now, LCM(x,y)=x*Y/HCF(x,y). Now we know that HCF(x,y)=HCF(y,z).
                            # Therefore, LCM(x,y)=x*y/HCF(y,z). If we multiply both numerator and denominator by z:
                            # LCM(x,y)=x*y*z/[HCF(y,z)*z] => LCM(x,y)=x*[y*z/HCF(y,z)]/z=x*[LCM(y,z)]/z
                            # Also, division will give float value and we know that LCM is always an integer. 
                            # So we can use floor division(//) since we know it won't be having remainders and output value will be integer.
                            # Therefor, LCM(x,y)=x*LCM(y,z)//z
def HCF(x,y):   # Creating function to find the hcf of given two numbers.
    if x==0 or y==0:  # Checking whether one of the two numbers is equal to 0.
        return x+y  # Returning x+y will give x when y=0 and y when x=0.
    z=x%y  # Storing x%y in another variable z.
    if z==0:  # When x%y=0.
        return y  # Since x%y is 0, y is a factor of x. Therefore y is the hcf.
    return HCF(y,z)  # When x%y is not equal to 0, this code will be executed.
                     # The logic for this line of code is that HCF(x,y)=HCF(y,z)
                     # where HCF=p and x=mp, y=np, z=x%y=mp%np=kp where k=m%n.
