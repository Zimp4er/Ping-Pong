from random import *
from pygame import *
FPS = 60
lost = 0
score = 0
max_lost = 3
speed = 10
win_width = 700
win_height = 500
life = 5
speed_x = 5
speed_y = 5
clock = time.Clock()
mixer.init()
mixer.music.load('space.ogg')
fire_sound = mixer.Sound("fire.ogg")
mixer.music.play()
font.init()
font1 = font.Font(None, 36)
lose = font1.render("Ты проиграл", 20 , (255, 255, 255))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += speed

window = display.set_mode((700,500))
display.set_caption('Ping_Pong')
background = transform.scale(image.load('12834.jpg'), (700,500))

player = Player2('Stick.png', -15, 250, 5)
player2 = Player('Stick.png', 650, 250, 5)
ball = GameSprite('images.png', 250, 350, 5)
game = True
finish = False
while game:
    
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        player.reset()
        player2.reset()
        player.update()
        ball.reset()
        ball.update()
        ball.reset()
        player2.update()
        clock.tick(FPS)
        display.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height -50 or ball.rect.y <0:
            speed_y *= -1
        if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1