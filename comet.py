
import pygame
import random
from monster import Mummy, Alien

class Comet(pygame.sprite.Sprite):
    
    def __init__(self, comet_event):
        super().__init__()
        self.velocity = random.randint(2,4)
        self.comet_event = comet_event
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20,1000)
        self.rect.y = -random.randint(0,300)
        
        
    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')
        
        if len(self.comet_event.all_comets) == 0 :
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster((Alien))
        
        
    def fall(self):
        self.rect.y += self.velocity
        
        if self.rect.y >= 500:
            self.remove()
            
            if len(self.comet_event.all_comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False
                
                
        if self.comet_event.game.check_collision(
            self,
            self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)
            