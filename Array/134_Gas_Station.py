def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    match sum(gas) < sum(cost):
        case True:
            return -1
        case False:
            if len(gas) == 1:
                return 0
            cum_sum = gas[0]-cost[0]
            min_sum = cum_sum
            ind = 1
            for i in range(1, len(gas)):
                cum_sum += gas[i]-cost[i]
                if cum_sum < min_sum:
                    min_sum = cum_sum
                    ind = i+1 if min_sum < 0 else 0

            return ind


gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

gas = [3, 1, 1]
cost = [1, 2, 2]

gas = [1, 2]
cost = [2, 1]
print(canCompleteCircuit(gas, cost))
