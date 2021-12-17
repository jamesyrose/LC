class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        secret_cnt = {}
        guess_cnt = {}

        bulls = 0
        cows = 0

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_cnt[s] = secret_cnt.get(s, 0) + 1
                guess_cnt[g] = guess_cnt.get(g, 0) + 1

        for k in guess_cnt.keys():
            if k in secret_cnt:
                cows += min(secret_cnt[k], guess_cnt[k])
        return f"{bulls}A{cows}B"


