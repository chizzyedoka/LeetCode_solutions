class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactionsByPerson = {}
        invalidTransactions = set()
        for  index, transaction in enumerate(transactions):
            person, time, amount, city = transaction.split(",")
            if person not in transactionsByPerson:
                transactionsByPerson[person] = []
            transactionsByPerson[person].append((int(time), int(amount), city, index))    
        

        for person in transactionsByPerson:
            personTransactions = transactionsByPerson[person]
            for i in range(len(personTransactions)):
                # case 1: amount exceeds 1000
                if personTransactions[i][1] > 1000:
                    invalidTransactions.add(personTransactions[i][3])

                # case 2: same person,different city in 60mins or less
                for j in range(len(personTransactions)):
                    if i != j and personTransactions[i][2] != personTransactions[j][2] and abs(personTransactions[i][0] - personTransactions[j][0]) <= 60 : # dont compare with self
                        invalidTransactions.add(personTransactions[i][3])
                        invalidTransactions.add(personTransactions[j][3])
                        

                

        print(invalidTransactions)
        return [transactions[i] for i in invalidTransactions]
            
