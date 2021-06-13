from abc import abstractmethod
from collections import Counter
import random



class GameLogic():

    odds={1:1000,2:200,3:300,4:400,5:500,6:600}
    odds_2={1:100,5:50}
    
    
    @staticmethod
    def calculate_score(numbers):
        dice_counter = Counter(numbers) 
        score=0
        if(len(dice_counter) == 6):
            return 1500
        if len(dice_counter) == 3 and dice_counter.most_common()[2][1] == 2:       
	        return 1500
        # if(len(dice_counter) == 3 and len(numbers) == 6):
        #     if(dice_counter.most_common()[0][1] == 2 and dice_counter.most_common()[1][1] == 2 and dice_counter.most_common()[2][1] == 2):
        #         return 1500

        for key in dice_counter:
            count = dice_counter[key]        
            if(count==3):
                score=score+GameLogic.odds[key]
            if(count==4):
                score=score+GameLogic.odds[key]*2
            if(count==5):
                score=score+GameLogic.odds[key]*3
            if(count==6):
                score=score+GameLogic.odds[key]*4

            if(key ==1 or key ==5):
                print(key)
                if(count==1):
                    score=score+GameLogic.odds_2[key]
                if(count==2):
                    score=score+GameLogic.odds_2[key]*2
        return int(score)
        
    @staticmethod 
    def roll_dice(times):
        return tuple([random.randint(1,6) for i in range(times)])

class Banker:
    def __init__(self) :
        self.balance=0
        self.shelved=0


    def shelf(self ,value):
       self.shelved=value
       return self.shelved  

    def bank (self):
        self.balance +=self.shelved
        self.shelved=0


    def clear_shelf(self):
         self.shelved=0