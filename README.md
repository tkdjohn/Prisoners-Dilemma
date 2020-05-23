# Student's Dilemma
y
It's you versus a fellow **CodeLouisville** student (played by the computer). You both have been caught cheating on your final project, however it isn't clear whether one of you plagiarized the other's project or if you both plagiarized from an outside source. In an effort to uncover the whole truth, you both have been offered a deceptively simple choice: confess or not. 

However, there are conditions:
- If you both confess: You both will fail the class, but in light of your honesty, both will be allowed to re-take the class next session. (0 points)
- If one of you confesses and the other does not: 
  - The student who confesses will be allowed to submit a new project by the original deadline, and potentially pass the course (2 points). 
  - The student who does not confess will fail, be expelled and banned from ever taking another Code Louisville course, and worst of all will receive a red X on their permanent record. (-5 points)  
 - If neither of you confesses: You both will fail the class and will not be allowed to take the course again, but you will not be expelled from the program. (-2 points)

You will have between five and fifteen chances to try and outwit the computer. For the purposes of the game, each possible outcome is awarded a numeric point value (in parentheses  above)

-----

### Can you outwit the computer and achieve the higher score? 

-----
TODO: get negative and positive and multi digit scores to line up better.

TODO: move scoring to something we can easily edit (here in the readme?) but also load as "settings" in the program.
TODO: provide description of code structure and implementation of features here. 

TODO: (stretch) record the moves and final scores in a data file 
    - convert each round's score/moves data into a data object (round # computer choice, player choice) 
    - convert game info into a list of score objects
    - extend objects to save as JSON
TODO: (stretch) provide some statistical analysis on the recorded games
    - load objects from JSON and parse with pandas or NumPy
---- these TODO s are best implemented using OOP 
TODO: (stretch2) provide a variety of strategies with some way to select/configure them - record teh selected strategy along with other stats
TODO: (stretch2) extend data analysis to include computer's strategy
TODO: (stretch2) allow the computer to play itself (to be able to test strategies)
