def simple_pyramid(n=5): #SIMPLE PARAMID
    print("******** SIMPLE PARAMID **********")
    for i in range (0,n+1):
        for j in range(0,i):
            print("*", end=" ")
        print("")

def flipped_simple_pyramid(n=5):
    print("******** FILPPED SIMPLE PARAMID **********")
    for i in range (1,n+1):
        print("  "*(n-i), end="")
        print("* "*i)

def inverted_pyramid(n=5):
    print("******** INVERTED PARAMID **********")
    for i in range (n+1,0,-1):
        for j in range(0,i):
            print("* ", end="")
        print("")

def flipped_inverted_pyramid(n=5):
    print("******** FLIPPED INVERTED PYRAMID **********")
    for i in range (0,n+1):
        print("  "*(i), end="")
        print("* "*(n-i))

def triangle(n=5):
    print("******** TRIANGLE **********")
    for i in range (0,n+1):
        print(" "*(n-i), end="")
        print("* "*i)

def inverted_triangle(n=5):
    print("******** INVERTED TRIANGLE **********")
    for i in range (0,n+1):
        print(" "*i, end="")
        print("* "*(n-i))

def half_dimond_patern(n=5):
    n=int(n/2)
    print("******** HALF DIMOND **********")
    for i in range(1,n+1):
        for j in range(1,3):
            if j==2: print("   ", end="")
            print("*     "*i)
        if i==n: print("*     "*(n+1))
    for i in range(n,0,-1):
        for j in range(1,3):
            if j==1: print("   ", end="")
            print("*     "*i)
            

def flipped_half_dimond_patern(n=5):
    print("******** FLIPPED HALF DIMOND **********")
    m=n
    n=int(n/2)
    for i in range(1,n+1):
        for j in range(1,3):
            if j==1: print("   ", end="")
            print("      "*(n-i), end="")
            print("   *  "*i)
        if i==n: print("*     "*(n+1))
    for i in range(n,0,-1):
        for j in range(1,3):
            if j==2: print("   ", end="")
            print("      "*(n-i), end="")
            print("   *  "*i)
        

def dimond_patern(n=5):
    print("******** DIMOND **********")
    for i in range (0,n):
        print(" "*(n-i), end="")
        print("* "*i)
    for i in range (0,n+1):
        print(" "*i, end="")
        print("* "*(n-i))

def hour_glass_patern(n=5):
    print("******** HOUR GLASS **********")
    for i in range (0,n):
        print(" "*i, end="")
        print("* "*(n-i))
    for i in range (2,n+1): 
        print(" "*(n-i), end="")
        print("* "*i)

try:
    n=int(input("Enter the hieght of the paramidpatern: "))
    if n<0: n*=-1
    if n==0: n=5
except:
    n=5

simple_pyramid(n)
flipped_simple_pyramid(n)
inverted_pyramid(n)
flipped_inverted_pyramid(n)
triangle(n)
inverted_triangle(n)
half_dimond_patern(n)
flipped_half_dimond_patern(n)
dimond_patern(n)
hour_glass_patern(n)
 