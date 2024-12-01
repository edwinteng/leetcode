class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        ans = set()
        d = {}
        anslist = list()
        for i in range(len(transactions)):
            name,time_str,amount_str,city = transactions[i].split(',')
            time,amount = int(time_str),int(amount_str)
            if amount>1000:
                ans.add(i)
            if name not in d:
                d[name]=list() 
            d[name].append([int(time),city,i])
            #print(d[name])
            for othertime,othercity,otheri in d[name]:
                if otheri!=i and abs(time-othertime)<=60 and city!=othercity:
                    ans.add(otheri) 
                    ans.add(i)


        return [transactions[i] for i in ans]