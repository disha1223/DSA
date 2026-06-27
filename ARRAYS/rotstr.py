#rotate string 
class solution:#26/06/2026
    def rotstr(self,s,goal):
        if len(s)!=len(goal):
            return False
        for i in range(len(s)):
            s=s[1:]+s[0]
            if s==goal:
                return True
        return False