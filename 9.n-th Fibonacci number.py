#Recurrence Method
def fibrecur(n):
    if n == 0:
        return 0
    elif (n==1):
        return 1
    else:
        return fibrecur(n-1) + fibrecur(n-2)
    print(fibrecur(num))

#Iterative Method
def fibiter(n):
    a = 0
    b = 1
    if n > 1:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return c
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        print("Please enter a positive number")

if __name__ == '__main__':
    num = 9
    print("Number using recurssive method is: ", fibrecur(num))
    print("Number using Iterative method is: ", fibiter(num))
