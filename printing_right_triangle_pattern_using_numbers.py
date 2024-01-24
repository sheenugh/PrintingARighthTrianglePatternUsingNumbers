

# ----- VISUALIZATION -----
# 1             1*2 - 1, 1 | 0, 1
# 2 2           2*2 - 2, 2 | 0, 1
# 3 3 3         3*2 - 3, 3 | 0, 1
# 4 4 4 4       4*2 - 4, 4 | 0, 1
# 5 5 5 5 5     5*2 - 5, 5 | 0, 1

# n or height = 5
# number of index = prev index/variable + 1 


# ----- FUNCTIONS -----
def right_triangle_using_num(height):
    for i in range(1, height+1):
        print((height - i), end= " ")
        print("1" * (i*2-1))
        
# PSEUDO CODES
# - Actual codes
right_triangle_using_num(5)