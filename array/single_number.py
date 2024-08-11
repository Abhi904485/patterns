def single_number_using_hash_table(self, nums):
        hash_table = dict()
        for i in nums:
            if i not in hash_table:
                hash_table[i] = i
            else:
                hash_table[i] -= i
                if hash_table[i] == 0:
                    del hash_table[i]
        return list(hash_table.values())[0]


def singleNumber_using_xor(self, nums):
        xor = 0
        for i in nums:
            xor ^= i
        return xor