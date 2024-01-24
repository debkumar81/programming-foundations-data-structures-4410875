def find_second_smallest(my_list):
    n = len(my_list)
    if n==0 or n==1:
        return None
    smallest=float('inf')
    second_smallest=float('inf')
    for i in my_list:
        if i>smallest and i<second_smallest:
            second_smallest=i
        elif i <smallest:
            second_smallest=smallest
            smallest=i
        
    return second_smallest

print(find_second_smallest([5, 8, 3, 2, 6]))
