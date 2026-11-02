class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        if numCourses == 1:
            return [0]
        
        weight = {}
        adj = [ [] for i in range(0, numCourses + 1)]


        for pre in prerequisites:
            weight[pre[0]] = weight.get(pre[0], 0) + 1
            adj[pre[1]].append(pre[0])

        completed = deque()
        ret_list = []

        for i in range(0, numCourses):
            if weight.get(i, 0) == 0:
                completed.append(i)
        
        if len(completed) == 0:
            return []

        while completed:
            c = completed.popleft()
            ret_list.append(c)

            for ad in adj[c]:
                weight[ad] -= 1
                
                if weight[ad] == 0:
                    completed.append(ad)
        if len(ret_list) != numCourses:
            return []
        return ret_list

     

        