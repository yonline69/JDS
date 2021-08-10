def pipeline(*funcs):
    def helper(arg):
        for elem in funcs:
            arg = elem(arg)
        return arg
    return helper
    
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print('final result: ', fun(3))