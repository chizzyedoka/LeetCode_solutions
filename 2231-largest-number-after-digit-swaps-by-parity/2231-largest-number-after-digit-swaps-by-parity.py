class Solution:
    def largestInteger(self, num: int) -> int:
		# Convert the number into a list of digits
        digits=[int(digit) for digit in str(num)]

		# Separate even and odd digits into two lists
        even = []
        odd = []
        for digit in digits:
            if digit % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)

        # Sort both lists in descending order
        even.sort(reverse=True)
        odd.sort(reverse=True)

        # Reconstruct the number using the sorted even and odd digits
        ans = []
        for digit in digits:
            if digit % 2 == 0:
                ans.append(even.pop(0))
            else:
                ans.append(odd.pop(0))

        # Convert the list back to an integer and return it
        ans = int(''.join(map(str, ans)))

        return ans
