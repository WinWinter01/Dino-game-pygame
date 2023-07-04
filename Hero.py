import pygame
from settings import Settings

class hero():
    def __init__(self, window, cfg):
        self.window = window
        self.cfg = cfg
        
        self.draw()
        
        if self.cfg.jump_id == True:
            self.jump()
    
    def draw(self):
        if self.cfg.jump_id == False:
            if self.cfg.img_counter == 20:
                self.cfg.img_counter = 0
                
            self.window.blit(self.cfg.hero_images[self.cfg.img_counter//10], (self.cfg.hero_pos_x, self.cfg.hero_pos_y))
            
            self.cfg.img_counter += 1
        else:
            self.window.blit(self.cfg.hero_images[2], (self.cfg.hero_pos_x, self.cfg.hero_pos_y))
            
    def jump(self):
        if self.cfg.jump_speed <= self.cfg.jump_power:
            self.cfg.hero_pos_y += self.cfg.jump_speed
            if self.cfg.jump_speed == -20:
                pygame.mixer.Sound.play(self.cfg.jump_sound)
            self.cfg.jump_speed+=1
        else:
            self.cfg.jump_speed = -self.cfg.jump_power
            self.cfg.hero_pos_y = self.cfg.ground-self.cfg.hero_height
            self.cfg.jump_id = False
    
    def collision(self):
        for obstacle in self.cfg.obstacle_arr:
            if not self.cfg.jump_id:
                #Звіряємо якщо він не пригає
                if obstacle.obstacle_pos_x <= self.cfg.hero_pos_x + self.cfg.hero_width - 35 <= obstacle.obstacle_pos_x + obstacle.obstacle_width:
                    return True
            if self.cfg.jump_speed >= -1:
                #Звіряємо якщо пригає ліву та праву ногу
                if self.cfg.hero_pos_y + self.cfg.hero_height - 15 >= obstacle.obstacle_pos_y:
                    if obstacle.obstacle_pos_x <= self.cfg.hero_pos_x + self.cfg.hero_width - 45 <= obstacle.obstacle_pos_x + obstacle.obstacle_width:
                        return True
                    elif obstacle.obstacle_pos_x <= self.cfg.hero_pos_x + 30 <= obstacle.obstacle_pos_x + obstacle.obstacle_width:
                        return True
        return False


            
        