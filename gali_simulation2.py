import pygame
import sys
import math
pygame.init()
pygame.mouse.set_visible(True)
font = pygame.font.Font("freesansbold.ttf", 32)


clock = pygame.time.Clock()
window = pygame.display.set_mode([800,600])
background_color = pygame.Color(240,25,255)

class Ball:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 10
        self.color = pygame.Color(0,0,0)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

ball = Ball()










class Ball2:
    def __init__(self):
        self.x = 500
        self.y = 300
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 10
        self.color = pygame.Color(0,0,0)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

ball2 = Ball2()





class Ball3:
    def __init__(self):
        self.x = 615
        self.y = 200
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 10
        self.color = pygame.Color(0,0,0)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

ball3 = Ball3()






class Ball4:
    def __init__(self):
        self.x = 615
        self.y = 400
        self.velocity_x = 0
        self.velocity_y = 0
        self.size = 10
        self.color = pygame.Color(0,0,0)

    def update(self):
        
        self.x += self.velocity_x
        self.y += self.velocity_y

        self.velocity_x *= 0.99
        self.velocity_y *= 0.99

        self.x = int(self.x)
        self.y = int(self.y)

        if (self.x > 800):
            self.velocity_x *=-1
        if (self.x < 0):
            self.velocity_x = self.velocity_x * -1

        if (self.y < 0):
            self.velocity_y *=-1
        if (self.y > 600):
            self.velocity_y *=-1
        
    def draw(self, window):
        pygame.draw.circle(window, self.color, [self.x, self.y], self.size)

ball4 = Ball4()








while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit

    window.fill(background_color)

    mouse_pos = pygame.mouse.get_pos()
    msg = "%i %i" %(mouse_pos[0],mouse_pos[1])
    text = font .render(msg, False, pygame.Color(0,0,0))
    window.blit(text,[0,0])


#ball 1
    if (pygame.mouse.get_pressed()[0] == True):
        #move to origin
        origin_mouse_x = mouse_pos[0] - ball.x
        origin_mouse_y = mouse_pos[1] - ball.y
        #find distance to origin (pythagorean)
        distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)

        #normalize
        normal_mouse_x = origin_mouse_x / distance
        normal_mouse_y = origin_mouse_y / distance

        #invert normal
        #normal_mouse_x *=-1
        #normal_mouse_y *=-1

        #move ball away from cursor, using the inverted normal
        ball.velocity_x += normal_mouse_x * 2.5
        ball.velocity_y += normal_mouse_y * 2.5


#ball 2
    if (pygame.mouse.get_pressed()[0] == True):
        #move to origin
        origin_mouse_x = mouse_pos[0] - ball2.x
        origin_mouse_y = mouse_pos[1] - ball2.y
        #find distance to origin (pythagorean)
        distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)

        #normalize
        normal_mouse_x = origin_mouse_x / distance
        normal_mouse_y = origin_mouse_y / distance

        #invert normal
        #normal_mouse_x *=-1
        #normal_mouse_y *=-1

        #move ball away from cursor, using the inverted normal
        ball2.velocity_x += normal_mouse_x * 2.5
        ball2.velocity_y += normal_mouse_y * 2.5

#ball 3
    if (pygame.mouse.get_pressed()[0] == True):
        #move to origin
        origin_mouse_x = mouse_pos[0] - ball3.x
        origin_mouse_y = mouse_pos[1] - ball3.y
        #find distance to origin (pythagorean)
        distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)

        #normalize
        normal_mouse_x = origin_mouse_x / distance
        normal_mouse_y = origin_mouse_y / distance

        #invert normal
        #normal_mouse_x *=-1
        #normal_mouse_y *=-1

        #move ball away from cursor, using the inverted normal
        ball3.velocity_x += normal_mouse_x * 2.5
        ball3.velocity_y += normal_mouse_y * 2.5

#ball 4
    if (pygame.mouse.get_pressed()[0] == True):
        #move to origin
        origin_mouse_x = mouse_pos[0] - ball4.x
        origin_mouse_y = mouse_pos[1] - ball4.y
        #find distance to origin (pythagorean)
        distance = math.sqrt(origin_mouse_x * origin_mouse_x + origin_mouse_y * origin_mouse_y)

        #normalize
        normal_mouse_x = origin_mouse_x / distance
        normal_mouse_y = origin_mouse_y / distance

        #invert normal
        #normal_mouse_x *=-1
        #normal_mouse_y *=-1

        #move ball away from cursor, using the inverted normal
        ball4.velocity_x += normal_mouse_x * 2.5
        ball4.velocity_y += normal_mouse_y * 2.5

     






    
    ball.update()
    ball.draw(window)

    ball2.update()
    ball2.draw(window)

    ball3.update()
    ball3.draw(window)

    ball4.update()
    ball4.draw(window)

    
    
    pygame.display.update()
    clock.tick(30)
