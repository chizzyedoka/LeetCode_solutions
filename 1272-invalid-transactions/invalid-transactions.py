class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        entries = defaultdict(list) # { person: [time, amount, city } 
        invalidIdx = set()

        for idx, transaction in enumerate(transactions):
            person, time, amount, city = transaction.split(',')
            if int(amount) > 1000:
                invalidIdx.add(idx)
            else:
                entries[person].append((time, amount, city, transaction, idx))

        #print(entries)

        # now check for trans in different cities and within 60 mins
        for person, entry in entries.items():
            for i in range(len(entry)):
                print(entry[i])
                time, amount, city, idx1 = entry[i]
                for j in range(i+1,len(entry)):
                    _time, _amount, _city, idx2 = entry[j]
                    if city != _city and abs(int(time) - int(_time))  <= 60:
                        invalidIdx.add(i)
                        invalidIdx.add(j)
        print(invalidIdx)
        return [transactions[i] for i in list(invalidIdx)]

from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        entries = defaultdict(list)  # { person: [(time, amount, city, idx)] }
        invalidIndexes = set()

        # Step 1: parse and store all
        for idx, transaction in enumerate(transactions):
            person, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)

            if amount > 1000:
                invalidIndexes.add(idx)

            # ✅ always store in entries, even if amount > 1000
            entries[person].append((time, amount, city, idx))

        # Step 2: check for city conflict within 60 minutes
        for person, entry in entries.items():
            for i in range(len(entry)):
                time, amount, city, idx1 = entry[i]
                for j in range(i + 1, len(entry)):
                    _time, _amount, _city, idx2 = entry[j]
                    if city != _city and abs(time - _time) <= 60:
                        invalidIndexes.add(idx1)
                        invalidIndexes.add(idx2)

        # Step 3: collect invalids in original order
        return [transactions[i] for i in range(len(transactions)) if i in invalidIndexes]




