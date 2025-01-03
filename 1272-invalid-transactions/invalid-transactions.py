class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        #same transaction can have different index/seq but can have same value
        idx = set()
        d = defaultdict(list)
        #loop through transaction
        for i, tran in enumerate(transactions):
            name,time,amount,city = tran.split(',')
            d[name].append((time,amount,city,i))
        #check if amount > 1000
            if int(amount)>1000:
                idx.add(i)
        # add transaction to answer list if not added before
            for cur_time,cur_amount,cur_city,cur_i in d[name]:
        #compare with transactions associated with same name ->  dictionary
                if cur_city!=city and abs(int(cur_time)-int(time))<=60:
        # add transactions to answer list if not added before
                    idx.add(cur_i)
                    idx.add(i)
        # return transaction
        return [transactions[i] for i in idx]
