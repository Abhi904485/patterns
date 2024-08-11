str1 = 'a'
str2 = "a"

def can_construct(ransom_str, magzene_str):
    hash_map = {}
    for i in magzene_str:
        if i in hash_map:
            hash_map[i] +=1
        else:
            hash_map[i] = 1
    for j in ransom_str:
        if j in hash_map and hash_map[j] > 0:
            hash_map[j] -=1
        else:
            return False
    else:
        return True
    


print(can_construct(ransom_str=str1, magzene_str=str2))