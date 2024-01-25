

#----- VISUALIZATION -----
# 1                         1*1 - 0, 1 | 0, 4 --> #height-i | 0 spaces on the left, 4 spaces on the right
# 2 2                       2*1 - 0, 2 | 0, 3 --> #height-i | 0 spaces on the left, 3 spaces on the right
# 3 3 3                     3*1 - 0, 3 | 0, 2 --> #height-i | 0 spaces on the left, 2 spaces on the right
# 4 4 4 4                   4*1 - 0, 4 | 0, 1 --> #height-i | 0 spaces on the left, 1 spaces on the right
# 5 5 5 5 5                 5*1 - 0, 5 | 0, 0 --> #height-i | 0 spaces on the left, 0 spaces on the right

# n or height = 5
# number of index = prev index/variable + 1 


# ----- FUNCTIONS -----
# - This section is for the def function in executing the right triangle pattern
def right_triangle_using_num(height):
    for i in range(0, height):
        print((str(i)+ " ") * ((i*1)-0), end= " ")
        print(" " * (height - i))

#>>>>>>>>>> PSEUDO CODE <<<<<<<<<<
#----- ACTUAL CODES -----
# - Caller of the def function
right_triangle_using_num(6)


        
        
        
