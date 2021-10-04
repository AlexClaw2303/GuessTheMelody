import pytest
from main import Game, Start, GameLogic

def test_EnterRounds():
    assert GameLogic.EnterRounds() == '5'

def test_EnterNamePlayerOne():
    assert GameLogic.EnterNamePlayerOne() == 'Alex'

def test_EnterNamePlayerTwo():
    assert GameLogic.EnterNamePlayerTwo() == 'Fred'

def test_EnterNamePlayerThree():
    assert GameLogic.EnterNamePlayerThree() == 'Sarah'

def test_GameStarted():
    assert GameLogic.GameStarted() == 'Game Started!'

if __name__ == "__main__":
    pytest.main()