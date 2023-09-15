# **Battleships Game**

<img src="/documentation_assets/images/battleships_responsive.png" alt="Main readme photo">

Welcome to BattleShips, my third project. This project uses python to create a simple single player battleships game.

The deployed version of the game can be found [here](https://ci-python-battleships-f474d146740d.herokuapp.com/).

## How To Play Battleships

This is a simple version of the classic pen and paper game of battleships.

In this version, one board which is 5x5 is displayed to the user. 

On this board there have been placed 4 enemy ships which take up one space.

The user will have 15 guesses to try and destroy the 4 ships before losing the game.

## **User Experience (UX)**

### Project Goals

The main focus of Battleships is to create a entertaining game for the user that is both engaging and interactive. My project should display the basic use of the Python language.

### User Goals

First Time User

As a first-time user, I want to be engaged and enjoy playing the game.
As a first-time user, the game should spark a positive emotion.
As a first-time user, I would like the instruction to be clear so I fully understand how to play.
As a first-time user, the game shouldn't be to difficult to win.

Returning Visitor User

As a Returning Visitor, I want to have another enjoyable experience and win at the game.

### User Expectations

- The game is enjoyable to play.
- The rules are easy to follow.
- To want to come back and play again.

## Game Structure

In the design phase of my project I used [LucidChart](https://www.lucidchart.com/) to create the logic of my battleships game.

<img src="/documentation_assets/images/battleships_logic.png" alt="Battleships logic">

## Features

### Current Features

- Battleships menu
    - Play game
    - Instructions
    - Exit game

<img src="/documentation_assets/images/battleships_menu.png" alt="Battleships menu">

Instructions
- Explaining how to play the game in a fun way to captivate the user.

<img src="/documentation_assets/images/battleships_instructions.png" alt="Battleships instructions">

Exit game

<img src="/documentation_assets/images/battleships_exit.png" alt="Battleships exit game">

Hit battleship
- An 'X' will appear on the board and a message saying "Boom! You hit! A ship has exploded! You were granted another shot!" will appear.

<img src="/documentation_assets/images/battleships_youhit.png" alt="Battleships you hit">

Missed battleship
- An '-' will appear on the board and a message saying "You missed!" will appear.

<img src="/documentation_assets/images/battleships_youmissed.png" alt="Battleships you missed">

Won game
- When all 4 ships have been sunk you win and a message saying "You sunk all the enemy ships! Congratulations, you won!" will appear.

<img src="/documentation_assets/images/battleships_youwon.png" alt="Battleships you won">

Lost game
- If you fail to sink the ships in 15 shots you lose and a message saying "Game over! You ran out of ammo, and the enemy ships are still afloat. Better luck next time!" will appear.

<img src="/documentation_assets/images/battleships_youlost.png" alt="Battleships you lost">

- Input Validation

Only enter a number

- You can only enter numbers in the input fields or an error message will appear.

<img src="/documentation_assets/images/battleships_onlyenternumber.png" alt="Battleships only enter a number">

Already shot there

- If you input a coordinate that has already been placed then an error message will appear.

<img src="/documentation_assets/images/battleships_aleadyplaced.png" alt="Battleships already placed there">

### Features To Add

- To add a computer board and take turns in attacking eachothers ships.

- To have the option for the user to choose from different grid sizes.

- To have the option for the user to place their ships on the board.

## **Testing**

### Manual Testing

- I used print statements throughout my code to make sure my functions were working correctly.
- I ran my code through the terminal regularly to make sure there were no errors and everything was working correctly.
- When creating value errors in my code I tested this by inputting incorrect data to make sure the correct error message was coming up. 

### Bugs (Fixed)

- when running my code through the terminal I recieved the error message "TypeError: 'function' object is not subscriptable". I fixed this by changing the name of the function as I had a variable the same name.

- when running my code through the terminal I recieved the error message "TypeError: create_board() missing 1 required positional argument: 'board_to_print'". I fixed this by adding the argument 'board' into the function as this was missing.

### Bugs (Existing)

no existing bugs. All errors were corrected.

### Validator Testing

I ran my code through the PEP8 validator to validate my code

Before:

<img src="/documentation_assets/images/pep8_before.png" alt="pep8 before errors were fixed">

I fixed all the error messages by:

- Removing any trailing whitespace.
- Adding an extra \ to remove the 'invalid escape sequence' error message
- Adding another space above the functions to fix the 'expected 2 blank lines, found 1' error message
- Adapting or shortening any code or strings that were too long.

After:

<img src="/documentation_assets/images/noerrors.png" alt="pep8 no errors">

## Deployement

I used Heroku to deploy my project. I did this by:

- Push final commits to Github.
- Log on to [Heroku](https://www.heroku.com).
- Select 'New' in the top right corner.
- Select 'Create new app'.
- Enter a name for the app and select Europe as the region.
- Go to the 'Settings' tab.
- Click 'Add buildpack'.
- Select 'Python', then 'Save changes'.
- Select 'Nodejs', then 'Save changes'.
- Making sure to add Python first and Nodejs second.
- Go to the 'Deploy' tab.
- Connect to GitHub.
- Search for the Github repository and connect.
- At the bottom under Manual Deploy, click 'Deploy branch'.

## End Product

Below is the final outcome of my project:

Opening Page/Menu

<img src="/documentation_assets/images/battleships_menu.png" alt="Battleships menu">

Instructions

<img src="/documentation_assets/images/battleships_instructions.png" alt="Battleships instructions">

Play Game

<img src="/documentation_assets/images/battleships_playgame.png" alt="Battleships play game">

Hit Ship

<img src="/documentation_assets/images/battleships_youhit.png" alt="Battleships hit ship">

Missed Ship

<img src="/documentation_assets/images/battleships_youmissed.png" alt="Battleships missed ship">

Winning Game Page

<img src="/documentation_assets/images/battleships_youwon.png" alt="Battleships winning game page">

Losing Game Page

<img src="/documentation_assets/images/battleships_youlost.png" alt="Battleships losing game page">


## Credits
 - Code Institute - Learning resources and deployment instructions.
 - My Mentor Marcel - Great support with regular check ins.

