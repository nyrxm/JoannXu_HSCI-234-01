import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)           # white background
    
    p5.noStroke()  # <3<3<3
    p5.fill(200, 0, 0)
    for i in range(10):
        p5.arc(i * 60 , 30, 20, 20, 3.14, 0)
        p5.arc(i * 60 + 20, 30, 20, 20, 3.14, 0)
        p5.triangle(i * 60 - 10, 30, i* 60 + 30, 30, i * 60 + 10, 50)
        p5.arc(i * 60 , 260, 20, 20, 3.14, 0)
        p5.arc(i * 60 + 20, 260, 20, 20, 3.14, 0)
        p5.triangle(i * 60 - 10, 260, i* 60 + 30, 260, i * 60 + 10, 280)

    p5.fill(240, 200, 200)  # pink body part
    p5.arc(100, 100, 50, 50, 3.14, 0)
    p5.arc(200, 100, 50, 50, 3.14, 0)
    p5.rect(75, 100, 50, 25)
    p5.rect(175, 100, 50, 25)
    p5.rect(75, 125, 150, 75)
    p5.arc(75, 175, 75, 50, 1.57, -1.57)

    p5.strokeWeight(5)  # UwU eyes
    p5.stroke(0)
    p5.arc(110, 150, 50, 60, 3.14, 0)
    p5.arc(185, 150, 50, 60, 3.14, 0)
    p5.fill(0)
    p5.ellipse(120, 160, 30, 60)
    p5.ellipse(195, 160, 30, 60)
    p5.fill(255)
    p5.noStroke()
    p5.ellipse(130, 160, 5, 10)
    p5.ellipse(205, 160, 5, 10)

    p5.noFill()  # UwU mouth
    p5.strokeWeight(3)
    p5.stroke(100, 50, 50)
    p5.line(140, 175, 145, 180)
    p5.line(145, 180, 150, 175)
    p5.line(150, 175, 155, 180)
    p5.line(155, 180, 160, 175)

    p5.strokeWeight(1)  #  hands
    p5.stroke(0)
    p5.fill(255, 255, 255)
    p5.ellipse(135, 200, 25, 25)
    p5.ellipse(165, 200, 25, 25)

    p5.strokeWeight(6)  #  blush
    p5.stroke(255, 0, 0)
    p5.noFill(0)
    for i in range(3):
        p5.line(75 + i * 10, 165, 60 + i * 10, 185)
        p5.line(215 + i * 10, 165, 200 + i * 10, 185)
