# Bomberman Game 

## Usage
- Clone the repository
- In the repository, do
```python3 start_here.py```

## Instructions
![gameplay](gameplay.png)

Player: the one with these eyes: ^ ^
Enemy: the one with these eyes: X X
Brick wall: shown using '///' symbol 

- To move around player, use: `a`, `s`, `d`, `w` 
- To drop a bomb, use: `b`
- To quit, press `q`

## Scoring
- +20 points for destroying a brick wall
- +100 points for destroying an enemy
- To win: destroy all enemies!

## Game features
- Random board generation every time you play.
- Asynchronous enemy movement 
- Multilevel game (a total of 4 levels)
- Bomb counts down to blast off 

## Object-oriented programming features demonstrated:
1) Modularity implemented (several modules)
2) Inheritance (All board objects inherit from the board_object class)
3) Encapsulation (Use of classes)
4) Polymorphism (both player and enemy move, but move differently)





