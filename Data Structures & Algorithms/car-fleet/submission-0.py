class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort()
        eta = []
        fleets = 0
        for pair in pairs:
            eta.append((target - pair[0]) / pair[1])
        while eta:
            curr = eta[-1]
            while eta and eta[-1] <= curr:
                eta.pop()
            fleets += 1

        return fleets
            
            #pop from stack, compute etas, when inner loop breaks increment fleets

