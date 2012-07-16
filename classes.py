import pygame, random, sys

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, color, color2, width, height, surface):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.colorFront = color2
        pygame.draw.ellipse(self.image, self.colorFront, self.rect)
        surface.all_sprites_list.add(self)
        self.rect.x = surface.screen_width/2+random.randint(-10,10)
        self.rect.y = surface.screen_height/3
        self.ball_change_x = 7*random.choice((-1,1))
        self.ball_change_y = 7*random.choice((-1,1))
        self.surface = surface

    def move(self):
        self.rect.x += self.ball_change_x
        self.rect.y += self.ball_change_y 
        if self.rect.x >390 or self.rect.x<0: self.ball_change_x*=-1 
        if self.rect.y<0: self.ball_change_y*=-1
        if self.rect.y>400: pygame.quit()
        self.collideBall()

    def collideBall(self): 
        if pygame.sprite.spritecollideany(self, self.surface.block_list) \
 or pygame.sprite.collide_rect(self, self.surface.player):
            self.ball_change_y*=-1
        pygame.sprite.spritecollide(self, self.surface.block_list, True)
        
class Player(Block):

    def __init__(self, color, width, height,surface):
        Block.__init__(self, color, width, height)
        self.rect.y = surface.screen_height-height
        surface.all_sprites_list.add(self)

    def move(self):
        self.rect.x = pygame.mouse.get_pos()[0]
        

class Blocks:
    def __init__(self,color, surface, width=19,height=14):
        for i in range(5):
            for j in range(20):
                block = Block(color, width, height)
 
                block.rect.x = j*20
                block.rect.y = i*15

                surface.block_list.add(block) 
                surface.all_sprites_list.add(block) 
        
class Screen:
    def __init__(self,color):
         self.color = color
         self.block_list = pygame.sprite.RenderPlain()
         self.all_sprites_list = pygame.sprite.RenderPlain()
         self.screen_width, self.screen_height = 400,400
         self.screen=pygame.display.set_mode([self.screen_width,self.screen_height])

    def mainLoop(self,player,ball):
        self.clock=pygame.time.Clock()
        self.ball = ball
        self.player = player
        while 1:
            #another game objects & logic
            player.move()
            ball.move()
            self.quit()
            self.fillAndDraw()
            self.clock.tick(24)

    def quit(self):
         for event in pygame.event.get():
             if event.type == pygame.QUIT: pygame.quit()
   
    def fillAndDraw(self):
        self.screen.fill(self.color)
        self.all_sprites_list.draw(self.screen)
        pygame.display.flip() 

s = Screen((255,255,255))
p = Player((0,0,0),100,12,s)
b = Ball((100,0,0),(0,100,0),20,20,s)
bs = Blocks((0,0,0),s)
s.mainLoop(p,b)
