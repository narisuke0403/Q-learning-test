from AI import AI
class player:
  
  def __init__(self, *args, **kwargs):
    if(len(args) != 0):
      self.position_x = args[0]
      self.position_y = args[1]
    else:
      self.position_x = 0.0
      self.position_y = 0.0

  # player moving method
  def move(self,stiuation):
    player_ai = AI(stiuation)
    if(type(player_ai.decision()) == str):
      print(player_ai.decision())
    else:
      move_x, move_y = player_ai.decision()
      self.position_x += move_x
      self.position_y += move_y

  def simulation_move(self,x,y):
    self.position_x += x
    self.position_y += y
