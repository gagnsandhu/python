import random

class Game():
    dict={'Heart':{'one':{1:1},'two':{2:1},'three':{3:1},'four':{4:1},'five':{5:1},'six':{6:1},'seven':{7:1},'eight':{8:1},'nine':{9:1},'ten':{10:1},'jack':{11:1},'queen':{12:1},'king':{13:1},'ace':{20:1}},'Diamond':{'one':{1:1},'two':{2:1},'three':{3:1},'four':{4:1},'five':{5:1},'six':{6:1},'seven':{7:1},'eight':{8:1},'nine':{9:1},'ten':{10:1},'jack':{11:1},'queen':{12:1},'king':{13:1},'ace':{20:1}},'Spade':{'one':{1:1},'two':{2:1},'three':{3:1},'four':{4:1},'five':{5:1},'six':{6:1},'seven':{7:1},'eight':{8:1},'nine':{9:1},'ten':{10:1},'jack':{11:1},'queen':{12:1},'king':{13:1},'ace':{20:1}},'Club':{'one':{1:1},'two':{2:1},'three':{3:1},'four':{4:1},'five':{5:1},'six':{6:1},'seven':{7:1},'eight':{8:1},'nine':{9:1},'ten':{10:1},'jack':{11:1},'queen':{12:1},'king':{13:1},'ace':{20:1}}}
    def play(self,user1,user2):
        print(f'{user1.name} turn')
        card1,rem1=random.choice(list(user1.dict.items()))
        number1,value1=random.choice(list(rem1.items()))
        print(list(user1.dict[card1][number1].items()))
        key1=list(user1.dict[card1][number1].items())
        print(f"{user1.name} your card was {card1} and value was {number1}\n")
        print(f"{user2.name} turn")
        card2,rem2=random.choice(list(user2.dict.items()))
        number2,value2=random.choice(list(rem2.items()))
        print(list(user2.dict[card2][number2].items()))
        key2=list(user2.dict[card2][number2].items())
        print(f"{user2.name} your card was {card2} and value was {number2}\n")
        if key1>key2:
            print(f"{user1.name} won this time")
            user1.dict[card2][number2][key2[0][0]]+=1
            print(user1.dict[card2][number2][key2[0][0]])
            user2.dict[card2][number2][key2[0][0]]-=1
            print(user2.dict[card2][number2][key2[0][0]])
            if user2.dict[card2][number2][key2[0][0]]==0:
                del user2.dict[card2][number2]
        elif key2>key1:
            print(f"{user2.name} won this time")
            user2.dict[card1][number1][key1[0][0]]+=1
            user1.dict[card1][number1][key1[0][0]]-=1
            if user1.dict[card1][number1][key1[0][0]]==0:
                del user1.dict[card1][number1]
        else:
            print("Match tied\n")
    
    # def check(self,obj):
    #     s
    #     print(obj.dict+"\n")
    #     # print(user2.dict+"\n")

class User(Game):
    def __init__(self,name):
        self.name=name


user1=User(name=input("Enter name of first player: "))
user2=User(name=input("Enter name of second player: "))
print("Now Lets start the game\n")
game=Game()
# for i in range(0,13):
game.play(user1,user2)
# game.check(user1)
# game.check(user2)
# print(user1.dict)
# print(user2.dict)

          