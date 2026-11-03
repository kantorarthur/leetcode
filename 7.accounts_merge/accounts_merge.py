class UnionFind:
    def __init__(self, n) -> None:
        self.parents = list(range(n))
    def union(self, child, parent) -> None:
        self.parents[self.find(child)] = self.find(parent)
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:

        union_find = UnionFind(len(accounts))

        ownership = {}

        for i in range(0, len(accounts)):
            cnt = 0
            for email in accounts[i]:
                if cnt == 0:
                    cnt += 1
                    continue
                if email in ownership:
                    union_find.union(i, ownership[email])
                ownership[email] = i
        
        owners = collections.defaultdict(list)
        for email, owner in ownership.items():
            owners[union_find.find(owner)].append(email)
        
        return [ [accounts[i][0]] + sorted(emails) for i, emails in owners.items() ]