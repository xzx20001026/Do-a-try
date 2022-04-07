'''
    @author:Xu Zixin
    @time:2022.4.5
    @versions:1.0
    @name:Hangman
'''
import random

HANGMANPICS=[           '''
                +---+
                |   |
                    |
                    |
                    |
                    |
             ============''','''

                +---+
                |   |
                0   |
                    |
                    |
                    |
             ============''','''

                +---+
                |   |
                0   |
                |   |
                    |
                    |
             ============''','''

                +---+
                |   |
                0   |
               /|   |
                    |
                    |
             ============''','''

                +---+
                |   |
                0   |
               /|\  |
                    |
                    |
             ============''','''

                +---+
                |   |
                0   |
               /|\  |
               /    |
                    |
             ============''','''

                +---+
                |   |
                0   |
               /|\  |
               / \  |
                    |
             ============''']

words='''Currently the rising temperature Arctic ice melt deforestation uncontrolled industrialization air pollution
and depletion of the ozone layer are all connected and would lead to a single event the destruction
of the world. We have already harmed the environment to a great extent and the time has come for all
nations to work together to reduce the environmental damage The sudden flood in the USA intense storms in Asia'''.split()

#从单词词库中随机获得一个单词
def getRandomWord(wordList):
    index=random.randint(0,len(wordList)-1)
    return wordList[index]

#模块一:Hangman形态的显示
#模块二:missedLetters的显示
#模块三:blank形态的显示，取决于secretWord长度以及correctLetters
def displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord):
    #Step1:根据missedLetters个数显示Hangman的形态
    print(HANGMANPICS[len(missedLetters)])
    print()
    #Step2:missedLetters的显示
    print("Missed letters: ",end='')#这里必须要加end='',否则会导致自动换行
    for letters in missedLetters:
          print(letters,end='')
    print()
    #Step3：blank形态的显示
    blank='_'*len(secretWord)#blank初始形态
          
    for i in range(0,len(secretWord),1):#进行正确字母的替换
          if secretWord[i] in correctLetters:#这里我一开始有一个疑问,secreWord只是一个单词也可以当做一个列表使用嘛，答案是肯定的
              blank=blank[0:i]+secretWord[i]+blank[i+1:]
          
    for letter in blank:#显示blank的最终形态
          print(letter,end='')
    print()

#确保玩家输入的是正确的一个字母，单独一个字母，不重复，在26个字母中
def getGuess(alreadyGuess):#传这个形参，是为了下面其中一个分支的判断
    while True:#为什么要加while true???
        print("Guess a letter.")
        guess=input()
        guess.lower()
        if len(guess)!=1:
            print("Please enter a single letter.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a letter.")
        elif guess in alreadyGuess:
            print("Please enter a different letter.")
        else:
            return guess
    
#询问玩家是否还想再玩一次
def palyAgain():
    print("Do you want to play again?")
    return input().startswith('y')#返回的是ture or false

#--------------------------------------------------------------------------------------------以上都是常量，函数的定义部分，下面是主函数部分-----------------------------------------------------------#
print("H A N G M A N")
print("You only have 6 opportunities")
missedLetters=''
correctLetters=''
secretWord=getRandomWord(words)
gameIsGone=False

while True:
    displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
    guess=getGuess(missedLetters+correctLetters)
    
    if guess in secretWord:
        correctLetters=correctLetters+guess
        #判断一下玩家是否取得获胜
        Win=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                Win=False
                break  #玩家还没有取得胜利
        if Win==True:
            print("Yes! You have won the game and the word is "+secretWord+"!!!")
            gameIsGone=True
            
    else:
        missedLetters=missedLetters+guess
        #判断一下玩家是否失败
        if len(missedLetters)==6:
            displayBoard(HANGMANPICS,missedLetters,correctLetters,secretWord)
            print("Sorry! You have lost the game and the word is "+secretWord+"!!!")
            gameIsGone=True
            
#询问玩家是否想再玩一次
    if gameIsGone:
        if palyAgain():
            print("H A N G M A N")
            print("You only have 6 opportunities")
            missedLetters=''
            correctLetters=''
            secretWord=getRandomWord(words)
            gameIsGone=False
        else:
            break
    
    
    

