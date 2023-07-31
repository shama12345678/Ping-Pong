import pygame 
from pygame import font
font.init()
pygame.init()

back = (0, 0, 0) 
mw = pygame.display.set_mode((900, 700)) 
clock = pygame.time.Clock() 
dx = 8 
dy = 8
score_1 = 0
score_2 = 0

platform_x = 200 
platform_y = 550 
move_right = False 
move_left = False 
move_up = False
move_down = False
game_over = False 
move_A = False
move_D = False


class Area(): 
  def __init__(self, x=0, y=0, width=10, height=10, color=None): 
      self.rect = pygame.Rect(x, y, width, height) 
      self.fill_color = back 
      if color: 
          self.fill_color = color 
  def color(self, new_color): 
      self.fill_color = new_color 
  def fill(self): 
      pygame.draw.rect(mw, self.fill_color, self.rect) 
  def collidepoint(self, x, y): 
      return self.rect.collidepoint(x, y)       
  def colliderect(self, rect): 
      return self.rect.colliderect(rect)
   
 
class Label(Area): 
  def set_text(self, text, fsize=12, text_color=(0, 0, 0)): 
      self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color) 
  def draw(self, shift_x=0, shift_y=0): 
      self.fill() 
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) 
 
 
class Picture(Area): 
  def __init__(self, filename, x=0, y=0, width=10, height=10): 
      Area.__init__(self, x=x, y=y, width=width, height=height, color=None) 
      self.image = pygame.image.load(filename) 
     
  def draw(self): 
      mw.blit(self.image, (self.rect.x, self.rect.y)) 

platform_1 = Picture('platform-removebg-preview (1).png', 300, 550, 200, 120)
platform_2 = Picture('platform-removebg-preview (1).png', 300, -20, 200, 120)
ball = Picture('ball-removebg-preview (1).png', 380, 350, 5, 5) 
image = pygame.image.load('bg5.jpg')
game_over = False
finish = False
while not game_over: 
  if not finish:
    ball.fill()
    platform_1.draw()
    platform_2.draw()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            game_over = True 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_RIGHT: 
                move_right = True 
            if event.key == pygame.K_LEFT: 
                move_left = True
            if event.key == pygame.K_a: 
                move_A = True 
            if event.key == pygame.K_d: 
                move_D = True
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT: 
                move_right = False 
            if event.key == pygame.K_LEFT: 
                move_left = False 
            if event.key == pygame.K_a: 
                move_A = False 
            if event.key == pygame.K_d: 
                move_D = False 
    mw.blit(image, (0,0))

    if move_right and platform_1.rect.x < 680: 
        platform_1.rect.x +=10 
    if move_left and platform_1.rect.x > -50: 
        platform_1.rect.x -=10
    if move_A and platform_2.rect.x > -50: 
        platform_2.rect.x -=10 
    if move_D and platform_2.rect.x < 680: 
        platform_2.rect.x +=10


    font1 = font.Font(None, 50)
    tex = str(score_1) + ':' + str(score_2)
    score_text = font1.render(tex, True, (255, 255, 255))
    mw.blit(score_text, (10, 10))
    ball.rect.x -= dx 
    ball.rect.y -= dy 
    if  ball.rect.y < 0:
        score_2 += 1
        ball.rect.y = 350
        ball.rect.x = 380
    if ball.rect.x > 850 or ball.rect.x < 0:
        dx *= -1 
    if ball.rect.y >= 650:
        score_1 += 1
        ball.rect.y = 350
        ball.rect.x = 380
    if ball.rect.colliderect(platform_1.rect): 
        dy *= -1 
    if ball.rect.colliderect(platform_2.rect): 
        dy *= -1 
    if score_1 == 10:
        win_text_1 = font1.render('Player 1 WIN!', True, (0, 255, 0))
        mw.blit(win_text_1, (300, 300))
        finish = True
    if score_2 == 10:
        win_text_2 = font1.render('Player 2 WIN!', True, (0, 255, 0))
        mw.blit(win_text_2, (300, 300))
        finish = True
    
    ball.draw() 
    platform_1.draw()
    platform_2.draw()
    pygame.display.update() 
    clock.tick(60)
