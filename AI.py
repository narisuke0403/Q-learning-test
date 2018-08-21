class AI:
  def __init__(self,_situation ,*args, **kwargs):
    # information of player's position
    #_situation[0] : player's position x
    #_situation[1] : player's position y
    self.sitiation = _situation
    pass

  def decision(self):
    #x,y = self._thinking()
    x,y = self._sample()
    if(x**2 + y**2 > 1):
      return "value Error"
    else:
      return x,y

  # describe base of AI
  def _thinking(self):
    return 0,0

  #sample of Pure MonteCarlo
  def _sample(self):
    from field import field
    from player import player
    from math import cos,sin,radians,sqrt
    from random import random,randint
    template_field = field()
    score = -100
    action = [0,0]
    #Number of trials : 100
    for i in range(100):
      template_player = player(self.sitiation[0], self.sitiation[1])
      template_score = 0
      #Search depth
      for t in range(5):
        d = random()  # Moving radius
        r = radians(randint(0,359))
        if(t == 0):
          template_action = [d*cos(r), d*sin(r)]
        template_player.simulation_move(d*cos(r), d*sin(r))
        if(template_field.check_player_status(template_player) == "gameover"):
          break

      #Evaluation value
      state = template_field.check_player_status(template_player)
      if(state == "gameover"):
        template_score = -100
      elif(state == "playing"):
        GOAL_POSITION_X = 9.5
        GOAL_POSITION_Y = 9.5
        template_score = -sqrt((GOAL_POSITION_X-template_player.position_x)** 2 + (GOAL_POSITION_Y-template_player.position_y) ** 2)
      else:
        template_score = 1
      #update
      if(score < template_score):
        score = template_score
        action = template_action
        
    return action[0],action[1]
