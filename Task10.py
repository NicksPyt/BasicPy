blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
height = 0
layer = 0
while blocks > height:
    layer = layer + 1
    blocks = blocks - layer
    height = height + 1 
#	

print("The height of the pyramid:", height)
