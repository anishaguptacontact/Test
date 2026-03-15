canvas_width = 1200
canvas_height = 600


def setup():
    #create a canvas with the specified width and heigth
    size (canvas_width, canvas_height)
    
    background(0)
    
    rows = 10
    cols = 10
    spacing = width / cols
    for y in range(rows):
        for x in range(cols):
            if random(1) < 0.2:
                fill(255, 0, 0)
            else :
                fill(255)
            ellipse (x * spacing + spacing / 2, y * spacing + spacing / 2, spacing * 0.8, spacing * 0.8)
