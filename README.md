# Student's Dilemma

You and a fellow **CodeLouisville** student (played by the computer) both been caught cheating on your final project, however it isn't clear whether one of you plagiarized the other's project or if you conspired together. In an effort to uncover the whole truth, you are both being interrogated. During interrogation you both have are offered a simple choice: confess or stay silent. 

However, there are conditions:
- If you both confess: Since you both came clean, you will be permitted to submit a new project by the class deadline otherwise you will fail, but you will be allowed to take the course again. (2 points)
- If one of you confesses and the other does not. It is assumed that the student who confesses must have plagiarized the other student's work without consent:    
    - The student who confesses will be expelled from the program, banned for life, and worst of all, will receive a red X on their permanent record. (-3 points).  
    - The student who stays silent is deemed an unknowing victim and will have their final project graded as normal. (3 points). 
- If you both stay silent: You will both fail the class and but will be allowed to take the course again, after a 1 year suspension, you will not be expelled from the program, and, thankfully, will avoid the dreaded red X on your permanent record. (-1 points)

You will have between five and fifteen chances to try and outwit the computer. For the purposes of the game, each possible outcome is awarded a numeric point value (in parentheses  above).
-----

### Can you outwit the computer and achieve the higher score? 

-----
TODO: move scoring matrix to something we can easily edit (here in the readme?) but also load as "settings" in the program. maybe use regex to pull this off?
TODO: provide description of code structure and implementation of features here. 
TODO: provide some way to select computer strategies 

TODO: (stretch) record the moves and final scores in a data file 
    - convert each round's score/moves data into an object (round # computer choice, player choice, computer strategy, player name) 
    - convert game info into a list of score objects
    - extend objects to save as JSON
TODO: (stretch) provide some statistical analysis on the recorded games
    - load objects from JSON and parse with pandas or NumPy


TODO: (stretch2) extend data analysis to include computer's strategy
TODO: (stretch2) allow the computer to play itself (to be able to test strategies)
