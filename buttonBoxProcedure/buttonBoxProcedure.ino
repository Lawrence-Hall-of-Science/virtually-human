#include <Keyboard.h>  //for assigning specific keystrokes to the button

const int button1 = 1;  //Assigned button pin numbers
const int button2 = 2;
const int button3 = 3;
const int button4 = 4;

int spaceBar = HIGH;  //INPUT PULLUP sets all button pins to HIGH
int fKey = HIGH;
int leftArrow = HIGH;
int rightArrow = HIGH;
int upArrow = HIGH;
int downArrow = HIGH;
int gKey = HIGH;

unsigned long startRestartPushTime = 0; //initializes the counter for all buttons
unsigned long leftPushTime = 0; 
unsigned long rightPushTime = 0;
unsigned long selectPushTime = 0;
unsigned long freezePushTime = 0;
unsigned long tellMorePushTime = 0;
unsigned long stealMyFacePushTime = 0;
unsigned long instructionsPushTime = 0;
unsigned long nextRoundPushTime = 0;

void setup() {
  pinMode(button1, INPUT_PULLUP);  //pin input is default HIGH
  pinMode(button2, INPUT_PULLUP);
  pinMode(button3, INPUT_PULLUP);
  pinMode(button4, INPUT_PULLUP);
}

void loop() { //UNCOMMENT whichever function you want to use
  // teachMeSilly();
  // mirrorMirror();
  // comedyCorner();
  // faceSwap();
  // letsMakePlan();
  learningTrialError();
}


void teachMeSilly() {
  int startRestartLockout = 3000;
  spaceBar = digitalRead(button1);
  if (spaceBar == LOW && millis() - startRestartPushTime > startRestartLockout){
    Keyboard.write(' ');
    startRestartPushTime = millis();
  }
}
void mirrorMirror() {
  int startRestartLockout = 3000;
  spaceBar = digitalRead(button1);
  if (spaceBar == LOW && millis() - startRestartPushTime > startRestartLockout){
    Keyboard.write(' ');
    startRestartPushTime = millis();
  }
}
void comedyCorner() {
  int startRestartLockout = 3000;
  spaceBar = digitalRead(button1);
  if (spaceBar == LOW && millis() - startRestartPushTime > startRestartLockout){
    Keyboard.write(' ');
    startRestartPushTime = millis();
  }
}

void faceSwap() {
  int freezeLockout = 500;
  int tellMoreLockout = 2000;
  int stealMyFaceLockout = 1000;
  fKey = digitalRead(button1);
  spaceBar = digitalRead(button2);
  gKey = digitalRead(button3);
  if (fKey == LOW && spaceBar == HIGH && gKey == HIGH && millis() - freezePushTime > freezeLockout){
    Keyboard.write('f');
    freezePushTime = millis();
  }
  if (fKey == HIGH && spaceBar == LOW && gKey == HIGH && millis() - tellMorePushTime > tellMoreLockout){
    Keyboard.write(' ');
    tellMorePushTime = millis();
  }
  if (fKey == HIGH && spaceBar == HIGH && gKey == LOW && millis() - stealMyFacePushTime > stealMyFaceLockout){
    Keyboard.write('g');
    stealMyFacePushTime = millis();
  }
}

void letsMakePlan() {
  int startRestartLockout = 3000;
  int leftLockout = 10;
  int rightLockout = 10;
  int selectLockout = 10;
  spaceBar = digitalRead(button1);    //start/Restart button label
  leftArrow = digitalRead(button2);   //left button label
  rightArrow = digitalRead(button3);  //right button label
  fKey = digitalRead(button4);        //select button label

  if (spaceBar == LOW && leftArrow == HIGH && rightArrow == HIGH && fKey == HIGH && millis() - startRestartPushTime > startRestartLockout) {
    Keyboard.write(' ');
    startRestartPushTime = millis();
  }
  if (spaceBar == HIGH && leftArrow == LOW && rightArrow == HIGH && fKey == HIGH && millis() - leftPushTime > leftLockout) {
    Keyboard.press(KEY_LEFT_ARROW);
    Keyboard.releaseAll();
    leftPushTime = millis();
  }
  if (spaceBar == HIGH && leftArrow == HIGH && rightArrow == LOW && fKey == HIGH && millis() - rightPushTime > rightLockout) {
    Keyboard.press(KEY_RIGHT_ARROW);
    Keyboard.releaseAll();
    rightPushTime = millis();
  }
  if (spaceBar == HIGH && leftArrow == HIGH && rightArrow == HIGH && fKey == LOW && millis() - selectPushTime > selectLockout) {
    Keyboard.write('f');
    selectPushTime = millis();
  }
}

void learningTrialError() {
  int instructionsLockout = 500;
  int startRestartLockout = 500;
  int nextRoundLockout = 500;
  leftArrow = digitalRead(button1);
  upArrow = digitalRead(button2);
  downArrow = digitalRead(button3);

  if (leftArrow == LOW && downArrow == HIGH && upArrow == HIGH && millis() - instructionsPushTime > instructionsLockout){
    Keyboard.press(KEY_LEFT_ARROW);
    Keyboard.releaseAll();
    instructionsPushTime = millis();
  }
  if (leftArrow == HIGH && downArrow == LOW && upArrow == HIGH && millis() - startRestartPushTime > startRestartLockout){
    Keyboard.press(KEY_DOWN_ARROW);
    Keyboard.releaseAll();
    startRestartPushTime = millis();
  }
  if (leftArrow == HIGH && downArrow == HIGH && upArrow == LOW && millis() - nextRoundPushTime > nextRoundLockout){
    Keyboard.press(KEY_UP_ARROW);
    Keyboard.releaseAll();
    nextRoundPushTime = millis();
  }
}
