def sum(n,i=1):
    s=0
    while i<=n:
        s=s+i
        i+=1
    return s
    
if __name__=="__main__":
    n=int(input("Enter Your Number:"))
    print(sum(n))