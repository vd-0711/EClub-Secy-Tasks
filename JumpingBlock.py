# Python code

obsP = -1 #1 in first two columns
blockP = -1 #0 in air, 1 on ground

def obstacle(x: int): #plots the obstacle starting from the given x position
  for i in range(3):
    led.plot(x, 2+i)
  led.plot(x+1,3)
  if(x==0 or x==1): obsP = 1  #to save the location of the obstacle, needed to check for collisions
  else : obsP = 0
  

def obstacleUnplot(x: int):  #turns of the leds of the obstacle without clearing entire screen so that the next obstacle can be plotted
  for i in range(3):
    led.unplot(x, 2+i)
  led.unplot(x+1,3)

def block(x: int): #plots the block(2x2 square) -- plots in air if x=0 and on ground if x=1
  for i in range(2):
    for j in range(2):
      led.plot(i,j+(x*3))
  if(x): blockP = 1
  else: blockP = 0

def blockUnplot(x: int): #turns of the leds of the block without clearing entire screen
  for i in range(2):
    for j in range(2):
      led.unplot(i,j+(x*3))
    
def on_button_pressed_a(): #to make the block jump
  blockUnplot(1)
  block(0)
  basic.pause(1200)
  blockUnplot(0)
  block(1)

def collide(): # to check if obstacle and block are at the same position, if yes game ends #need to check this
  if(obsP==1 and blockP==1):
  		basic.clear_screen()
  		basic.show_icon(IconNames.No)
  		basic.show_icon(IconNames.Sad)
 
def on_forever():
  block(1)
  input.on_button_pressed(Button.A, on_button_pressed_a)
  for i in range(4): # 0,1,2,3
    obstacle(3-i) 
    collide()
    basic.pause(500)
    obstacleUnplot(3-i)
    
basic.show_string("Dino")
basic.forever(on_forever)
