class UnionFind:
    def __init__(self, size):
        self.parents = list(range(size))
    def union(self, parent, child):
        self.parents[self.find(child)] = self.find(parent)
    def find(self, child):
        if child != self.parents[child]:
            self.parents[child] = self.find(self.parents[child])
        return self.parents[child]
        

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:

        uf = UnionFind(len(accounts))

        ownership = {}

        for i in range(0, len(accounts)):
            cnt = 0
            for email in accounts[i]:
                if cnt == 0:
                    cnt += 1
                    continue
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i
        
        merged_accounts = collections.defaultdict(list)

        for email, owner in ownership.items():
            account_ind = uf.find(owner)
            merged_accounts[account_ind].append(email)
        
        return [ [accounts[i][0]] + sorted(email) for i, email in merged_accounts.items() ]