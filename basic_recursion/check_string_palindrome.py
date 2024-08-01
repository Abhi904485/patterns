def check_string_palindrome_bf(string):
    result = ""
    for i in string:
        result +=i
    return result == string

def check_string_palindrome_slicing(string):
    return string == string[::-1]


def check_string_palindrome_using_two_pointer(string):
    n = len(string)
    for i in range(n//2):
        if string[i] != string[n-i-1]:
            return False
    else:
        return True
    
def check_string_palindrome_using_functional_recursion(string):
    if len(string) == 1:
        return string
    return check_string_palindrome_using_functional_recursion(string[1:])+string[0:1]

def check_string_palindrome_using_parametrized_recursion(string, i):
    if i > len(string)//2:
        return True
    if string[i] != string[len(string)-i-1]:
        return False
    return check_string_palindrome_using_parametrized_recursion(string, i+1)
    
def check_string_palindrome_using_builtin(string):
    return "".join(reversed(string)) == string

print(check_string_palindrome_bf("ABCDCBA"))
print(check_string_palindrome_slicing("ABCDCBA"))
print(check_string_palindrome_using_two_pointer("ABCDCBA"))
print(check_string_palindrome_using_builtin("ABCDCBA"))
print("ABCDCBA" == check_string_palindrome_using_functional_recursion("ABCDCBA"))
print(check_string_palindrome_using_parametrized_recursion("ABCDCBA", 0))