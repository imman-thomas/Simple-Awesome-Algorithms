
def Insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while (i >=0) and (A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A



def main():
    x = []
    n = int(input("Enter the Total number of Elements"))
    for i in range(1,n):
        e = input("Enter element :")
        x.append(e)
    print("The entered Elements are :")
    print(x)
    print("The sorted Elements are:")
    print(Insertion_sort(x))

if __name__ == "__main__":
    main()
