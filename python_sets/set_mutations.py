#https://www.hackerrank.com/challenges/py-set-mutations/problem

set_len = int(input())
init_set = set(map(int, input().split(' ')))

num_of_mut = int(input())

def do_mut_op(operation, new_set):
    # since we are assigning a new set to the variable 'init_set',
    # we need to explicitly declare that the 'init_set' to be used
    # in this function scope is the global 'init_set' defined outside 
    # of the function's local scope
    global init_set
    
    if operation == 'update':
        # equivalent to s.update(new_set)
        init_set |= new_set
        
    elif operation == 'intersection_update':
        # equivalent to s.intersection_update(new_set)
        init_set &= new_set
        
    elif operation == 'difference_update':
        # equivalent to s.difference_update(new_set)
        init_set -= new_set
        
    elif operation == 'symmetric_difference_update':
        # equivalent to s.symmetric_difference_update(new_set)
        init_set ^= new_set
        
    return init_set
    
for i in range(num_of_mut):
    do_mut_op(input().split(' ')[0], set(map(int, input().split(' '))))
    
print(sum(init_set))