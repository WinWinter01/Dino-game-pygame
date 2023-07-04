import pygame
import random

class obstacle:
    def __init__(self, window, cfg, x, y, width, image):
        self.window = window
        self.cfg = cfg
        self.obstacle_pos_x = x
        self.obstacle_pos_y = y
        self.obstacle_width = width
        self.image = image

    def move_obstacle(self):
        if self.obstacle_pos_x+self.obstacle_width<=0:
            self.gen_new_pos()
        else:
            self.window.blit(self.image, (self.obstacle_pos_x, self.obstacle_pos_y))
            self.obstacle_pos_x -= self.cfg.obstacle_speed

    def Increase_speed(self):
        if self.cfg.obstacle_speed_increase == 10:
            self.cfg.obstacle_speed += 1
            self.cfg.obstacle_speed_increase = 0
  
    def gen_new_pos(self):
        #Знаходимо позицію та довжину крайньої правої перешкоди
        max_pos = max(self.cfg.obstacle_arr[0].obstacle_pos_x, self.cfg.obstacle_arr[1].obstacle_pos_x, self.cfg.obstacle_arr[2].obstacle_pos_x)
        max_width = 0
        for i in range(0,3):
            if max_pos == self.cfg.obstacle_arr[i].obstacle_pos_x:
                max_width = self.cfg.obstacle_arr[i].obstacle_width
                break
        #Якщо перешкода видима на екрані   
        if max_pos < self.cfg.window_width:
            self.obstacle_pos_x = self.cfg.window_width
            if self.obstacle_pos_x - max_pos < self.cfg.hero_width+25:
                self.obstacle_pos_x += 150
        else:
            self.obstacle_pos_x = max_pos
            
        #Генерація позиції
        random_choice = random.randrange(0,5)
        if random_choice == 0:
            self.obstacle_pos_x+=max_width
            self.obstacle_pos_x += random.randrange(0,10)
        else:
            self.obstacle_pos_x += random.randrange(self.cfg.hero_width+100,400)
        
        #Генерація зображення
        choice = random.randrange(0, 3)    
        self.image = self.cfg.obstacle_images[choice]
        self.width = self.cfg.obstacle_options[choice*2]
        self.obstacle_pos_y = self.cfg.obstacle_options[choice*2+1]
        
