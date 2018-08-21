from field import field
from player import player
import csv

def main():
  #initialize field and player
  base_field = field()
  base_player = player()
  history = []
  turn = 0

  while(base_field.check_player_status(base_player) == "playing"):
    history.append(base_player.position_x)
    history.append(base_player.position_y)
    situation = [base_player.position_x,base_player.position_y]
    base_player.move(situation)
    turn += 1
    print("player's position: ({},{})".format(base_player.position_x,base_player.position_y))
  
  if(base_field.check_player_status(base_player) == "clear"):
    print("clear")
    print(turn)
    with open("output.csv","w") as f:
      writer = csv.writer(f, lineterminator='\n')
      writer.writerow(history)
  else:
    print("gameover")


if __name__ == '__main__':
    main()
