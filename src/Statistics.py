#!/usr/bin/python3.4

from Match import Match

if __name__ == "__main__":
   
   matches = []
   team_goals={}
   
   with open("../res/results.txt", "r") as my_file:
      lines = my_file.readlines()
      
      for line in lines:
         components = line.split()
         matches.append(Match(components[0], components[1], int(components[2]), int(components[3])))
     
      
   for m in matches:
   
      if not m.team1 in team_goals.keys():
         team_goals[m.team1] = m.score1
      else:
         team_goals[m.team1] += m.score1
         
      if not m.team2 in team_goals.keys():
         team_goals[m.team2] = m.score2
      else:
         team_goals[m.team2] += m.score2

   srt = sorted(team_goals.items() , key = lambda x : x[1], reverse = True)
   for item in srt:
      print("{0} - {1}".format(item[0], item[1]))
    
   over = (len([m for m in matches if m.is_over()]))
   total = len(matches)
   goals = sum(team_goals.values())
   print("\nMatches over = {0}/{1}".format(over, total))
   print("Matches under = {0}/{1}".format(total - over, total))
   print("Total goals = {0}".format(goals))
   print("Goals per match = {0}".format(float(goals)/float(total)), end = "\n\n")
