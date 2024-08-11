def convert_list_to_string(b: list):
    localstring = ""
    for i in b:
        localstring += i
    return localstring


def convert_string_to_list(b: str):
    locallist = []
    for i in b:
        locallist.append(i)
    return locallist


def mysplit(inputString: str, separator: str):
    listFromInputString = convert_string_to_list(inputString)
    part = []
    result = []
    j = 0
    for i in range(0, len(listFromInputString)):
        if listFromInputString[i] == separator:
            part = listFromInputString[j:i]
            j = i+1
            result.append(convert_list_to_string(part))
    if j != 0:
        result.append(convert_list_to_string(listFromInputString[j:]))
    if len(result) == 0:
        result.append(inputString)
    return result


print(mysplit("deesdfedefddfssd", "d"))
