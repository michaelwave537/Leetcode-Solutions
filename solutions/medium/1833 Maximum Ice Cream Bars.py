class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if coins < costs[0]:
            return 0
        
        total = 0
        for cost in costs:
            if coins >= cost:
                coins -= cost
                total += 1
            else:
                return total
        
        return total