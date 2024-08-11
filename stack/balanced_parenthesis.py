from collections import deque


def balanced_parenthesis(x):
    stack = deque()
    hash_map = {
        "{": 1,
        "(": 2,
        "[": 3,
        "}": -1,
        ")": -2,
        "]": -3
    }
    for i in x:
        if i == '{' or i == '(' or i == '[':
            stack.append(i)
        else:
            if stack:
                top = stack.pop()
                if hash_map[top] + hash_map[i] == 0:
                    continue
                else:
                    return False
            else:
                return False
    else:
        if stack:
            return False
        return True


print(balanced_parenthesis(")"))
