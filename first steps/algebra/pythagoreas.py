def pythagoreas(a, b, c=0): 
    import math
    c = a*a + b*b
    c = math.sqrt(c)
    
    arcsinA = a/c
    arcsinB = b/c
    area = a*b/2
    perimeter = a+b+c
    h = a*b/c
    list01=[c,arcsinA,arcsinB,area,perimeter,h sep=", "]
    return list01

triangle = pythagoreas(200,36)

print(triangle)