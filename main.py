"""
Framework for peer mechanism

A set of N competitors compete in M rounds of a game to try to claim a prize
In each round, the competitors get a score that ranks them from 1 to N
After each round, each competitor must vote for another competitor who they want to claim the prize based on their score
Once all rounds are finished, the competitor with the most votes wins
However,
There is a random chance each round that an audit occurs
When an audit occurs, each competitor that could have voted for another competitor with a higher score gets a penalty of -2 votes.


"""

import random



class Competitor:
    def __init__(self,id,skill):
        self.id = id
        self.skill = skill
        self.votes = 0
        self.score = 0

    def select(self,competitors):
        # implement logic to use ml to make decision
        for competitor in competitors:
            if competitor.id == self.id:
                pass
            # create input to NN that combines player score and votes

        pass

    def result(self):
        var = random.randint()
        res = self.skill + var
        return res


