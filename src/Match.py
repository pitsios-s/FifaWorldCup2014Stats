#!/usr/bin/python3.4

class Match:
   
   def __init__(self, team1, team2, score1, score2):
      self.team1 = team1
      self.team2 = team2
      self.score1 = score1
      self.score2 = score2
      
   def is_over(self):
      return self.score1 + self.score2 >= 3
      
   def print_match(self):
      print(self.team1 + " - " + self.team2 + " " + str(self.score1) + " - " + str(self.score2))
