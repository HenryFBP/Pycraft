if not __name__ == "__main__":
    print("Started <Pycraft_HomeScreen>")
    class GenerateHomeScreen:
        def __init__(self):
            try:
                import pygame # self mod (module) (module name) (subsection of module) (name references)
                self.mod_Pygame__ = pygame
                import os
                self.mod_OS__ = os
                import sys
                self.mod_Sys__ = sys
                import random
                self.mod_Random__ = random
                import time
                self.mod_Time__ = time
                import pygame.locals
                self.mod_Pygame_locals_ = pygame.locals
                import psutil
                self.mod_Psutil__ = psutil
                from tkinter import messagebox
                self.mod_Tkinter_messagebox_ = messagebox
                
                self.mod_Pygame__.init()
                
                base_folder = os.path.dirname(__file__)
            except Exception as error:
                print(error)
                try:
                    import tkinter as tk
                    root = tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showerror("Startup Fail", "Missing required modules")
                    quit()
                except:
                    try:
                        self.mod_Pygame__.quit()
                        sys.exit("Thank you for playing")
                    except:
                        quit()

        def Home_Screen(self):
            try:
                self.Display.fill(self.BackgroundCol)
                self.mod_Pygame__.display.flip()
                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")
                Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()
                SelectorWidth = Selector.get_width()
                hover1 = False 
                hover2 = False 
                hover3 = False 
                hover4 = False 
                hover5 = False
                hover6 = False
                mousebuttondown = False 
                
                MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60) 
                PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)
                TitleWidth = PycraftTitle.get_width()
                realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                self.Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))
                self.mod_Pygame__.display.flip()

                SideFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 24) 
                VersionFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
                ButtonFont1 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                ButtonFont2 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                ButtonFont3 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                ButtonFont4 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30) 
                ButtonFont5 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)
                ButtonFont6 = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 30)
                DataFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15) 
                data1 = [] 
                data2 = [] 
                data3 = [] 
                data4 = [] 
                run = 0
                rerun = 0 
                self.aFPS = self.FPS
                counter = 0
                oldTHEME = self.theme
                tempFPS = self.FPS
                coloursARRAY = []

                anim = True

                special = [30, 30, 30]
                TargetARRAY = []

                ColourDisplacement = 80

                increment = False

                while True:
                    coloursARRAY = []
                    if anim == True:
                        anim = False
                        TargetARRAY = []
                        for a in range(self.mod_Random__.randint(0, 32)):
                            TargetARRAY.append(a)
                                    
                    if len(TargetARRAY) == 0:
                        TargetARRAY = [33]
                    for i in range(32):
                        for j in range(len(TargetARRAY)):
                            if i == TargetARRAY[j]:
                                coloursARRAY.append(special)
                            else:
                                coloursARRAY.append(self.ShapeCol)

                    if increment == False:
                        if self.aFPS == 0 or counter == 0:
                            ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.FPS)/4))
                        else:
                            ColourDisplacement -= (self.mod_Random__.randint(0,10)/((self.aFPS/counter)/4))
                        special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement
                    if increment == True:
                        if self.aFPS == 0 or counter == 0:
                            ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.FPS)/4))
                        else:
                            ColourDisplacement += (self.mod_Random__.randint(0,10)/((self.aFPS/counter)/4))
                        special[0], special[1], special[2] = ColourDisplacement, ColourDisplacement, ColourDisplacement
                    if special[0] <= 30:
                        increment = True
                        special[0], special[1], special[2] = 30, 30, 30
                    if special[0] >= 80:
                        increment = False
                        anim = True
                        special[0], special[1], special[2] = 80, 80, 80

                    if self.mod_Pygame__.mixer.Channel(3).get_busy() == 1:
                        self.mod_Pygame__.mixer.Channel(3).stop()

                    if str(self.Display) == "<Surface(Dead Display)>":
                        if self.Fullscreen == False:
                            self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)
                        elif self.Fullscreen == True:
                            self.mod_DisplayUtils__.DisplayUtils.SetDisplay(self)

                    realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                    if not (realWidth == self.FullscreenX and realHeight == self.FullscreenY):
                        self.SavedWidth, self.SavedHeight = self.mod_Pygame__.display.get_window_size()

                    if self.SavedWidth == self.FullscreenX:
                        self.SavedWidth = 1280
                    if self.SavedHeight == self.FullscreenY:
                        self.SavedHeight = 720

                    if realWidth < 1280:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, 1280, self.SavedHeight)
                    if realHeight < 720:
                        self.mod_DisplayUtils__.DisplayUtils.GenerateMinDisplay(self, self.SavedWidth, 720)

                    yScaleFact = realHeight/720
                    xScaleFact = realWidth/1280
                    
                    if not oldTHEME == self.theme:
                        Selector = self.mod_Pygame__.image.load(self.mod_OS__.path.join(self.base_folder, (f"Resources\\General_Resources\\selectorICON{self.theme}.jpg"))).convert()
                        SelectorWidth = Selector.get_width()
                        oldTHEME = self.theme

                    tempFPS = self.mod_DisplayUtils__.DisplayUtils.GetPlayStatus(self)
                        
                    counter += 1
                    self.Display.fill(self.BackgroundCol)
                    self.eFPS = self.clock.get_fps()
                    self.aFPS += self.eFPS
                    self.Iteration += 1
                    Mx, My = self.mod_Pygame__.mouse.get_pos() 
                    run += 1 
                    PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)
                    TitleWidth = PycraftTitle.get_width()

                    Name = SideFont.render("By Tom Jebbo", self.aa, self.FontCol)
                    NameHeight = Name.get_height()

                    Version = VersionFont.render(f"Version: {self.version}", self.aa, self.FontCol) 
                    VersionWidth = Version.get_width()
                    VersionHeight = Version.get_height()

                    Play = ButtonFont1.render("Play", self.aa, self.FontCol)
                    PlayWidth = Play.get_width()

                    SettingsText = ButtonFont2.render("Settings", self.aa, self.FontCol)
                    SettingsWidth = SettingsText.get_width()

                    Character_DesignerText = ButtonFont3.render("Character Designer", self.aa, self.FontCol)
                    CharDesignerWidth = Character_DesignerText.get_width()

                    AchievementsText = ButtonFont4.render("Achievements", self.aa, self.FontCol)
                    AchievementsWidth = AchievementsText.get_width()

                    Credits_and_Change_Log_Text = ButtonFont5.render("Credits", self.aa, self.FontCol)
                    CreditsWidth = Credits_and_Change_Log_Text.get_width()

                    BenchmarkText = ButtonFont6.render("Benchmark", self.aa, self.FontCol)
                    BenchmarkWidth = BenchmarkText.get_width()

                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None, "saveANDexit"
                        if event.type == self.mod_Pygame__.KEYDOWN: 
                            if event.key == self.mod_Pygame__.K_SPACE and self.Devmode < 10: 
                                self.Devmode += 1
                            if event.key == self.mod_Pygame__.K_q:
                                self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)
                            if event.key == self.mod_Pygame__.K_F11:
                                self.mod_DisplayUtils__.DisplayUtils.UpdateDisplay(self)
                            if event.key == self.mod_Pygame__.K_x:
                                self.Devmode = 1 
                        if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN: 
                            mousebuttondown = True 
                        if event.type == self.mod_Pygame__.MOUSEBUTTONUP: 
                            mousebuttondown = False

                    self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Home screen")
                    
                    ButtonFont1.set_underline(hover1) 
                    ButtonFont2.set_underline(hover2) 
                    ButtonFont3.set_underline(hover3)
                    ButtonFont4.set_underline(hover4)
                    ButtonFont5.set_underline(hover5)
                    ButtonFont6.set_underline(hover6)
                    
                    if My >= 202*yScaleFact and My <= 247*yScaleFact and Mx >= (realWidth-(PlayWidth+SelectorWidth))-2:
                        hover1 = True
                        if mousebuttondown == True:
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None, "Play"
                    else:
                        hover1 = False
                    
                    if My >= 252*yScaleFact and My <= 297*yScaleFact and Mx >= (realWidth-(SettingsWidth+SelectorWidth))-2: 
                        hover2 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None, "Settings"
                    else:
                        hover2 = False

                    if My >= 302*yScaleFact and My <= 347*yScaleFact and Mx >= (realWidth-(CharDesignerWidth+SelectorWidth)-2):
                        hover3 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None, "CharacterDesigner"
                    else:
                        hover3 = False

                    if My >= 402*yScaleFact and My <= 447*yScaleFact and Mx >= (realWidth-(AchievementsWidth+SelectorWidth)-2):
                        hover4 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None, "Achievements"
                    else:
                        hover4 = False

                    if My >= 352*yScaleFact and My <= 397*yScaleFact and Mx >= (realWidth-(CreditsWidth+SelectorWidth)-2):
                        hover5 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None, "Credits"
                    else:
                        hover5 = False

                    if My >= 452*yScaleFact and My <= 497*yScaleFact and Mx >= (realWidth-(BenchmarkWidth+SelectorWidth)-2):
                        hover6 = True
                        if mousebuttondown == True:
                            self.Display.fill(self.BackgroundCol)
                            self.mod_Pygame__.display.flip()
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayClickSound(self)
                            return None, "Benchmark"
                    else:
                        hover6 = False

                    self.Display.fill(self.BackgroundCol)

                    self.Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))
                    self.Display.blit(Name, (0, (realHeight-NameHeight)))

                    self.Display.blit(Version, ((realWidth-VersionWidth)-2, (realHeight-VersionHeight)))

                    self.Display.blit(Play, ((realWidth-PlayWidth)-2, 200*yScaleFact))

                    self.Display.blit(SettingsText, ((realWidth-SettingsWidth)-2, 250*yScaleFact))

                    self.Display.blit(Character_DesignerText, ((realWidth-CharDesignerWidth)-2, 300*yScaleFact))

                    self.Display.blit(Credits_and_Change_Log_Text, ((realWidth-CreditsWidth)-2, 350*yScaleFact))

                    self.Display.blit(AchievementsText, ((realWidth-AchievementsWidth)-2, 400*yScaleFact))

                    self.Display.blit(BenchmarkText, ((realWidth-BenchmarkWidth)-2, 450*yScaleFact))

                    if hover1 == True:
                        self.Display.blit(Selector, (realWidth-(PlayWidth+SelectorWidth)-2, 200*yScaleFact))
                        self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)
                    elif hover2 == True:
                        self.Display.blit(Selector, (realWidth-(SettingsWidth+SelectorWidth)-2, 250*yScaleFact))
                        self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)
                    elif hover3 == True:
                        self.Display.blit(Selector, (realWidth-(CharDesignerWidth+SelectorWidth)-2, 300*yScaleFact))
                        self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)
                    elif hover5 == True:
                        self.Display.blit(Selector, (realWidth-(CreditsWidth+SelectorWidth)-2, 350*yScaleFact))
                        self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)
                    elif hover4 == True:
                        self.Display.blit(Selector, (realWidth-(AchievementsWidth+SelectorWidth)-2, 400*yScaleFact))
                        self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)
                    elif hover6 == True:
                        self.Display.blit(Selector, (realWidth-(BenchmarkWidth+SelectorWidth)-2, 450*yScaleFact))
                        self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_HAND)
                    else:
                        self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_ARROW)
                        
                    if run >= 1000:
                        run = 0
                        rerun += 1
                    Message = self.mod_DrawingUtils__.GenerateGraph.CreateDevmodeGraph(self, run, rerun, data1, data2, data3, data4, DataFont)
                    if not Message == None:
                        return Message, None

                    self.mod_DrawingUtils__.DrawRose.CreateRose(self, xScaleFact, yScaleFact, coloursARRAY)

                    self.mod_Pygame__.display.flip()
                    self.clock.tick(tempFPS)
            except Exception as Message:
                print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))
                return Message, None
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()