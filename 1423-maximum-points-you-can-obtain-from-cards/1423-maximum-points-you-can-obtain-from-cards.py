# class Solution:
#     def maxScore(self, cardPoints: List[int], k: int) -> int:
#         frontSetofCards = cardPoints[0:k]
#         rearSetofCards = cardPoints[-1 : -k - 1 : -1 ]
#         current_sum, sumFront, sumRear = 0,0,0
#         for i in range(k):
#             sumFront += frontSetofCards[i]
#             sumRear += rearSetofCards[i]
#         maxSum = 0
#         for i in range(k):
#             current_sum = frontSetofCards[i] + sum(rearSetofCards[i:k-i])
#             print(current_sum)
#             maxSum = max(current_sum,maxSum)
#         return maxSum
#         # def sum_from_left(cardPoints,k):
#         #     left_sum = 0
#         #     for i in range(k):
#         #         left_sum += cardPoints[i]
#         #     return left_sum
#         # def sum_from_right(cardPoints,k):
#         #     right_sum = 0
#         #     j = len(cardPoints) - 1
#         #     while j > len(cardPoints) - k-1:
#         #         right_sum += cardPoints[j]
#         #         j -= 1
#         #     return right_sum
#         # left_sum = sum_from_left(cardPoints,k) 
#         # right_sum = sum_from_right(cardPoints,k)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        s = sum(cardPoints[-k:])
        maximum = s
        j = length-k
        i=0
        while i!=j and j<length:
            s+=cardPoints[i]
            s-=cardPoints[j]
            i+=1
            j+=1
            maximum = max(s,maximum)
        return maximum
      
        