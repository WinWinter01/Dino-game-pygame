import pygame
import sys

class menusANDtext:
    def __init__(self, window, cfg, main_loop):
        self.window = window
        self.cfg = cfg        
        self.main_loop = main_loop
        
    def print_text(self, message, x, y, font_color=(0,0,0), font_size = 15):
        font_type = pygame.font.Font(self.cfg.font_type, font_size)
        text = font_type.render(message, True, font_color)
        self.window.blit(text, (x, y))
    
    def stopGame(self):
        pygame.mixer.music.pause()
        self.print_text("Game over. Press Enter to play again, Esc to exit", 30,100, self.cfg.RED)
        pygame.display.update()
        
        while self.cfg.STOPPED:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.cfg.game = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.cfg.game = True
                        self.cfg.STOPPED = False
                        if self.cfg.devMenu:
                            pygame.mixer.music.play(-1)
                        self.main_loop.run()
                    elif event.key == pygame.K_ESCAPE:
                        self.cfg.STOPPED = False
                        self.cfg.game = False
                        sys.exit()
            
    def count_scores(self):
        self.scores_max()
        self.print_text(str("HI {}".format(self.cfg.max_points)), self.cfg.window_width - 250, 20)
        self.print_text(str(self.cfg.number_points), self.cfg.window_width - 100, 20)
        if self.cfg.devMenu:
            self.print_text(str("Speed {}".format(self.cfg.obstacle_speed)), self.cfg.window_width - 250, 40)
        
        for obstacle in self.cfg.obstacle_arr:
            if obstacle.obstacle_pos_x <= self.cfg.hero_pos_x + self.cfg.hero_width <= obstacle.obstacle_pos_x + obstacle.obstacle_width and obstacle!=self.cfg.jump2obstacles:
                self.cfg.number_points += 1
                self.cfg.addScores = False
                self.cfg.jump2obstacles = obstacle
                self.cfg.obstacle_speed_increase += 1
            
    def scores_max(self):
        if self.cfg.number_points > self.cfg.max_points:
            data_file = open(self.cfg.path_file_data, 'w')
            data_file.write(str(self.cfg.number_points))
            data_file.close()
    
        data_file = open(self.cfg.path_file_data, 'r')
        data = data_file.read()
        data_file.close()      
        self.cfg.max_points = int(data)
        
    def blit_bg(self):
        self.window.blit(self.cfg.bg1, (self.cfg.bg1_x, self.cfg.ground-80))
        self.window.blit(self.cfg.bg2, (self.cfg.bg2_x, self.cfg.ground-80))
        
        if self.cfg.bg1_x + self.cfg.bg_width <= 0:
            self.cfg.bg1_x = self.cfg.bg2_x + self.cfg.bg_width #self.cfg.window_width
        else:
            self.cfg.bg1_x -= self.cfg.obstacle_speed
            
        if self.cfg.bg2_x + self.cfg.bg_width <= 0:
            self.cfg.bg2_x = self.cfg.bg1_x + self.cfg.bg_width #self.cfg.window_width
        else:
            self.cfg.bg2_x -= self.cfg.obstacle_speed
            
    def menu(self):
        
        while True:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            
            self.window.blit(self.cfg.img_menu, self.cfg.img_menu_rect)
            if self.cfg.needMen:
                self.cfg.FLAG_MENU = True
                self.cfg.needMen = False
            
            if self.cfg.FLAG_MENU == False:
                pygame.draw.rect(self.window, self.cfg.BLACK, (self.cfg.settings_x,self.cfg.settings_y,self.cfg.settings_width,self.cfg.settings_height), 2)
                pygame.draw.rect(self.window, self.cfg.BLACK, (self.cfg.play_x,self.cfg.play_y,self.cfg.play_width,self.cfg.play_height), 2)
                pygame.draw.rect(self.window, self.cfg.BLACK, (self.cfg.exit_x,self.cfg.exit_y,self.cfg.exit_width,self.cfg.exit_height), 2)

                if self.cfg.play_x < mouse[0] < self.cfg.play_x + self.cfg.play_width:
                    if self.cfg.play_y < mouse[1] < self.cfg.play_y + self.cfg.play_height:
                        pygame.draw.rect(self.window, self.cfg.WHITE, (self.cfg.play_x,self.cfg.play_y,self.cfg.play_width,self.cfg.play_height))

                        if click[0] == 1:
                            pygame.mixer.Sound.play(self.cfg.button_sound)
                            if self.cfg.devMenu:
                                pygame.mixer.music.play(-1)
                            return False
                    
                if self.cfg.settings_x < mouse[0] < self.cfg.settings_x + self.cfg.settings_width:
                    if self.cfg.settings_y < mouse[1] < self.cfg.settings_y + self.cfg.settings_height:
                        pygame.draw.rect(self.window, self.cfg.WHITE, (self.cfg.settings_x,self.cfg.settings_y,self.cfg.settings_width,self.cfg.settings_height))

                        if click[0] == 1:
                            pygame.mixer.Sound.play(self.cfg.button_sound)
                            self.cfg.needMen = True
                            pygame.time.delay(300)
                            
                if self.cfg.exit_x < mouse[0] < self.cfg.exit_x + self.cfg.exit_width:
                    if self.cfg.exit_y < mouse[1] < self.cfg.exit_y + self.cfg.exit_height:
                        pygame.draw.rect(self.window, self.cfg.WHITE, (self.cfg.exit_x,self.cfg.exit_y,self.cfg.exit_width,self.cfg.exit_height))

                        if click[0] == 1:
                            pygame.mixer.Sound.play(self.cfg.button_sound)
                            pygame.time.delay(300)
                            sys.exit()
                
                data_file = open(self.cfg.path_file_data, 'r')
                data = data_file.read()
                data_file.close()      
                self.print_text(str("Your record: {}".format(int(data))), self.cfg.window_width - 600, 50, (52,142,20), 20)
                self.print_text(str("PLAY"), self.cfg.play_x+5,self.cfg.play_y+5, self.cfg.BLACK)
                self.print_text(str("SETTINGS"), self.cfg.settings_x+5,self.cfg.settings_y+5, self.cfg.BLACK)
                self.print_text(str("EXIT"), self.cfg.exit_x+5,self.cfg.exit_y+5, self.cfg.BLACK)
            
                
            if self.cfg.FLAG_MENU == True:
                pygame.draw.rect(self.window, self.cfg.BLACK, (self.cfg.play_x,self.cfg.play_y,self.cfg.play_width+60,self.cfg.play_height), 2)
                pygame.draw.rect(self.window, self.cfg.BLACK, (self.cfg.settings_x,self.cfg.settings_y,self.cfg.settings_width+90,self.cfg.settings_height), 2) 
                pygame.draw.rect(self.window, self.cfg.BLACK, (self.cfg.exit_x,self.cfg.exit_y,self.cfg.exit_width,self.cfg.exit_height), 2)

                    
                if self.cfg.play_x < mouse[0] < self.cfg.play_x + self.cfg.play_width+60:
                    if self.cfg.play_y < mouse[1] < self.cfg.play_y + self.cfg.play_height:
                        pygame.draw.rect(self.window, self.cfg.WHITE, (self.cfg.play_x,self.cfg.play_y,self.cfg.play_width+60,self.cfg.play_height))
                        if click[0] == 1:
                            pygame.mixer.Sound.play(self.cfg.button_sound)
                            data_file = open('DATA_DEV.txt', 'w')
                            
                            if self.cfg.window_width == 900 and self.cfg.window_height == 500:
                                data_file.write("1\n")
                            
                            elif self.cfg.window_width == 1200 and self.cfg.window_height == 700:
                                data_file.write("0\n")
                            
                            if self.cfg.devMenu:
                                
                                data_file.write("1")
                            else:
                                data_file.write("0")
                                
                            data_file.close()
                            sys.exit()
                            
                if self.cfg.settings_x < mouse[0] < self.cfg.settings_x + self.cfg.settings_width+90:
                    if self.cfg.settings_y < mouse[1] < self.cfg.settings_y + self.cfg.settings_height:
                        pygame.draw.rect(self.window, self.cfg.WHITE, (self.cfg.settings_x,self.cfg.settings_y,self.cfg.settings_width+90,self.cfg.settings_height))
                        
                        if click[0] == 1:
                            pygame.mixer.Sound.play(self.cfg.button_sound)
                            data_file = open('DATA_DEV.txt', 'w')
                            data_file.write(str("{}\n".format(self.cfg.size_window)))
                            if self.cfg.devMenu:
                                data_file.write("0")
                                self.cfg.devMenu = False
                            else:
                                data_file.write("1")
                                self.cfg.devMenu = True
                            data_file.close()
                            pygame.time.delay(300)

                if self.cfg.exit_x < mouse[0] < self.cfg.exit_x + self.cfg.exit_width:
                    if self.cfg.exit_y < mouse[1] < self.cfg.exit_y + self.cfg.exit_height:
                        pygame.draw.rect(self.window, self.cfg.WHITE, (self.cfg.exit_x,self.cfg.exit_y,self.cfg.exit_width,self.cfg.exit_height))

                        if click[0] == 1:
                            pygame.mixer.Sound.play(self.cfg.button_sound)
                            self.cfg.FLAG_MENU = False
                            pygame.time.delay(300)
                
                self.print_text("Launch the game again to apply the changes", self.cfg.play_x+5,self.cfg.play_y+5-30, self.cfg.RED)
                
                if self.cfg.window_width == 900 and self.cfg.window_height == 500:
                    self.print_text(str("1200x700"), self.cfg.play_x+5,self.cfg.play_y+5, self.cfg.BLACK)
                    
                elif self.cfg.window_width == 1200 and self.cfg.window_height == 700:
                    self.print_text(str("900x500"), self.cfg.play_x+5,self.cfg.play_y+5, self.cfg.BLACK)
                    
                self.print_text("left arrow - STOP, right arrow - immortality", self.cfg.settings_x+5,self.cfg.settings_y+5-30, self.cfg.RED)

                if self.cfg.devMenu:
                    self.print_text(str("developer menu"), self.cfg.settings_x+5,self.cfg.settings_y+5, self.cfg.RED)
                else:
                    self.print_text(str("developer menu"), self.cfg.settings_x+5,self.cfg.settings_y+5, self.cfg.BLACK)

                self.print_text(str("BACK"), self.cfg.exit_x+5,self.cfg.exit_y+5, self.cfg.BLACK)
                
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.cfg.game = False
                    sys.exit()