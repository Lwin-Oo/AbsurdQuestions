Question: U have a function called Random which generates the number from 0 to 1 randomly and uniformly distributed.
          Calculate the number Pi.

_____________________________________________________________________________________________________________________________________________________________________________________________

Random(x, y)
Range(0,1)

1.Draw a square of the area of ( 1 + 1 ) ^ 2.
2.Put as many dots as u can in the sqaure.
3.Draw a circle with the radius of 1.
 
Now pay attention only to the 1st quadrant of the graph (+, +)

4.Pick up a random dot from the square.P(x , y)
5.Draw a line from that point to the origin(0 , 0).
	The distant between P and origin:
	d = sqt(x^2 + y^2)

THE LOGIC!! 

If d < r:
	the dot is inside of the circle.
If d > r:
	the dot is outsise of the circle.

Now we know how many dots lie inside of the circle and how many of them are outside of the circle ( inside the square ).

THE LOGIC:

Number of dots in circle / Number of dots in square =~ area of the circle / area of square => pi(r^2) / (2.r)^2 . 

Since the definition of Pi in the circle states that Pi is the ratio of the circumference of the circle to its diameter,
Pi value should be equivalent with the ratio we got.