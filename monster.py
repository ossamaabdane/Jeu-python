
import pygame
import random
import animation

class Monster(animation.AnimateSprite):  
    
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.health = 95
        self.max_health = 100
        self.attack = 1
        self.game = game
        self.offset = offset
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()
        self.score_amount = 10


    def set_score_amount(self, points):
        self.score_amount = points

    def set_speed(self, speed):
        self.defaul_speed = speed
        self.velocity = random.randint(1, speed)
        

    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 90
            self.velocity = random.randint(1,self.defaul_speed)
            self.rect.x = 1000 + random.randint(0, 300)
            self.rect.y = 540 - self.offset
            
            self.game.add_score(self.score_amount)
            
            if self.game.comet_event.is_full():
                self.game.all_monsters.remove(self)
                   
                self.game.comet_event.attempt_fall()
                
                
    def update_animation(self):
        self.animate(loop=True)


    def update_health_bar(self, surface):
        bar_color = (110,210,45)
        back_bar_color = (60,60,60)
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
      
            
class Mummy(Monster):
    
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_score_amount(20)
  
        
class Alien(Monster):
    
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)      
        self.health = 250
        self.max_health = 250
        self.attack = 2
        self.set_speed(1)
        self.set_score_amount(50)