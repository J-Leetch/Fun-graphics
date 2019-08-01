float sigma = 10;
float beta = 8/3;
float rho = 28;
float x = 1;
float y = 1;
float z = 1;
float xdash = 0;
float ydash = 0;
float zdash = 0;
float px = 0;
float py = 0;
float pz = 0;
float dt = 0.01;
//float ang = 0;

float col = 0;
float c = 0;


void setup() {
  size(1200,700,P3D);
  background(0);
  
}

void draw() {
  translate(width/2, height/2, 0);
  lights();
  scale(5);
  xdash = sigma * (y - x);
  ydash = x * (rho - z) - y;
  zdash = x * y - beta * z;
  x += dt * xdash;
  y += dt * ydash;
  z += dt * zdash;
  colorMode(HSB,255,255,255);
  line(x, y, z, px, py, pz);
  stroke(col,255,255);
  strokeWeight(0.2);
  if (col<255) {
    col++; 
  } else {
    col = 0;
  }
  
  px = x;
  py = y;
  pz = z;
}