# canvas dimenstions
canvas_width = 1200
canvas_height = 600

game_state = ("PLAYING", "GAME_OVER")
current_game_state = game_state [0] 

states = ("UP", "RIGHT", "DOWN", "LEFT")
current_state = states [0]

x = 600
y = 300
move_x = 1
move_y = 0
speed = 1

def setup():
    #create a canvas with the specified width and heigth
    size (canvas_width, canvas_height)
    
    background(0)
    
def draw():
    global x, y, move_x, move_y, current_game_state
    
    if (current_game_state == game_state[0]):
        background(0)
        check_collision()
        #change_state()
    
        fill(255)
        noStroke()
    
        x += move_x
        y += move_y
    
        rect (x, y, 30, 30)
    elif (current_game_state == game_state[1]):
        background(255, 0, 0)
        textSize(40)
        fill(255)
        text("GAME OVER", 520, 300)
    


def mouseClicked():
    global speed
    change_state()
    speed += 1
    
def keyPressed():
    global current_state, move_x, move_y, speed
    speed += 1
    
    # Direct control using Arrow Keys
    if (key == CODED):
        if (keyCode == UP):
            current_state = states[0]
            move_x = 0
            move_y = -speed
        elif (keyCode == RIGHT):
            current_state = states[1]
            move_x = speed
            move_y = 0
        elif (keyCode == DOWN):
            current_state = states[2]
            move_x = 0
            move_y = speed
        elif (keyCode == LEFT):
            current_state = states[3]
            move_x = -speed
            move_y = 0
    
def check_collision():
    global x, y, canvas_width, canvas_height
    global current_game_state, game_state
    
    if (x > canvas_width):
        current_game_state = game_state[1]
    elif (x < 0):
        current_game_state = game_state1 [1]
    elif (y > canvas_height):
        current_game_state = game_state[1]
    elif (y < 0):
        current_game_state = game_state[1]
    
def change_state():
    global states, current_state, move_x, move_y, speed 
    
    if (current_state == states[0]): #UP
        current_state = states [1]
        move_x = 0
        move_y = -speed
    elif (current_state == states[1]): #RIGHT
        current_state = states [2]
        move_x = speed
        move_y = 0
    
    elif (current_state == states[2]): #DOWN
        current_state = states [3]
        move_x = 0
        move_y = speed
    elif (current_state == states[3]): #LEFT
        current_state = states [0]
        move_x = -speed
        move_y = 0
    
