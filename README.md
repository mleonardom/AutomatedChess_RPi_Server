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
gunicorn --bind 0.0.0.0:8000 --reload server.app
```