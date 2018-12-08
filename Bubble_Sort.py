def  Bubble_Sort(A):

    for num in range(len(A)-1,0,-1):
        for i in range(num):
            if A[i]> A[i+1]:
                temp = A[i]
                A[i]= A[i+1]
                A[i+1] = temp
    return A


def main():
    print("Bubble Sort:")
    x = []
    n = int(input("Enter the Total number of Elements"))
    for i in range(n):
        e = input("Enter element :")
        x.append(e)
    print("The entered Elements are :")
    print(x)
    print("The sorted Elements are:")
    print(Bubble_Sort(x))

if __name__ == "__main__":
    main()
