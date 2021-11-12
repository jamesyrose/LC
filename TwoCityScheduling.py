class Solution:
    def twoCitySchedCost(self, costs: list) -> int:
        costs = sorted(costs, key=lambda x: x[0] -x[1])
        total = 0
        for i in range(len(costs) //2):
            total += costs[i][0]
            total += costs[-i - 1 ][1]
        return total




if __name__ == "__main__":
    nums = costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
    ans = 1859
    resp = Solution().twoCitySchedCost(nums)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

