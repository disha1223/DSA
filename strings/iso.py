class Solution:
    def isomorphicString(self, s: str, t: str) -> bool:

        map1 = {}
        map2 = {}

        for c1, c2 in zip(s, t):

            if c1 in map1:
                if map1[c1] != c2:
                    return False
            else:
                map1[c1] = c2

            if c2 in map2:
                if map2[c2] != c1:
                    return False
            else:
                map2[c2] = c1

        return True