from pygame import*
window = display.set_mode((500, 500))
display. set_caption("STRIKOZA")
back = (120, 153, 234)
window.fill (back)

clock = time.Clock()
FPS = 60

game = True

finish = False

class GameSprite(sprite.Sprite):
    def __init__(self, pImage, pX, pY, sizex, sizeY, pSpeed):

        super().__init__()

        self.image = transform. scale(image.load(pImage), (sizex, sizeY))
        self.speed = pSpeed

        self.rect = self.image .get_rect()
        self.rect.x = pX
        self.rect.y = pY

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
    def fire(self):

        bullet = Bullet("bullet.png", self.rect.centerx,self.rect.top,50,50,-15)
        bullets.add(bullet)
from random import *
lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global hearts
        global lost
        if self.rect.y >500:
            try:

                hearts.pop(0)
            except:
                pass
            self.rect.x = randint(0,600)
            self.rect.y = 0
            self.speed = randint(1,4)
            lost +=1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

bullets = sprite.Group()


rozetka = sprite.Group()
for i in range(1,3):
    randSPrite = randint(1,6)
    if randSPrite == 1:
        aterrot = Enemy("asteroid.png", randint(80, 600), -40, 50, 50, randint(1, 3))
        rozetka.add(aterrot)
    if randSPrite == 2:
        aterrot = Enemy("asteroid.png", randint(80, 600), -40, 50, 50, randint(1, 4))
        rozetka.add(aterrot)
    if randSPrite == 3:
        aterrot = Enemy("zombie2.png", randint(80, 600), -40, 50, 50, randint(1, 4))
        rozetka.add(aterrot)
    if randSPrite == 4:
        aterrot = Enemy("zombie3.png", randint(80, 600), -40, 50, 50, randint(1, 4))
        rozetka.add(aterrot)
    if randSPrite == 5:
        aterrot = Enemy("asteroid.png", randint(80, 600), -40, 50, 50, randint(1, 3))
        rozetka.add(aterrot)
    if randSPrite == 6:
        aterrot = Enemy("zombie4..png", randint(80, 600), -40, 50, 50, randint(1, 5))
        rozetka.add(aterrot)



rocket = Player("rocket.png", 20,400,85,90,4)
backround = transform.scale(image.load("bg.png"),(700,500))
menu = GameSprite("tab.png", 0,0,220,145,0)

mixer.init()
#mixer.music.load('mussic.ogg')
#mixer.music.play()
mixer.music.set_volume(0.3)
fire_sound = mixer.Sound('fire.ogg')
kill_sound = mixer.Sound('kill.ogg')

font.init()
mainfont = font.Font('VCR_OSD_MONO_1.001.ttf',40)
losefont = font.Font('luckiestguyrus_bel_ukr.otf',40)
score = 0

from time import time as timer
rel_time = False
num_fire = 0

hearts = []
hX = 300
for i in range(5):
    heart = GameSprite("heart.png",hX,10,40,40,0)
    hearts.append(heart)
    hX += 35
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 10 and rel_time == False:
                    num_fire += 1
                    fire_sound.play()
                    rocket.fire()
                if num_fire >= 10 and rel_time == False:
                    last = timer()
                    rel_time= True


    if not finish:
        window.blit(backround,(0,0.000000000000000000000000000000000000000001))
        score_text = mainfont.render("KILLED:"+str(score),True,(0,255,0))
        lose_text = mainfont.render("MISSED:" +str(lost), True,(255,0,0))
        menu.draw()
        menu.update()
        window.blit(score_text,(5,10))
        window.blit(lose_text,(5,60))
        rocket.draw()
        rocket.update()
        rozetka.update()
        rozetka.draw(window)

        bullets.update()
        bullets.draw(window)

        if rel_time:
            now_time = timer()
            if now_time - last <3:
                reload = mainfont.render("RELOAD...",True,(255, 170, 25))
                window.blit(reload, (250,400))
            else:
                num_fire = 0
                rel_time= False
        if len(hearts) == 0:
            print('Bombigt dombas')
            randfont = randint(1, 5)
            loser = losefont.render("death!", True, (255, 0, 0))
            window.blit(loser, (220, 220))
            kill_sound.play()
            finish = True

        collides = sprite.groupcollide(rozetka, bullets, True,True)
        if sprite.spritecollide(rocket,rozetka, False):
            loser = losefont.render("ooops!", True, (255, 0, 0))
            window.blit(loser, (220, 220))
            kill_sound.play()
            finish = True



        for heart in hearts:
            heart.draw()
        for c in collides:
            score+=1
            randSPrite = randint(1, 6)
            if randSPrite == 1:
                aterrot = Enemy("asteroid.png", randint(80, 600), -40, 50, 50, randint(1, 3))
                rozetka.add(aterrot)
            if randSPrite == 2:
                aterrot = Enemy("asteroid.png", randint(80, 600), -40, 50, 50, randint(1, 4))
                rozetka.add(aterrot)
            if randSPrite == 3:
                aterrot = Enemy("zombie2.png", randint(80, 600), -40, 50, 50, randint(1, 4))
                rozetka.add(aterrot)
            if randSPrite == 4:
                aterrot = Enemy("zombie3.png", randint(80, 600), -40, 50, 50, randint(1, 4))
                rozetka.add(aterrot)
            if randSPrite == 5:
                aterrot = Enemy("asteroid.png", randint(80, 600), -40, 50, 50, randint(1, 3))
                rozetka.add(aterrot)
            if randSPrite == 6:
                aterrot = Enemy("zombie4..png", randint(80, 600), -40, 50, 50, randint(1, 5))
                rozetka.add(aterrot)
        if rocket.rect.x >= 435:
            rocket.rect.x = 435
        if rocket.rect.x <= 0:
            rocket.rect.x = 0



    display.update()
    clock.tick(FPS)