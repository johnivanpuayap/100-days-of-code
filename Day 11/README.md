# Day 11: BlackJack Capstone Project
## Reflection
 Today was a busy day for me, but I wanted to ensure I made some progress on my 100 Days of Python journey. Despite feeling tired, I dedicated time to Day 11, which involved working on a BlackJack Capstone Project. My aim is to enhance the program by incorporating additional features beyond the main requirements. Specifically, I plan to enable the CPU to make decisions on hitting or standing, similar to how dealers do in casinos. Additionally, I want the CPU's choices to be influenced by various scenarios and probabilities.

 To begin, I created a repository for the project and focused on the main requirements. Here's how I approached it

 1. Imported the logo from art.py and the random module. I also set the default value of an Ace card to 11 in the cards list.
 2. Developed a function to randomly retrieve a card.
 3. Established the main flow of the program, starting with asking the user if they want to play the game.
 4. Generated the user_cards and cpu_cards.
 5. Created a while loop to prompt the user for adding another card or not.
 6. Within the while loop, implemented an if statement to handle the following scenarios:
    - If the user's score exceeds 21 and they don't have an Ace, they lose.
    - If the user's score exceeds 21 but they have an Ace, subtract 10 from their score and replace the value of 11 with 1.
    - If the score reaches 21, the loop stops.
 7. Once the loop ends, the scores are compared, and the game's result is displayed.

 I was actually having fun doing this project and would actually like to continue and improve on this. I will definitely try and make it so that they are only using a certain number of decks like in the casino and probably some graphics. But anyway, this project was fun that even when I was tired all day, I actually had more energy after I started doing this

 Conclusion
 Today's focus was the BlackJack Capstone Project, and despite a busy schedule and fatigue, I pushed through and made notable progress. I look forward to continuing this project and further enhancing it, including features such as limited decks and potential graphics. Engaging with this project revitalized my energy and enthusiasm, reaffirming my commitment to this learning journey. 89 Days to go!

## Progress
 - Completed Day 11 of 100 Days of Python
 - Initiated the Blackjack Repository ([Repository](https://github.com/johnivanpuayap/Blackjack))
