![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome sammanomar,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!



ULTIMATE Battleships
Ultimate Battleshios is a Python terminal aame. which runs in the Code Institute mock terminal on Heroku Users can try to beat the computer by finding all of the computer's battleships before the computer tinds theirs. Each
battleship occupies one sauare on the board
Here Is the live version of my project


How to play
Ultimate Battleships Is based on the classic pen-and-paper game. You can read more about it on Wikipedia
sign, but cannot see where the computer's ships are
The player and the computer then take it in turns to make quesses and try to sink each other's battleships
The winner is the player who sinks all of their opponent's battleships first.

Features
Existing Features
Random board generation
Shins are randomv placed on born the plaver and computer boards
The plaver cannot see where the computer's ships are

• Plav against the compute
~ Mointoine croree
player guessed: (1, 2)
§ player missed this time.
missed this time.
• Input validation and error-checkina
• You cannot enter the same auess twice
S Guess a rowa
• Var met enter
• var cannot dess
; Values must be betwen
o ata maintained in cace inctancos

Euture Features
Allow plaver to select the board size and number of shios
Allow plaver to position shios themselves
• Have chins larger than 'y?
Data Model I decided to use a Board class as my model. The aame creates two instances of the Board class to hold the plaver's and
the computer's board The Board class stores the board size. the number of ships. the position of the ships. the guesses against that board
and details such as the board tvpe (olaver's board or computer) and the paver's name.
The class also has methods to heln play the came such as a moint method to print out the current beard an
add ships method to add ships to the board and an add guess method to add a guess and return the result.

Testing
[ have manually tested this proiect by doing the following
• Daccod the rode throuch a DED& lintor and confirmed there ore no nroblome
• Given invalid inouts: strinas when numbers are expected out of bounds inouts. same inbut twice
Tested in my local terminal and the Code Institute Heroku terminal
Buas When I wrote the proiect. I was aetting index errors because I had forgotten that the lists are zero indexed. I fixed
this br addina size _ 1 where necessarv
properly
Remainina Buas
• No buas remainina

Validator Testing
~ DEDO
No errors were returned from PEPSonline cor

Deplovment
This proiect was deploved using Code Institute's mock terminal for Heroku.
Stens for deplovment
o Fork or clone this renocitor.
a Crosto a nom Horobu onn
o link the Herokuann to the renociton
click on Donlou

Credits
Code Institute for the denloyment terminal
• Wikipedia for the details of the Battleshios game