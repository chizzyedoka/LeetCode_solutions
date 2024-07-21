class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        d = {}
        res=""
        for vote in votes:
            for i,char in enumerate(vote):
                if char not in d:
                    d[char] = [0] * len(vote)
                d[char][i] += 1
        sorted_d = sorted(d.items(), key=lambda x:( x[1], -ord(x[0])), reverse=True)
        for item in sorted_d:
            res+= item[0]
        return res