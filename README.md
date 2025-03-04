# AutomatedChess_RPi_Server
Automated Chess Arduino project server side using stockfish

## Using stockfish-1
This project use the https://github.com/johndoknjas/stockfish-1 project

## RaspberryPi install
```bash
$ sudo apt-get install stockfish
```

## Gunicorn to take code changes
To take code changes use the `--reload` command option

```bash
gunicorn --bind 0.0.0.0:8081 --reload server.app
```

## Game HTTP requests
To start a game:

PUT `/chess/game`
With Payload:
```JSON
{
  "user_color": "BLACK", // Must be WHITE or BLACK
  "elo": 2000, // The Stockfish ELO between 1320 and 3190 (Default 1500)
  "depth": 20, // The depth of the machine between 0 and 80 (Default 10)
  "threads": 4 // The threads to use, this must be the same CPU number (Default 2)
}
```
If `user_color` is BLACK the first move will be on teh game creation
Example response:
```jSON
{
  "engine_parameters": {
    "Debug Log File": "",
    "Contempt": 0,
    "Min Split Depth": 0,
    "Ponder": false,
    "MultiPV": 1,
    "Skill Level": 20,
    "Move Overhead": 10,
    "Minimum Thinking Time": 20,
    "Slow Mover": 100,
    "UCI_Chess960": false,
    "UCI_LimitStrength": true,
    "UCI_Elo": 2000,
    "Threads": 4,
    "Hash": 2048
  },
  "stockfish_move": "d2d4" // None if the user plays with WHITE pieces
}
```

To make a move
POST `/chess/game`
```JSON
{
  "move": "d2d4"
}
```
Example response:
```JSON
{
  "stockfish_move": "g8f6" // NULL if is a invalid move
}
```
