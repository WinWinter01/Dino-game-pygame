import pygame
import sys
import random
from settings import Settings
from Hero import hero
from Obstacle import obstacle
from MenuText import menusANDtext

class Main_Loop():
    def __init__(self):
        pygame.init()
        
        self.cfg = Settings()
    
        self.showMenu = True
        
        self.window = pygame.display.set_mode((self.cfg.window_width,  self.cfg.window_height), pygame.DOUBLEBUF)
        pygame.display.set_caption('"Dino run" created by Vadym Bazalei')
        
        self.run()
        
    def run(self):
        
        self.cfg = Settings() #Ініціалізація налаштувань
        
        self.cfg.img_load()
        self.textinfo = menusANDtext(self.window, self.cfg, self) #Ініціалізація меню
        if self.showMenu:
            self.textinfo.menu()
            self.showMenu = False
            
        elif self.cfg.devMenu:
            pygame.mixer.music.play(-1)
            
        self.create_obstacle_arr() #створювання перешкод
        self.fps_font = pygame.font.SysFont((self.cfg.font_type), 64)
        
        
        while self.cfg.game:
            
            #Системне
            self.cfg.clock.tick(self.cfg.FPS)
            self.cfg.keys = pygame.key.get_pressed()
            
            #Відображення об'єктів
            self.window.fill(self.cfg.WHITE) #фон
            self.textinfo.blit_bg()#фон з картинкою
            self.Create_Visual_Obj()#хмари
            #FPS
            if self.cfg.devMenu:
                fps_surface = self.fps_font.render(self.cfg.clock.get_fps().__int__().__str__(), False, self.cfg.BLACK)
                fps_rect = fps_surface.get_rect(topleft=(0, 0))
                self.window.blit(fps_surface, (0,0))
            #
            self.textinfo.count_scores() #Підрахунок та відображення очок
            self.Hero = hero(self.window, self.cfg) #головний герой, малювання та стрибок
            self.call_drawFunk() #переміщення та малювання перешкод

            pygame.display.update()

            #Перевірка на зіткнення
            if self.Hero.collision() and self.cfg.immortality == False:
                pygame.mixer.Sound.play(self.cfg.death_sound)
                self.cfg.game = False
                self.cfg.STOPPED = True
                self.textinfo.stopGame()

            #Натискання клавіш та пауза    
            self.EventsKeys()
            if self.cfg.PAUSE:
                while self.cfg.PAUSE:
                    self.EventsKeys()
                    
    def create_obstacle_arr(self):
        #Функція яка створює перешкоди
        choice = random.randrange(0, 3)
        img = self.cfg.obstacle_images[choice]
        width = self.cfg.obstacle_options[choice*2]
        y = self.cfg.obstacle_options[choice*2+1]
        
        self.cfg.obstacle_arr.append(obstacle(self.window, self.cfg, self.cfg.window_width + 100, y, width, img))
        
        choice = random.randrange(0, 3)
        img = self.cfg.obstacle_images[choice]
        width = self.cfg.obstacle_options[choice*2]
        y = self.cfg.obstacle_options[choice*2+1]
        
        self.cfg.obstacle_arr.append(obstacle(self.window, self.cfg, self.cfg.window_width + 300, y, width, img))
        
        choice = random.randrange(0, 3)
        img = self.cfg.obstacle_images[choice]
        width = self.cfg.obstacle_options[choice*2]
        y = self.cfg.obstacle_options[choice*2+1]
        
        self.cfg.obstacle_arr.append(obstacle(self.window, self.cfg, self.cfg.window_width + 500, y, width, img))
    
    def call_drawFunk(self):
        #Функція яка запускає переміщення перешкод та збільшення швидкості
        for obs in self.cfg.obstacle_arr:
            obs.move_obstacle()
            obs.Increase_speed()
           
    def EventsKeys(self):
        #Функція подій клавіш
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.cfg.game = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.cfg.devMenu:
                    if self.cfg.PAUSE == False:
                        self.cfg.PAUSE = True
                    else:
                        self.cfg.PAUSE = False
                if event.key == pygame.K_RIGHT and self.cfg.devMenu:
                    if self.cfg.immortality == False:
                        self.cfg.immortality = True
                    else:
                        self.cfg.immortality = False
                        
            if self.cfg.keys[pygame.K_SPACE]:
                self.cfg.jump_id = True
                self.cfg.addScores = True
                
    def Create_Visual_Obj(self):
        #Функція для відображення візуальних ефектів(хмар)
        for i in range(len(self.cfg.cords_visual_obj_x)):
            self.window.blit(self.cfg.visual_obj_img, (self.cfg.cords_visual_obj_x[i], self.cfg.cords_visual_obj_y[i]))
            
        if(self.cfg.count_vis_obj < 3):
            max_pos_x = max(self.cfg.cords_visual_obj_x)
            max_pos_y = max(self.cfg.cords_visual_obj_y)
            
            self.cfg.count_vis_obj+=1
            
            if max_pos_x > self.cfg.window_width:
                pos_x = max_pos_x + self.cfg.vis_obj_width + random.randint(50, 500)
                pos_y = random.randint(0, self.cfg.hero_pos_y - self.cfg.vis_obj_height)
            else:
                pos_x = self.cfg.window_width + random.randint(50, 500)
                pos_y = random.randint(0, self.cfg.hero_pos_y - self.cfg.vis_obj_height)
                
            self.cfg.cords_visual_obj_x.append(pos_x)
            self.cfg.cords_visual_obj_y.append(pos_y)
        
        elif(self.cfg.count_vis_obj > 0):
            for i in range(len(self.cfg.cords_visual_obj_x)):
                self.cfg.cords_visual_obj_x[i] -= self.cfg.obstacle_speed-2
                if(self.cfg.cords_visual_obj_x[i] + self.cfg.vis_obj_width <= 0):
                    self.cfg.count_vis_obj-=1
                    self.cfg.cords_visual_obj_x.pop(i)
                    self.cfg.cords_visual_obj_y.pop(i)
                    break
        
a = Main_Loop()