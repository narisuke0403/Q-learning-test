class field:
  # field information
  #length,width,hole position,goal position

  def __init__(self, length=10, hole_position_x=2, hole_position_y=2, goal_position_x=9, goal_position_y=9, *args, **kwargs):
    self.length = length
    self.hole_position_x = hole_position_x
    self.hole_position_y = hole_position_y
    self.goal_position_x = goal_position_x
    self.goal_position_y = goal_position_y

  def check_player_status(self, player):
    hole_length = 3
    goal_length = 1
    if (player.position_x > self.hole_position_x and player.position_x < self.hole_position_x + hole_length and player.position_y > self.hole_position_y and player.position_y < self.hole_position_y + hole_length) or player.position_x < 0 or player.position_x > self.length or player.position_y < 0 or player.position_y > self.length:
      return "gameover"  # gameover
    elif player.position_x > self.goal_position_x and player.position_x < self.goal_position_x + goal_length and player.position_y > self.goal_position_y and player.position_y < self.goal_position_y + goal_length:
      return "clear"  # clear
    else:
      return "playing"  # playing
