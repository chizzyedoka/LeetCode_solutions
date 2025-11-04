class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()
        invalidIdx = set()
        person_transaction_map = {}

        for  i, entry in enumerate(transactions):
            if int(entry.split(",")[2]) > 1000:
                invalid.add(entry)
                invalidIdx.add(i)

        for i, transaction in enumerate(transactions):
            (name, time, amount, city) = transaction.split(",")
            if name not in person_transaction_map:
                person_transaction_map[name] = []
            person_transaction_map[name].append((city, int(time), amount, i))

        for name, transaction in person_transaction_map.items():
            for i in range(len(transaction)):
                (city1,time1, amount1, idx1) = transaction[i]
                for j in range(i+1,len(transaction)):
                    (city2, time2, amount2, idx2) = transaction[j]
                    if abs(time2 - time1) <= 60 and city1 != city2:
                        invalid.add(f"{name},{time2},{amount2},{city2}")
                        invalid.add(f"{name},{time1},{amount1},{city1}")
                        invalidIdx.add(idx1)
                        invalidIdx.add(idx2)

        return [transactions[i] for i in invalidIdx]