Table a;
void setup(){
  size(400,400);
  a = loadTable("../output.csv");

}

void draw(){
  background(-1);
  translate(75,75);
  scale(25);
  strokeWeight(0.1);
  rect(0,0,10,10); // field
  rect(0,0,1,1); // start
  rect(9,9,1,1); //goal
  rect(2,2,3,3); //hole
  for(int i = 0;i < a.getColumnCount();i+=2){
   ellipse(a.getFloat(0,i),a.getFloat(0,i+1),0.5,0.5);
   if(i != 0){
     line(a.getFloat(0,i-2),a.getFloat(0,i-1),a.getFloat(0,i),a.getFloat(0,i+1));
   }
  }
}