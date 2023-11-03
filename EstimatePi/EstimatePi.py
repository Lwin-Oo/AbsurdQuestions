#U have a function called Random which generates the number from 0 to 1 randomly and uniformly distributed.
#Calculate the number Pi.


from cmath import sqrt
import random
#from turtle import distance


def estimate_pi(n):
    num_points_circle = 0
    num_points_total = 0
    for _ in range (n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2
        if distance <= 1:
            num_points_circle += 1
        num_points_total += 1    

    return 4 * num_points_circle / num_points_total        

result = estimate_pi(10000000)
print("Estimated value of π:", result)