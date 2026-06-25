def iseven(n):
    if n%2 ==0:
        return True
    else:
        return False

if __name__=="__main__":
    n=int(input("Enter Your Number:"))
if iseven(n):
    print("even")
else:
    print("odd")