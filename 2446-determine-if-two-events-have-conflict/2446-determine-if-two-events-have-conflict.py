class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        s1,e1 = event1[0], event1[1]
        s2,e2 = event2[0], event2[1]
        if s2<=e1 and e2>= s1:
            return True
        return False
        
        