from tkinter import *
from pygame import mixer
import random
import time
import sphinx

class GameLogic():
    mixer.init()
    songsList = [["Barbariki.mp3", "Moscow.mp3", "Wave.mp3"],
                ["Барбарики", "Москва", "Волна"]]


    def EnterNamePlayerOne(self):
        global firstName
        firstName = playerOneName.get()
        print(firstName)

    def EnterNamePlayerTwo(self):
        global secondName
        secondName = playerTwoName.get()
        print(secondName)

    def EnterNamePlayerThree(self):
        global thirdName
        thirdName = playerThreeName.get()
        print(thirdName)

    def EnterRounds(self):
        global rounds
        rounds = RoundsEntry.get()
        print(rounds)

class Start():
    def start(self):
        global playerOneName, playerTwoName, playerThreeName, firstName, secondName, thirdName, RoundsEntry
        startingWindow = Tk()
        startingWindow.geometry('275x300')
        startingWindow.title("Введите данные")

        player_oneLabel = Label(startingWindow, text="Игрок 1", font=("Arial", 12))
        player_oneLabel.grid(column=0, row=0)
        playerOneName = Entry(startingWindow, width=20)
        playerOneName.grid(column=0, row=1)
        AcceptPlayerOneName = Button(startingWindow, text="Принять", command=GameLogic.EnterNamePlayerOne)
        AcceptPlayerOneName.grid(column=1, row=1)

        player_twoLabel = Label(startingWindow, text="Игрок 2", font=("Arial", 12))
        player_twoLabel.grid(column=0, row=2)
        playerTwoName = Entry(startingWindow, width=20)
        playerTwoName.grid(column=0, row=3)
        AcceptPlayerTwoName = Button(startingWindow, text="Принять", command=GameLogic.EnterNamePlayerTwo)
        AcceptPlayerTwoName.grid(column=1, row=3)

        player_threeLabel = Label(startingWindow, text="Игрок 3", font=("Arial", 12))
        player_threeLabel.grid(column=0, row=4)
        playerThreeName = Entry(startingWindow, width=20)
        playerThreeName.grid(column=0, row=5)
        AcceptPlayerThreeName = Button(startingWindow, text="Принять", command=GameLogic.EnterNamePlayerThree)
        AcceptPlayerThreeName.grid(column=1, row=5)

        RoundsLabel = Label(startingWindow, text="Введите количество раундов", font=("Arial", 10))
        RoundsLabel.grid(column=0, row=6)
        RoundsEntry = Entry(startingWindow, width=20)
        RoundsEntry.grid(column=0, row=7)

        AcceptRounds = Button(startingWindow, text="Принять", command=GameLogic.EnterRounds)
        AcceptRounds.grid(column=1, row=7)

        playButton = Button(startingWindow, text="Начать игру", command=Game.game)
        playButton.grid(column=0, row=8)

        quitButton = Button(startingWindow, text="Quit", command=startingWindow.quit)
        quitButton.grid(column=0, row=9)
        startingWindow.mainloop()

class Game():
    def game(self):
        x = 0
        global score_one, score_two, score_three, rounds
        score_one = 0
        score_two = 0
        score_three = 0

        def playMusic():
            global x
            x = random.randint(0, 2)
            mixer.music.load(GameLogic.songsList[0][x])
            mixer.music.play()

        def pauseMusic():
            mixer.music.pause()

        def addPointToPlayerOneScore():
            global score_one
            score_one += 1
            scoreOne['text'] = str(score_one)

        def addPointToPlayerTwoScore():
            global score_two
            score_two += 1
            scoreTwo['text'] = str(score_two)

        def addPointToPlayerThreeScore():
            global score_three
            score_three += 1
            scoreThree['text'] = str(score_three)

        def DeleteSuccessResult():
            Success.destroy()

        def DeleteFailResult():
            Fail.destroy()

        def sendAnswer():
            global score_one, score_two, score_three, x, Success, Fail
            playerAnswer = Answer.get()
            rightAnswer = GameLogic.songsList[1][x]
            if playerAnswer == rightAnswer:
                Success = Label(window, text="Верно!", font=('Arial', 14))
                Success.grid(column=3, row=5)
                time.sleep(1.5)
            else:
                Fail = Label(window, text="Неправильно! Переход хода", font=('Arial', 14))
                Fail.grid(column=3, row=5)
                time.sleep(1.5)
            if (score_one + score_two + score_three) == rounds:
                GameOver = Label(window, text="Игра закончена", font=('Arial', 14))
                GameOver.grid(column=0, row=8)
                time.sleep(2)
                window.quit()

        window = Tk()
        window.title("Угадай мелодию")
        window.geometry('800x600')

        playerOneLabel = Label(window, text="{}".format(firstName), font=("Arial", 14))
        playerOneLabel.grid(column=0, row=0)

        playerTwoLabel = Label(window, text="{}".format(secondName), font=("Arial", 14))
        playerTwoLabel.grid(column=1, row=0)

        playerThreeLabel = Label(window, text="{}".format(thirdName), font=("Arial", 14))
        playerThreeLabel.grid(column=2, row=0)

        scoreOne = Label(window, text="{}".format(score_one), font=('Arial', 14))
        scoreOne.grid(column=0, row=1)

        scoreTwo = Label(window, text="{}".format(score_two), font=('Arial', 14))
        scoreTwo.grid(column=1, row=1)

        scoreThree = Label(window, text="{}".format(score_three), font=('Arial', 14))
        scoreThree.grid(column=2, row=1)

        AddScoreOne = Button(window, text="Добавить балл игроку 1", command=addPointToPlayerOneScore)
        AddScoreOne.grid(column=0, row=2)
        AddScoreTwo = Button(window, text="Добавить балл игроку 2", command=addPointToPlayerTwoScore)
        AddScoreTwo.grid(column=1, row=2)
        AddScoreThree = Button(window, text="Добавить балл игроку 3", command=addPointToPlayerThreeScore)
        AddScoreThree.grid(column=2, row=2)

        playButton = Button(window, text="▶", command=playMusic)
        playButton.grid(column=0, row=3)

        pauseButton = Button(window, text="⏸", command=pauseMusic)
        pauseButton.grid(column=1, row=3)

        QuestionLabel = Label(window, text="Какая песня играет?", font=('Arial', 14))
        QuestionLabel.grid(column=0, row=4)

        Answer = Entry(window, width=40)
        Answer.grid(column=0, row=5)

        sendAnswerButton = Button(window, text="Отправить ответ", command=sendAnswer)
        sendAnswerButton.grid(column=1, row=5)

        DeleteResultSuccessButton = Button(window, text="Стереть результат успеха", command=DeleteSuccessResult)
        DeleteResultSuccessButton.grid(column=0, row=6)

        DeleteResultFailButton = Button(window, text="Стереть результат неудачи", command=DeleteFailResult)
        DeleteResultFailButton.grid(column=0, row=7)
        window.mainloop()

GameLogic = GameLogic()
Start = Start()
Game = Game()
Start.start()