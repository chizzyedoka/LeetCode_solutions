class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        entries = defaultdict(list) # { person: [time, amount, city } 
        invalidIdx = set()

        for idx, transaction in enumerate(transactions):
            person, time, amount, city = transaction.split(',')
            if int(amount) > 1000:
                invalidIdx.add(idx)
            entries[person].append((time, amount, city, idx))

        # now check for trans in different cities and within 60 mins
        for person, entry in entries.items():
            for i in range(len(entry)):
                time, amount, city, idx1 = entry[i]
                for j in range(i+1,len(entry)):
                    _time, _amount, _city, idx2 = entry[j]
                    if city != _city and abs(int(time) - int(_time))  <= 60:
                        invalidIdx.add(idx1)
                        invalidIdx.add(idx2)
        return [transactions[i] for i in list(invalidIdx)]










