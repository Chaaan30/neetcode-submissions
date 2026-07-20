class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        notepad = {}
        #i is indices [0,1,2,3]
        #nums [3,4,5,6], target = 7 should be [0,1] because 0 is 3 then 1 is 4 which is = to 7

        for i, num in enumerate(nums):
            partner = target - num
            #if we have the target, subtract to the current num to get the right partner
            #example 7 - 3 = 4 meaning target - num = partner

            if partner in notepad:
                return [notepad[partner], i]

            if partner not in notepad:
                notepad[num] = i