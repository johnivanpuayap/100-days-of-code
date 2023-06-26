# Day 15: Coming Back From Vacation
## Reflection
  Today marked my return to learning after a refreshing vacation. Honestly, it was a struggle to regain momentum and find the energy to start. However, I simply turned on my computer and allowed myself to embrace a period of idleness until my curiosity sparked and propelled me forward. Once I initiated my learning session, the journey became smooth sailing, and my motivation was reignited.

  To begin, I revisited the Python Intermediate Course on Sololearn, focusing on the topic of dictionaries. Since I had already covered dictionaries on Day 9, it served as a valuable review of my knowledge. During this review, I encountered a key insight: dictionaries only accept immutable objects as keys. Additionally, I learned that the get() function in dictionaries retrieves the value associated with a given key, and if the key is not found, it returns a specified default value.

  Subsequently, I delved into Day 16 of the 100 Days of Python challenge, which delved into Object-Oriented Programming (OOP) in Python. Thanks to my prior experience and certification in Java OOP, which was a mandatory course at my school, I possessed a solid foundation in OOP principles. Furthermore, I explored Python packages and familiarized myself with PyPi, a comprehensive repository of software for the Python programming language. Additionally, I acquired the knowledge to utilize the pip package manager in both the command line and Pycharm. The culmination of this section mirrored Day 15, as I revisited the Coffee Machine project, this time implementing it with an OOP approach.

  Here is a breakdown of my approach to the project:

  1. Imported the necessary classes: Menu, MenuItem, CoffeeMaker, and MoneyMachine.
  2. Created instances of Menu, CoffeeMaker, and MoneyMachine.
  3. Established a while loop that continues until the user inputs "off".
  4. Within the loop, prompted the user for their choice and employed conditional statements to handle different scenarios.
  5. If the choice is "off", the program is exited.
  6. If the choice is "report", I called the report methods of the CoffeeMaker and MoneyMachine classes to generate relevant reports.
  7. For other choices, I utilized the Menu's find_drink() method to determine if the requested drink is available.
  8. Ensured the drink is a MenuItem by performing a type check, disregarding it otherwise.
  9. If the drink is a valid MenuItem, I verified if sufficient resources were available using the CoffeeMaker's is_resource_sufficient() method, and then utilized the MoneyMachine's make_payment() method to handle payment and calculate the sufficiency of funds.
  10. If both conditions were met, the ordered menu item was prepared; otherwise, no action was taken.

  Since I completed the project ahead of schedule, I decided to undertake Day 17 as well, which continued the exploration of OOP. This particular section centered on creating classes. While the syntax differed significantly from what I was accustomed to, I dedicated time to familiarize myself with it and practiced extensively in creating Python classes. Although the syntax remained a slight concern, I am confident that continued practice will facilitate familiarity and ease.

  Here is how I did the project:
  1. Create the Questions Class
  2. Create a list of questions from the data.py provided
  3. Implement the Quizbrain Class and its next_question method
  4. Implement still_has_questions method that will be used to run the while loop
  5. Implement check_answer method that checks if the user's answer is correct
  6. Initialize score attribute to keep track of the score
  7. Print the score after answering and when the quiz ends.
  8. Additional: Randomize the questions using the random module

  Conclusion:
  
  Looking back on Day 15, I am thrilled with the progress I made and the knowledge I acquired. Overcoming the initial hurdles of transitioning from a vacation mindset to active learning demonstrated my dedication and resilience. With 85 days remaining in my learning journey, I am optimistic about the opportunities ahead to expand my skills and explore new topics.

## Progress
 - Finished Dictionaries and Dictionary Function lessons in Python Intermediate on Sololearn
 - Completed Day 16 of 100 Days of Python
 - Completed Day 17 of 100 Days of Python
