def mul(n,i=1):
    if i==11:
        return 
    print(n,"*",i,"=",n*i)
    i+=1
    mul(n,i)

if __name__=="__main__":
    n=int(input("Enter Your Number:"))
    mul(n)
