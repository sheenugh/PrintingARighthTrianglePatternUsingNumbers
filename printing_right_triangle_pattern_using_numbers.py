

# ----- VISUALIZATION -----
# 1                         1*2 - 1, 1 | 0, 2 --> #height*2-1 | 0 spaces on the left, 2 spaces on the right
# 2 2 2                     2*2 - 2, 2 | 0, 2 --> #height*2-2 | 0 spaces on the left, 2 spaces on the right
# 3 3 3 3 3                 3*2 - 3, 3 | 0, 2 --> #height*2-3 | 0 spaces on the left, 2 spaces on the right
# 4 4 4 4 4 4 4             4*2 - 4, 4 | 0, 2 --> #height*2-4 | 0 spaces on the left, 2 spaces on the right
# 5 5 5 5 5 5 5 5 5         5*2 - 5, 5 | 0, 2 --> #height*2-5 | 0 spaces on the left, 2 spaces on the right

# n or height = 5
# number of index = prev index/variable + 1 


# ----- FUNCTIONS -----
def right_triangle_using_num(height):
    for i in range(1, height+1):
        print((str(i)+ " ") * (i*2-1), end= " ")
        print(" " * (height - i))

# PSEUDO CODES
# - Actual codes
# - Calling the function
right_triangle_using_num(5)

        
        
        
        
