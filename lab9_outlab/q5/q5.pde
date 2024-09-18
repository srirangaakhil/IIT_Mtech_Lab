float h = 0;  
float s = 255;
float b = 255;
float bgColor = color(h, s, b);
int i=0;

void setup() {
  size(640, 360);
  background(0);
}

void draw() {
  stroke(255);
  if (mousePressed && (mouseButton == RIGHT)) {
    line(mouseX, mouseY, pmouseX, pmouseY);
  } else if (mousePressed && (mouseButton == LEFT)) {
      stroke(bgColor);
  line(pmouseX, pmouseY, mouseX, mouseY);
  } 
  if (keyPressed == true && key == '+')
  {
    i=i+2;
   strokeWeight(i);
  }
  if (keyPressed == true && key == '-')
  {
    i=i-2;
    if(i<0)
    {i=0;}
   strokeWeight(i);
  }
}