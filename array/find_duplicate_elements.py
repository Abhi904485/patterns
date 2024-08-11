def contains_duplicate(self, nums):
        return not len(set(nums)) == len(nums)

def contains_duplicate_using_hash(self, nums):
        hash_table = dict()
        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table[i] += 1
        for i in hash_table.values():
            if i >= 2:
                return True
        else:
            return False
        
def contains_duplicate_bf(self, nums):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        else:
            return False