# Day 17
## Reflection
  I actually just had a 2 day break because I attended the funeral of my lola's sister. Anyway, I started today by completing day 19 of 100 Days of Python. This section delves more about turtle graphics, event listeners and also state and multiple instances. I actually learned alot on this Day like functions as inputs which is a concept I am not familiar yet.

  This section has two final projects, the first one is an etch-a-sketch app using turtle graphics and the second one is a turtle race betting app.

  Here is how I did the etch-a-sketch app:
  1. Import Turtle and Screen from the turtle module
  2. Create a Turtle and Screen object
  3. Create functions move_forward, move_backward, turn_left, turn_right
  4. Make the screen listen by using the listen() function
  5. Add keylisteners for letters w, a, s, d where the keylisterner for w will call the move_forward function, s will call the move_backward function, a for turn_left and d for turn_right
  6. Create a function called clear_drawing that uses the clear function of turtle to clear the drawings, the penup so that it doesn't draw when the turtle is move, the home function to make the turtle return to its default position.
  7. Since, the letters are case-sensitive, create the same kind of keylistener that the lowercase have for its uppercase.
  
  Here is how I did the turtle race betting app:
  1. Import Turtle and Screen from the turtle module
  2. Create a Turtle and Screen object
  3. Create a variable named left_edge and the right_edge that is calculated using screen.width_size/2
  4. Create the six turtles for the different colors
  5. Move the turtles to their starting position with left edge as the x position and the y position is 50 units apart from each other6
  6. Create a function to start the race called start race
  7. On the start_race function, create a while loop
  8. On the while loop, use the turtle's forward function to move the turtles but used the randomint() function of the random module to randomized the units it will move forward
  9. Create an if statement to check if someone reached the right_edge
  10. When a turtle whens, we will break the while loop and call the declare_winner function and just 


  Conclusion


## Progress
 - Completed Day 19 of 100 Days of Python
 - Completed Collection Types Section of Python Intermediate on Sololearn
