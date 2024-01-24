

# ----- VISUALIZATION -----
# 1                         1*2 - 1, 1 | 0, 2
# 2 2 2                     2*2 - 1, 2 | 0, 2
# 3 3 3 3 3                 3*2 - 1, 3 | 0, 2
# 4 4 4 4 4 4 4             4*2 - 1, 4 | 0, 2
# 5 5 5 5 5 5 5 5 5         5*2 - 1, 5 | 0, 2

# n or height = 5
# number of index = prev index/variable + 1 


# ----- FUNCTIONS -----
def right_triangle_using_num(height):
    for i in range(1, height+1):
        print((str(i)+ " ") * (i*2-1), end= " ")
        print(" " * (height - i))

right_triangle_using_num(5)
    
        # print("2" * (i*2-1), end= " ")
        # print(" " * (height - i))
        
        
        
        
# PSEUDO CODES
# - Actual codes
