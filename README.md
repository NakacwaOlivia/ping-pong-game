## ping-pong-game
This is a simple 2D Ping Pong game built using Python and the Pygame library. The game allows two players to compete against each other, controlling paddles to prevent the ball from going out of bounds. The first player to score the most points wins!

### Table of Contents
- Features
- Installation
- How to Play
- Controls
- Game Rules
- Screenshots
- Contributing
- License

### Features
Classic 2D Ping Pong gameplay.
Smooth movement of paddles and ball.
Real-time score display for both players.
Simple collision detection between ball, paddles, and walls.
Frame rate controlled at 60 FPS.

### Installation
#### Prerequisites
Python 3.x installed on your system.
Pygame library installed.
You can install Pygame using pip:
pip install pygame

### Download and Run
Clone this repository or download the game files:
git clone https://github.com/NakacwaOlivia/ping-pong-python.git
cd ping-pong-python
Run the game:
python ping_pong.py

### How to Play
This is a two-player game where each player controls a paddle.
The goal is to prevent the ball from passing your paddle and bouncing it back to your opponent.
The player who misses the ball loses a point to the opponent.
The game continues indefinitely, keeping track of the score.

### Controls
Left Player:
Move Up: W
Move Down: S
Right Player:
Move Up: ↑ Arrow Key
Move Down: ↓ Arrow Key

### Game Rules
The ball starts moving toward the right paddle.
Players must hit the ball with their paddles to send it toward the opponent.
If the ball goes past a paddle and touches the left or right edge of the screen, the opposing player scores a point.
The first player to score the most points wins (no score limit set by default).
The ball speed increases as the game progresses, making it more challenging.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
