class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pref = [1] * n
        suff = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]

        # Calculate suffix products
        for j in range(n-2, -1, -1):
            suff[j] = suff[j+1] * nums[j+1]

        # Multiply prefix and suffix
        output = [0] * n

        for i in range(n):
            output[i] = pref[i] * suff[i]

        return output
            