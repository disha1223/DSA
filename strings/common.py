def longest(self,str):
    ans=""
    for i in range(len(str[0])):
        for word in str:
            if i==len(word) or word[i]!=str[0][i]:
                return ans
        ans+=str[0][i]
    return ans