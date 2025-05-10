# 1-x^2/2!+x^4/4!-.......      res=res+sign*power/fact
def cosineseriessum(x,n):
    PI=3.142
    x=x*PI/180
    res=1
    sign=1
    power=1
    fact=1
    for i in range(1,n):
        sign=sign*-1
        power=power*x*x
        fact=fact*(2*i-1)*(2*i)
        res=res+sign*power/fact
    return res
x=int(input("Enter  the angle in degreees: "))
n=int(input("Enter the no:of terms: "))
print("The sum is "+str(round(cosineseriessum(x,n),6)))
