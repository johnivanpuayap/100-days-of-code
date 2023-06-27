# Day 16: Introduction to Turtle Graphics and Tuples 
## Reflection
  Today, I delved into Day 18 of the 100 Days of Python course, which introduced me to Turtle Graphics, reading documentation, using aliases, and tuples. This section was a bit unfamiliar to me, as I hadn't worked with Turtle Graphics before. However, my previous experience in reading documentation came in handy.

  The challenges presented were not easy, particularly challenge 4. It took me a while to realize that I needed to use the colormode function to generate random numbers within the color range. I also made the mistake of using the object instead of the module to access the colormode() function. 
  
  The final project of the day was called "Hirst Painting," and here's how I approached it:

  1. I started by installing the colorgram package using pip.
  2. I adjusted the file path in the extract function to ensure it worked correctly.
  3. I created a random_color function that returned a random color from the colorgram output.
  4. I instantiated a Turtle and Screen object, set the color and speed on the turtle, and set the colormode to 255 on the screen.
  5. I positioned the turtle at the top-left corner.
  6. I created a while loop that decreased the y-coordinate until it reached the bottom edge of the screen.
  7. Inside the outer loop, I created an inner loop that increased the x-coordinate until it reached the right edge of the screen.
  8. Within the inner loop, I used the dot method to draw a dot and set its color using the random_color function.
  9. Finally, I called exitonclick() on the screen to keep the drawing visible until the screen is clicked.

  This was actually a fun project, the hard part for me was making sure the colorgram works since I am not using Pycharm and trying to make the distance between the edges and the circles on both ends nearly equal and since the x and y coordinates is based on the center like a cartesian plane, i am actually not used to it anymore since I am used to 0,0 at the top right. 

  After that I also finished the Tuples part of the Python Intermediate certification. What I mainly learned is that values of tuples can't be change so can consider it like a final data structure.

  Conclusion
  
  Today, I completed the Day 18 section in the 100 Days of Python. With each passing day, the challenges and exercises become more demanding, requiring additional time and effort to tackle. Although the concepts introduced in Day 18 were unfamiliar to me, I pushed through and gained valuable experience in Turtle Graphics and working with tuples.

  With 84 more days remaining in the 100 Days of Python challenge, I am excited about the knowledge and skills I will acquire along the way. The challenges and obstacles encountered thus far have only fueled my determination to continue learning and growing as a Python developer.

## Progress
 - Completed Day 18 of 100 Days of Python
 - Finished Tuples and Tuples Unpacking lesson in Python Intermediate on Sololearn
