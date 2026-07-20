class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a set which in this case is notepad
        notepad = set()

        for num in nums: #check per iteration in the list
            if num in notepad: #if the number is in the notepad
                return True #return True
            else:
                notepad.add(num) #if not yet in the notepad, add it to the notepad set

        return False #else return False
