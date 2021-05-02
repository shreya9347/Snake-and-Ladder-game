<h1 align="center" style="margin-top: -4px !important;">Snake and Ladder Game</h1>
<p align="center">
  <img src="https://img.shields.io/badge/build-passing-brightgreen">
  <img src="https://img.shields.io/badge/Joy of Computing Python-Nptel Course-informational">
  <img src="https://img.shields.io/badge/python-3.8-informational">
  <img src="https://img.shields.io/badge/maintainer-Shreya Chourasiya-information">
  <img src="https://img.shields.io/badge/os-linux-brightgreen">
  <img src="https://img.shields.io/badge/contributions-welcome-brightgreen">
</p>

Snake and ladder is a simple game consists of snakes and ladders. The object of the game is to navigate one's game piece, according to die rolls, from the start (bottom square) to the finish (top square), helped or hindered by ladders and snakes respectively.

This is a python based version of this game which consist of GUI which is designed using Python's Image library 

Libraries Used:-

1. PIL also known as Python Imaging Library is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.From where we can import lot of image libraries

2. Random Module is a built-in module to generate the pseudo-random variables. It can be used perform some action randomly such as to get a random number, selecting a random elements from a list, shuffle elements randomly, etc.

Let's start :

<p align="center">
  <img src="https://github.com/shreya9347/Snake-and-Ladder-game/blob/main/board_image.png">
</p>
<br>

With the help of board image we have to form dictionary of ladder and snake such that ladder={start_point:ending_point},snake={ending_point,starting_point}
ladder = {1: 38, 4: 14, 8: 30, 21: 42, 28: 74, 50: 67, 71: 92, 88: 99}
snake = {32: 10, 34: 6, 48: 26, 62: 18, 88: 89, 95: 56, 97: 78}

Functions:

def show_board():This Function is needed to show the image of board

def check_ladder(points): It checks the point in Ladder dictionary .If matches Climb up (increment to ending_point).

def check_snake(points): It checks the points in Snake dictoionary .If matches snake bite!(decrement to starting_point).

def reached_end(points): checks weather a points has reached end point that is 100

def play(): It asked for player name and then dice is roll randomly between (1,6)

How to install this

git clone https://github.com/shreya9347/Snake-and-Ladder-game
