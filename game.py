import pygame
pygame.init()

back = (200, 255, 255)
mw = pygame.display.set_mode((500,500))
mw.fill(back)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0,y=0, width=10, height=10, color=None ):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_color = back
        if color:
            self.fill_color = colo
    def color(self,new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x,y)
    def colliderect(self,rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self,filename, x = 0, y = 0,width=10, height=10):
        Area.__init__(self, x = x, y = y, width = width, height = height, color = None)
        self.image = pygame.image.load(filename)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont("verdana" , fsize).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))



game over = False

while not game_over:
    pygame.display.upadate()
    clock.tick(40)



ball = Picture("мяч-removebg-preview (1).png", 160, 200, 50, 50)

platform1 = Picture("Mars_Preview_9-removebg-preview (1).png", racket_x, racket_y, 100, 30)

platform2 = Picture("Mars_Preview_9-removebg-preview (1).png", racket_x, racket_y, 100, 30)


score_text = Label(300, 0 ,50, 50, bask)
score_text.set_text("Рахунок 🀄", 45, BLACK)
score_text.draw(20,20)
score = Label(430, 55 ,50, 40, bask)
score.set_text("0", 40, BLACK)
score.draw(20,20)
wait = 0

start_time = time.time()
cur_time = start_time


time_text = Label(0, 0 ,50, 50, bask)
time_text.set_text("ЧАС ⏱️", 45, BLACK)
time_text.draw(20,20)

timer = Label(50, 55 ,50, 40, bask)
timer.set_text("0", 40, BLACK)
timer.draw(0,0)




