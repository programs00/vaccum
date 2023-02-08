import random

m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))
room = [[1 for i in range(m)] for j in range(n)]
print("Initailly all room are dirty")
print(room)
x = 0
y = 0

while x < n:
	while y < m:
		 room[x][y] = random.choice([0,1])
		 y += 1
	x += 1
	y = 0
print("Before cleaning the room")
print(room)
x = 0
y = 0
z = 0

while x < n:
	while y < m:
		if room[x][y] == 1:
			print("vacuum cleaner is in position ", x, y)
			room[x][y] = 0
			print("cleaned position ", x, y)
			z +=1
		y +=1
	x +=1
	y = 0
pro = (100 - ((z/(m*n))*100))
print("Room is cleaned completely now!!")
print(room)
print (z)
print("Performance = ", pro ,"%")

