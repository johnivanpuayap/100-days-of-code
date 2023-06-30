# Day 17
## Reflection
  I just had a 2-day break because I attended my Lola's sister's funeral. Nonetheless, I started today by completing Day 19 of the 100 Days of Python challenge. This section delves more into turtle graphics, event listeners, and working with state and multiple instances. I learned a lot today, particularly about functions as inputs, which is a concept I wasn't familiar with before.

  This section has two final projects, the first one is an etch-a-sketch app using turtle graphics and the second one is a turtle race betting app.

  Here's how I implemented the Etch-a-Sketch app:

  1. Imported the Turtle and Screen modules from the turtle module.
  2. Created Turtle and Screen objects.
  3. Defined functions for moving the turtle forward, moving it backward, turning left, and turning right.
  4. Made the screen listen for key events using the listen() function.
  5. Added key listeners for the letters 'w', 'a', 's', and 'd', where 'w' triggers the move_forward function, 's' triggers the move_backward function, 'a' triggers the turn_left function, and 'd' triggers the turn_right function.
  6. Created a function called clear_drawing that uses the turtle's clear() function to clear the drawings, sets the pen to the up position to prevent drawing, and returns the turtle to its default position using the home() function.
  7. Since the key listeners are case-sensitive, I added additional key listeners for the uppercase versions of the lowercase letters.
  
  For the turtle race betting app, I followed these steps:

  1. Imported the Turtle and Screen modules from the turtle module.
  2. Created Turtle and Screen objects.
  3. Defined variables named left_edge and right_edge, with right_edge calculated as half of the screen width using screen.width_size/2.
  4. Created a function named create_turtles that generates turtles and returns a list of turtles.
  5. Created a function named start_race to initiate the race.
  6. Inside the start_race function, positioned the turtles at their starting positions with the left_edge as the x position and spaced them 50 units apart on the y-axis.
  7. Implemented a while loop.
  8. Inside the while loop, used the turtle's forward function to move the turtles, with the number of units randomized using the random.randint() function from the random module.
  9. Added an if statement to check if any turtle has reached or go beyond the right_edge.
  10. If a turtle wins, the while loop is broken, and the declare_winner function is called with the winning turtle's color as an argument.
  11. Defined the declare_winner function to print the winner using an f-string.
  12. Added a prompt using textinput to ask the user who they think will win.
  13. Modified the declare_winner function to compare the user's bet with the winner and stored the result in a variable called result.
  14. Modified the f-string to also display the result variable.
  15. Implemented error handling to only proceed if the user's input is a valid color.
  16. Added a title on the Screen
  17. Added docstrings to functions for improved code documentation.

  After that, I finished the day by completing the collecting types module of the Python Intermediate course. I studied about sets and list comprehensions. I also learned alot on this lessons like on the list comprehension but still theree are some parts that was not covered in the course that I was curious about, so what I did was also get some research about it like the difference between sets, dictionaries and lists, operations in sets, etc. The last part of the module was the quiz, which was not that hard and I was able to pass it.

  
  Conclusion
  
  

## Progress
 - Completed Day 19 of 100 Days of Python
 - Completed Collection Types Module of Python Intermediate on Sololearn
