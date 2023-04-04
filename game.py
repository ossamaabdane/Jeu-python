import pygame

from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager

class Game:
    
    def __init__(self):
        self.is_playing = False 
        self.player = Player(self)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}
        self.all_monsters = pygame.sprite.Group()
        self.comet_event = CometFallEvent(self)
        self.font = pygame.font.Font("assets/PottaOne-Regular.ttf",24)
        self.score = 0
        self.sound_manager = SoundManager()

    def add_score(self, points=10):
        self.score += points

        
    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
    
    def spawn_monster(self, monster_class_name):
        monster = monster_class_name.__call__(self)
        self.all_monsters.add(monster)

        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.rect.x = 400
        self.player.rect.y = 500
        self.is_playing = False
        self.comet_event.reset_percent()
        self.score = 0
        self.sound_manager.play('game_over')
        
    
    def update(self, screen):
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)
        self.player.update_animation()
        
        self.comet_event.update_bar(screen)
    
        for projectile in self.player.all_projectiles:
            projectile.move()
            
        self.player.all_projectiles.draw(screen)
            
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()
                
        self.all_monsters.draw(screen)
        
        for comet in self.comet_event.all_comets:
            comet.fall()
        
        self.comet_event.all_comets.draw(screen)
        
        if self.pressed.get(pygame.K_RIGHT) and (self.player.rect.x + self.player.rect.width) < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        