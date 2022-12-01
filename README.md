# DinoBattle---LLD
LLD question to design a dino game. Instructions attached in the README file



Dinosaur Class & Dino Battle
Introduction:
● Essentially the user will choose a dinosaur (T-Rex, Stegosaurus, Triceratops, or one that
you will decide on) and then the computer will choose one of the remaining choices.
● In each round the user will choose to be aggressive or defensive and their dinosaur will
attack accordingly. The computer will choose as well using a random number.
● This choice will affect damage ranges, but also defensive ranges for the computer’s
counterattack.
The stats for the three suggested dinos are:
○ T-Rex:
■ Health: 20 pts
■ Damage:
● Aggressive: 6 - 10
● Defensive: 4 - 8
■ Defense:
● Aggressive: 0 - 2
● Defensive: 3 - 5
○ Stego:
■ Health: 40 pts
■ Damage:
● Aggressive: 3 - 6
● Defensive: 1 - 4
■ Defense:
● Aggressive: 1 - 3
● Defensive: 4 - 8
○ Triceratops:
■ Health 30 points
■ Damage:
● Aggressive: 4 - 8
● Defensive: 2 - 6
■ Defense:
● Aggressive: 1 - 4
● Defensive: 2 - 6
Instructions:
DINOSAUR CLASS
1. Import declare and instantiate a random object
2. Declare instance data (PRIVATE):
a. Name
b. Attack min1(aggressive)
c. Attack min2(defensive)
d. Attack max1
e. Attack max2
f. Defense min1
g. Defense min2
h. Defense max1
i. Defense max2
j. Health
3. Write constructors
a. Blank(default)
b. Parameterized - Name, attack mins and maxes, defense mins and maxes, and
health - Take in all but the attack mode instance data and initialize it.
4. Write instance methods
a. Get attack (takes in attack mode and generates a random number in the
corresponding range and returns it)
b. Get defense (takes in attack mode and generates a random number in the
corresponding range and returns it)
c. Adjust health (takes in the attack[of the attacking dino] and defense[of the
defending dino] and adjusts the health of the defending dino
d. toString method to print out the dino’s stats (name and health remaining)
DINO BATTLE CLASS
1. Import declare and instantiate scanner and random object
2. Declare an int variable for the user’s selection and one for the computer’s selection.
3. Declare int variables for userAttack, userDefense, compAttack, and compDefense
4. Prompt the user to select a dinosaur (present a menu with the stats of each)
5. Have the computer select a dino at random
6. (Optional) set up a do while loop that will have the computer continue choosing a
random number until the computer has a different choice than the user.
7. Declare 2 Dinosaur objects and initialize them using the non-default constructor.
8. Generate a random number to pick who goes first (Optionally, ask the user to guess 1 or
2 and if they are correct they go first)
9. Set up a while or do/while loop that will run as long as one of the 2 dino objects has a
health above 0.
10. Inside the loop
a. If the user goes first
i. Have the user pick aggressive or defensive
ii. Have the computer generate a random number to determine aggressive
vs defensive.
iii. Call the getAttack and getDefense methods of each dino and pass the
aggressive/defensive choices as parameters then store the returned
values in the corresponding variables.
iv. Call the adjustHealth method of the computer’s dino and pass the user’s
attack and comp’s defense
v. Call the adjustHealth method of the user’s dino and pass the comp’s
attack and the user’s defense.
b. If the computer goes first
i. Have the computer generate a random number to determine aggressive
vs defensive.
ii. Have the user pick aggressive or defensive
iii. Call the getAttack and getDefense methods of each dino and pass the
aggressive/defensive choices as parameters then store the returned
values in the corresponding variables.
iv. Call the adjustHealth method of the users dino and pass the comp’s
attack and user’s defense
v. Call the adjustHealth method of the comp's dino and pass the user attack
and the comp defense.
11. If the user’s dino’s health is 0, print a loss message
12. Else print a win message.
13. (Optional) Make the entire game replayable
