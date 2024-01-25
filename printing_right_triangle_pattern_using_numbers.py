

# ----- VISUALIZATION -----
# 1                         1*2 - 1, 1 | 0, 4 --> #height-i | 0 spaces on the left, 4 spaces on the right
# 2 2                       2*2 - 1, 3 | 0, 3 --> #height-i | 0 spaces on the left, 3 spaces on the right
# 3 3 3                     3*2 - 1, 5 | 0, 2 --> #height-i | 0 spaces on the left, 2 spaces on the right
# 4 4 4 4                   4*2 - 1, 7 | 0, 1 --> #height-i | 0 spaces on the left, 1 spaces on the right
# 5 5 5 5 5                 5*2 - 1, 9 | 0, 0 --> #height-i | 0 spaces on the left, 0 spaces on the right

# n or height = 5
# number of index = prev index/variable + 1 


# ----- FUNCTIONS -----
def right_triangle_using_num(height):
    for i in range(0, height):
        print((str(i)+ " ") * ((i*1)-0), end= " ")
        print(" " * (height - i))

# PSEUDO CODES
# - Actual codes
# - Calling the function
right_triangle_using_num(6)


        
        
        
