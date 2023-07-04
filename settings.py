import pygame

class Settings:
    def __init__(self):
        pygame.init() #підключення модулів
        self.game = True #основний цикл
        self.PAUSE = False #пауза
        self.STOPPED = False #стоп
        self.devMenu = None
        self.immortality = False
        #Параметри вікна
        self.window_width = None #900 1200
        self.window_height = None #500 700
        
      

        data_file = open('DATA_DEV.txt', 'r')
        data = data_file.readline()
        data2 = data_file.readline()
        data_file.close()      
        self.size_window = int(data)
        self.devMenu = int(data2)
  
        
        if self.size_window == 0:
            self.window_width = 900 
            self.window_height = 500 
        elif self.size_window == 1:
            self.window_width = 1200 
            self.window_height = 700
            
        #
        #Меню
        #self.img_menu = pygame.image.load("Sprites/bg_menu.jpg").convert_alpha()
        #self.img_menu_pos = [1800, 800]
        #self.img_menu = pygame.transform.scale(self.img_menu, (1800, 800))
        #self.img_menu_rect = self.img_menu.get_rect(topleft=(0,0))
        
        self.play_x = 10
        self.play_y = 200
        self.play_width = 70
        self.play_height = 30
        self.settings_x = 10
        self.settings_y = 280
        self.settings_width = 130
        self.settings_height = 30
        self.needMen = False
        self.exit_x = 10
        self.exit_y = 360
        self.exit_width = 70
        self.exit_height = 30        
        self.FLAG_MENU = False
        
        
        
        #Частота кадрів
        self.clock = pygame.time.Clock()
        self.FPS = 80
        
        #Кольори
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,255,0)
        self.BLUE = (0,0,255)
        self.YELLOW = (255,255,0)
        self.ORANGE = (255,215,0)
        self.DARKORANGE = (252, 192, 63)
        self.SILVER = (192, 192, 192)
        
        #Земля
        self.ground = self.window_height - 100 
        #self.bg = pygame.image.load(r'Sprites/Ground.png').convert_alpha()
        #self.bg1 = pygame.image.load(r'Sprites/Ground_1.png').convert_alpha()
        #self.bg2 = pygame.image.load(r'Sprites/Ground_2.png').convert_alpha()
        self.bg1_x = 0
        self.bg2_x = 1200
        self.bg_width = 1200
        self.bg_pos_x = 0
        
        
        #Параметри головного героя
        self.hero_width = 80
        self.hero_height = 100
        self.hero_pos_x = self.window_width // 10
        self.hero_pos_y = self.ground - self.hero_height
        #self.hero_images = [pygame.image.load("Sprites/run1.png").convert_alpha(), pygame.image.load("Sprites/run2.png").convert_alpha(), pygame.image.load("Sprites/Idle.png").convert_alpha()] 
        self.img_counter = 6
        
        #Перешкоди
        self.obstacle_arr = []
        #self.obstacle_images = [pygame.image.load("Sprites/cactus1.png").convert_alpha(), pygame.image.load("Sprites/cactus2.png").convert_alpha(), pygame.image.load("Sprites/cactus3.png").convert_alpha()] 
        self.obstacle_options = [20,self.ground - 60, 25,self.ground - 50, 40,self.ground - 40]
        self.obstacle_speed = 4
        self.obstacle_speed_increase = 0
        
        #Стрибок
        self.jump_id = False
        self.jump_power = 20
        self.jump_speed = -self.jump_power
        
        #Шрифт
        self.font_type = 'PublicPixel.ttf'
        
        #Лічильник очок
        self.number_points = 0
        self.addScores = False
        self.jump2obstacles = None
        self.path_file_data = 'DATA.txt'
        self.max_points = 0

        #Візуальні еффекти
        self.cords_visual_obj_x = [self.window_width]
        self.cords_visual_obj_y = [0]
        #self.visual_obj_img = pygame.image.load(r'Sprites/cloud.png').convert_alpha()
        self.vis_obj_width = 100
        self.vis_obj_height = 30
        self.count_vis_obj = 1
        #Звуки
        pygame.mixer.music.load('Sounds/game_m.mp3')
        self.button_sound = pygame.mixer.Sound('Sounds/button.wav')
        self.jump_sound = pygame.mixer.Sound('Sounds/jump.mp3')
        self.death_sound = pygame.mixer.Sound('Sounds/death.mp3')


        
        
    def img_load(self):
        self.img_menu = pygame.image.load("Sprites/bg_menu.jpg").convert_alpha()
        self.bg = pygame.image.load(r'Sprites/Ground.png').convert_alpha()
        self.bg1 = pygame.image.load(r'Sprites/Ground_1.png').convert_alpha()
        self.bg2 = pygame.image.load(r'Sprites/Ground_2.png').convert_alpha()
        self.hero_images = [pygame.image.load("Sprites/run1.png").convert_alpha(), pygame.image.load("Sprites/run2.png").convert_alpha(), pygame.image.load("Sprites/Idle.png").convert_alpha()] 
        self.obstacle_images = [pygame.image.load("Sprites\cactus1.png").convert_alpha(), pygame.image.load("Sprites/cactus2.png").convert_alpha(), pygame.image.load("Sprites/cactus3.png").convert_alpha()] 
        self.visual_obj_img = pygame.image.load(r'Sprites\cloud.png').convert_alpha()
        if self.window_width == 1200 and self.window_height == 700:
            self.img_menu = pygame.transform.scale(self.img_menu, (1800, 800))
        elif self.window_width == 900 and self.window_height == 500:
            self.img_menu = pygame.transform.scale(self.img_menu, (1500, 700))
        self.img_menu_rect = self.img_menu.get_rect(topleft=(0,0))
