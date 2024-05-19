# MakeCode Python 

def on_gesture_shake():   #When shake gesture is detected this function will be called
  basic.clear_screen()
   #randomly select an led to turn on. This process is repeated 30 times to see more number of leds and minimise the chances of seeing lesser leds due to same led being sleected more than once
  for index in range(30):
    led.plot_brightness(randint(0, 5), randint(0, 5), 255)  
  basic.pause(2000)
  basic.clear_screen()
  
input.on_gesture(Gesture.Shake, on_gesture_shake) # calls the function on shaking
      
def on_forever():
  #Reading acceleration data on X and Y axes and showing corresponding output
  if input.acceleration(Dimension.Y) < -400:
    basic.show_leds("""
    # # # # #
    . # # # .
    . . # . .
    . . . . .
    . . . . .
    """)
  elif input.acceleration(Dimension.Y) > 400:
    basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . # # # .
    # # # # #
    """)
  elif input.acceleration(Dimension.X) > 400:  #To check if the board is titled to the right by an extent of more than 400 ie a barrier to detect tilt
    basic.show_leds("""
    . . . . #
    . . . # #
    . . # # #
    . . . # #
    . . . . #
    """)
  elif input.acceleration(Dimension.X) < -400:
    basic.show_leds("""
    # . . . .
    # # . . .
    # # # . .
    # # . . .
    # . . . .
    """)
  elif input.acceleration(Dimension.X) < -100 and input.acceleration(Dimension.Y) <-100:  #To check is the board is tilted a LIITLE bit to left AND LITTLE behind ie in northwest direction 
    basic.show_leds("""
    # # # . .
    # # . . .
    # . . . .
    . . . . .
    . . . . .
    """)
  elif input.acceleration(Dimension.X) < -100 and input.acceleration(Dimension.Y) >100:
    basic.show_leds("""
    . . . . .
    . . . . .
    # . . . .
    # # . . .
    # # # . .
    """)
  elif input.acceleration(Dimension.X) > 100 and input.acceleration(Dimension.Y) <-100:
    basic.show_leds("""
    . . # # #
    . . . # #
    . . . . #
    . . . . .
    . . . . .
    """)
  elif input.acceleration(Dimension.X) > 100 and input.acceleration(Dimension.Y) > 100:
    basic.show_leds("""
    . . . . .
    . . . . .
    . . . . #
    . . . # #
    . . # # #
    """)
  else:
    basic.show_icon(IconNames.Happy) #When no acc is detected ie board is flat
    
basic.forever(on_forever)


