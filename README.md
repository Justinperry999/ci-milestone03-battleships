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

## Testing

### Bugs (Fixed)

### Bugs (Existing)

### Validator Testing


## Deployement


## End Product


## Credits

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
