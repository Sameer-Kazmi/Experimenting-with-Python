def Factorial(num):
    if num==0:
        return 1
    return num*Factorial(num-1)
def Fibonacci(num):
    if num in (1,2):
        return num-1
    return Fibonacci(num-1)+Fibonacci(num-2)
def Power(num,pow):
    if pow==0:
        return 1
    return num*Power(num,pow-1)
def LCM(x,y):
    z=x%y
    if z==0:
        return x
    return x*(LCM(y,z))//z
def HCF(x,y):
    if x==0 or y==0:
        return x+y
    z=x%y
    if z==0:
        return y
    return HCF(y,z)
print((HCF(0,0)))
