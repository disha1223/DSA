def sumR(n,i=1):
    if n==1:
        return 1
    else:
        return n+sumR(n-1)

if __name__=="__main__":
    n=int(input("Enter Your Number:"))
    print(sumR(n))