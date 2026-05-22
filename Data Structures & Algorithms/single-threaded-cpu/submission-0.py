import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #need to add indexes to tasks
        for i, task in enumerate(tasks):
            task.append(i)
        tasks.sort(reverse=True)

        order = []
        time = 0
        heap = []

        #keep track of time independently, enqueue based on time
        #heappify based on processing time > index
        while tasks or heap:
            if not heap:
                time = max(time, tasks[-1][0])
            while tasks and tasks[-1][0] <= time:
                enq, proc, idx = tasks.pop()
                heapq.heappush(heap, (proc, idx))

            proc, idx = heapq.heappop(heap)
            time += proc
            order.append(idx)
        return order


        
            
        