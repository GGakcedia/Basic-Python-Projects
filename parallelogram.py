def right_slash(piece):
    for i in range(int(piece)):
        print("/", end="")

def left_slash(piece):
    for i in range(int(piece)):
        print("\\", end="")

def skip_line(piece):
    for i in range(int(piece)):
        print()

def space(piece):
    for i in range(int(piece)):
        print(" ", end="")         

def upside(diameter):
   startspace = diameter/2-1
   for i in range (int(diameter/2)):
       space(startspace-i)
       right_slash(1)
       space(i*2)
       left_slash(1)
       skip_line(1)

def under_part(diameter):
   startspace = diameter-2
   for i in range (int(diameter/2)):
       space(i)
       left_slash(1)
       space(startspace - i*2)
       right_slash(1)
       skip_line(1)

def parallelogram(diameter):
    upside(diameter)
    under_part(diameter)         

diameter_value = int(input("Enter a diameter value:"))
parallelogram(diameter_value)