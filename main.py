#PYTHON PROGRAMS BY M NUMAAN ALI TAHIR
# https://github.com/MNumaan

def simple_pyramid(n=5): #SIMPLE PYRAMID
    print("******** SIMPLE PYRAMID **********")
    for i in range (0,n+1):
        for j in range(0,i):
            print("*", end=" ")
        print("")

def flipped_simple_pyramid(n=5):
    print("\n******** FILPPED SIMPLE PYRAMID **********")
    for i in range (1,n+1):
        print("  "*(n-i), end="")
        print("* "*i)

def inverted_pyramid(n=5):
    print("\n******** INVERTED PYRAMID **********")
    for i in range (n+1,0,-1):
        for j in range(0,i):
            print("* ", end="")
        print("")

def flipped_inverted_pyramid(n=5):
    print("\n******** FLIPPED INVERTED PYRAMID **********")
    for i in range (0,n+1):
        print("  "*(i), end="")
        print("* "*(n-i))

def triangle(n=5):
    print("******** TRIANGLE **********")
    for i in range (0,n+1):
        print(" "*(n-i), end="")
        print("* "*i)

def inverted_triangle(n=5):
    print("\n******** INVERTED TRIANGLE ********** \n")
    for i in range (0,n+1):
        print(" "*i, end="")
        print("* "*(n-i))

def half_diamond_patern(n=5):
    n=int(n/2)
    print("******** HALF DIAMOND **********")
    for i in range(1,n+1):
        for j in range(1,3):
            if j==2: print("   ", end="")
            print("*     "*i)
        if i==n: print("*     "*(n+1))
    for i in range(n,0,-1):
        for j in range(1,3):
            if j==1: print("   ", end="")
            print("*     "*i)
            

def flipped_half_diamond_patern(n=5):
    print("******** FLIPPED HALF DAIMOND **********")
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
        

def diamond_patern(n=5):
    print("******** DIAMOND **********")
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
half_diamond_patern(n)
flipped_half_diamond_patern(n)
diamond_patern(n)
hour_glass_patern(n)
