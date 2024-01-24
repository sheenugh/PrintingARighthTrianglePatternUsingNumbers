def right_triangle_using_num(height):
    for i in range(1, height+1):
        print((str(i) + " ") * (i*2-1), end="")
        print(" " * (height - i))

right_triangle_using_num(5)