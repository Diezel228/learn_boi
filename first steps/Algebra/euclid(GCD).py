# Euclid's algorithm (greatest common divisor)
#
#divide a and b
#q(quotient) x b + r(remainder)
#loop until a remainder of 0 then GCD=b

print("GCD calculator\n")
a = int(input("provide first #:"))
b = int(input("provide second #:"))
q = (a / b) 
r = (a % b)
print("a","b","q","r \n", sep=" | ")# printing table until r = 0
print(a,b,int(q),r, sep=" | ")

while r >= 1:
    a = b
    b = r
    q = (a / b) 
    r = (a % b)
    print(a,b,int(q),r, sep=" | ")
else:
    print("")

print("GCD: ", str(b))   #lets test
