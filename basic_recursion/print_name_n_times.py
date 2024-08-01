def print_name_n_times(n):
    if not n:
        return
    print("Abhishek")
    print_name_n_times(n-1)



n = 4
print_name_n_times(4)