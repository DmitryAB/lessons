import pygame, random, sys

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, color2, width, height):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.colorFront = color2
        pygame.draw.ellipse(self.image, self.colorFront, self.rect)
        

class Field: 
   
    def __init__(self):
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.screen_width = self.screen_height = 400
        self.screen=pygame.display.set_mode([self.screen_width,self.screen_height])
        self.block_list = pygame.sprite.RenderPlain()
        self.all_sprites_list = pygame.sprite.RenderPlain()
    
    def createBlocks(self):
        for i in range(5):
            for j in range(20):
                block = Block(self.black, 19, 14)
 
                block.rect.x = j*20
                block.rect.y = i*15

                self.block_list.add(block)
                self.all_sprites_list.add(block)

    def createPlayer(self):
        self.player = Block(self.red, 60, 15) #Player object
        self.all_sprites_list.add(self.player)
        self.player.rect.y = self.screen_height-15

    def createBall(self):
        self.ball = Ball(self.white,self.red,10,10)
        self.all_sprites_list.add(self.ball)
        self.ball.rect.x = self.screen_width/2+random.randint(-10,10)
        self.ball.rect.y = self.screen_height/3
        self.ball_change_x = 7*random.choice((-1,1))
        self.ball_change_y = 7*random.choice((-1,1))

    def mainLoop(self):
        self.clock=pygame.time.Clock()
        while 1:
           self.reboundBall()
           self.moveBallAndPlayer()
           self.collideBall()
           self.fillAndDraw()
           self.quit()
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

    def reboundBall(self):
        if self.ball.rect.x >390 or self.ball.rect.x<0: self.ball_change_x*=-1 #size
        if self.ball.rect.y<0: self.ball_change_y*=-1
        if self.ball.rect.y>400: pygame.quit()

    def moveBallAndPlayer(self):
        self.ball.rect.x += self.ball_change_x
        self.ball.rect.y += self.ball_change_y
        self.player.rect.x = pygame.mouse.get_pos()[0]

    def collideBall(self):
        if pygame.sprite.spritecollideany(self.ball, self.block_list) or pygame.sprite.collide_rect(self.ball,self.player):
            self.ball_change_y*=-1
        pygame.sprite.spritecollide(self.ball, self.block_list, True)

    def fillAndDraw(self):
        self.screen.fill(self.white)
        self.all_sprites_list.draw(self.screen)
        pygame.display.flip() 
        self.clock.tick(24)

    def createAll(self):
        self.createBlocks()
        self.createPlayer()
        self.createBall()

class FieldA(Field):
    def __init__(self):
        super().__init__()
        self.red = self.black = (0,255,0)
        self.white = (0,0,0)

class FieldB(FieldA):
    def __init__(self):
        super().__init__()
        self.red = self.black = (255,255,255)

class FieldHard(Field):

    def createBall(self):
        super().createBall()
        self.ball2 = Ball(self.white,self.red,10,10)
        self.all_sprites_list.add(self.ball2)
        self.ball2.rect.x = self.screen_width/2+random.randint(-10,10)
        self.ball2.rect.y = self.screen_height/3
        self.ball2_change_x =10*random.choice((-1,1)) #delete?
        self.ball2_change_y =10*random.choice((-1,1))

    def reboundBall(self):
        super().reboundBall()
        if self.ball2.rect.x >390 or self.ball2.rect.x<0: self.ball2_change_x*=-1 #size
        if self.ball2.rect.y<0: self.ball2_change_y*=-1
        if self.ball2.rect.y>400: pygame.quit()

    def moveBallAndPlayer(self):
        super().moveBallAndPlayer()
        self.ball2.rect.x += self.ball2_change_x
        self.ball2.rect.y += self.ball2_change_y
       # self.player.rect.x = pygame.mouse.get_pos()[0] #delete?

    def collideBall(self):
        super().collideBall()
        if pygame.sprite.spritecollideany(self.ball2, self.block_list) or pygame.sprite.collide_rect(self.ball2,self.player):
            self.ball2_change_y*=-1
        pygame.sprite.spritecollide(self.ball2, self.block_list, True)

class FieldHardest(Field):
    def createBall(self):
        super().createBall()
        self.ball_change_x =12*random.choice((-1,1)) #delete?
        self.ball_change_y =12*random.choice((-1,1))

    def createPlayer(self):
        self.player = Block(self.red, 30, 15)
        self.all_sprites_list.add(self.player)
        self.player.rect.y = self.screen_height-15

class FieldFactory: 
    def __init__(self):
        self.style = {
        'default':Field, 'green':FieldA,
        'white':FieldB, 'hard':FieldHard,
        'hardest':FieldHardest
        }
    def get_style(self, style): #if comp in complexity{}?
        if style in self.style:
            return self.style[style]() #() - init
        return self.style['default']()

class Application:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
             cls.instance = super(Application, cls).__new__(cls)
        return cls.instance

    def __init__(self): 
        f = FieldFactory().get_style(sys.argv[1] if len(sys.argv)>1 else 'default')
        f.createAll()
        f.mainLoop()

Application()

