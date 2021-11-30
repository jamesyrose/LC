import collections


class Solution:
    def leastInterval(self, tasks: list, n: int) -> int:
        if n == 0:
            return len(tasks)

        idle = collections.deque(maxlen=n)
        task = {}
        for t in tasks:
            task[t] = task.get(t, 0) + 1
        cnt = 0
        res = 0
        while cnt < len(tasks):
            # find max_key and add it to idle for cool down
            res += 1
            if task:
                max_key = max(task, key=task.get)
                if len(idle) == n:
                    tmp = idle.popleft()
                    if tmp[1] > 0 and tmp[1] != "idle":
                        task[tmp[0]] = tmp[1]
                idle.append([max_key, task[max_key] - 1])
                cnt += 1
                del task[max_key]
            else:
                tmp = idle.popleft()
                if tmp[1] > 0 and tmp[1] != "idle":
                    task[tmp[0]] = tmp[1]
                idle.append(["idle", 0])
                max_key = "idle"
            print(res, cnt, max_key, task, idle)
        return res



if __name__ == "__main__":
    nums = ["A","A","A","B","B","B"]
    n = 10
    ans = 10
    resp = Solution().leastInterval(nums, n)
    if ans == resp:
        print("PASS", resp)
    else:
        print("FAIL", resp)

