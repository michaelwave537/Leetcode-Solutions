class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        # sol = 0
        # basket = []
        # cost.sort(reverse=True)
        # if len(cost) >= 3:
        #     for i in range(len(cost)):
        #         if len(basket) == 2:
        #             sol += basket[0] + basket[1]
        #             basket = []
        #             continue
        #         if len(basket) != 2:
        #             basket.append(cost[i])
        #             print(basket)

        #     for price in basket:
        #         sol += price
        # else:
        #     for price in cost:
        #         sol += price
        

        # return sol

        cost.sort(reverse=True)
        sol = 0
        for i in range(len(cost)):
            if i % 3 != 2:
                sol += cost[i]
        return sol