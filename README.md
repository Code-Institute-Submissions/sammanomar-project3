# CONNECT FOUR GAME
Connect four game  is a Python terminal game. which runs in the Code Institute mock terminal on Heroku. 2 Users (X or O) can try to beat each other by dropping and connecting four pieces whether vertically or horizontally or diagonally. The first player to connect four will win.

Here Is the live version of my project:

![](/screenshots/a.png)

## How to play
Connect four is based on the classic connect four game. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Connect_Four) 
in this version, the players names are automaically generated (X,O).
Pieces dropped are marked on the board with an X or O marks.
The two players take it in turns to drop pieces and try to connect four.
The winner is the player who connects four four first whether vertically or horizontally or diagonally.

## Features
### Existing Features
- Flexible 6 row X 8 column board generation
- Marked up board with columns number on the top

![](/screenshots/b.png)

- Play against another player without computer
- Accept users input
![](/screenshots/c.png)
![](/screenshots/d.png)

- Input validation and error-checking
1. You cannot enter string
![](/screenshots/e.png)
2. You must enter numbers from 1 to 8 only
![](/screenshots/f.png)
3. Zero, negative values, or any special character values are not acceptable
![](/screenshots/i.png)
4. Game saves the last move of any player on the top of the title of the game
![](/screenshots/j.png)
- data maintained in class instances
5. Win and draw messages
![](/screenshots/h.png)
![](/screenshots/k.png)

### Future Features
- Allow more players to play the game
- Add difficulty levels
- Add player VS computer option

## Data Model 
I decided to use a Board class as my model. The game creates the instance of the Board class. 
The Board class prints the slots of the board, rotate the turn of the player, check the position of the dropped piece. check the possibility of win against that board in all directions.
I used a python trick to print 50 dashes all next to each other using `print` method.

## Testing
Have manually tested this proiect by doing the following:
- passed the code through a PE8 linter and confirmed there are no problems
- Given invalid inputs: strings when numbers are expected out of bounds inputs.
- Tested in my local terminal and the Code Institute Heroku terminal

## Bugs 
- When I wrote the project. I had an issue with validating zero and negative entries. I fixed
this by using if conditional statment
- E501 error line too long by PEP8. I fixed it using line continuation operator \ and parenthesis()

## Remaining Bugs
No bugs remaining

## Validator Testing
- PEP8
No errors were returned from PEP8.online.com
![](/screenshots/l.png)

## Deployment
This proiect was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment
1. Fork or clone this repository
2. Create a new Heroku app
3. Set the buildpacks to Python and NodeJS in that order
4. Link the Herokuapp to the repository
5. Click on Deploy

## Credits
- Code Institute for the deployment terminal
- Wikipedia for the details of the connect four game
- My mentor Lauren Nicole
- freeCodeCamp.org
- stackoverflow.com
- quora.com
- doingmathwithpython.github.io
