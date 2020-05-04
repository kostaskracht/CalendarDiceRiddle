# CalendarDiceRiddle
The following blocks of code present the "Calendar Dice Riddle" in an interfaced way. This is an oftenly used riddle during job interviews.
The code gives to the interviewer a graphical interface, with which he can:
- View the riddle description
- Insert and check the given answer
- View the correct answer
- View a detailed explanation of the correct answer.

# Code structure
- media: Contains all images used inside the code
- sample:
   - __init__.py: Empty python file to allow calls of custom classes
   - calculations.py: Class that performs all calculations of the riddle
   - Calendar_Dice_Riddle.py: The main file for code execution
   - explanation window.py: Class that is used to produce the "Explanation window"
   - insertAnswerWindow.py: Class that is used to produce the "Insert your answer window" 
   - startupWindow.py: Class that is used to produce the "Startup window"
 
 # Packages
 In order for the code to be executed, the following packages need to be installed:
 - tkinter
 - numpy
 - Pillow
 