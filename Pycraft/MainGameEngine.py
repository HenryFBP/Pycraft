if not __name__ == "__main__":
    print("Started <Pycraft_MainGameEngine>")
    class CreateEngine:
        def __init__(self):
            pass
        
        def GenerateLoadDisplay(self, LoadingFont, text, MainTitleFont, SecondaryFont, LoadingTextFont):
            try:
                self.Display.fill(self.BackgroundCol)

                self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()

                PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)
                TitleWidth = PycraftTitle.get_width()
                self.Display.blit(PycraftTitle, ((self.realWidth-TitleWidth)/2, 0))

                LoadingTitle = SecondaryFont.render("Loading", self.aa, self.SecondFontCol)
                self.Display.blit(LoadingTitle, (((self.realWidth-TitleWidth)/2)+55, 50))

                self.mod_Pygame__.draw.lines(self.Display, (self.ShapeCol), self.aa, [(100, self.realHeight-100), (self.realWidth-100, self.realHeight-100)], 3)
                self.mod_Pygame__.draw.lines(self.Display, (self.AccentCol), self.aa, self.Progress_Line)

                DisplayMessage = LoadingFont.render(self.ProgressMessageText, self.aa, self.FontCol)
                DisplayMessageWidth = DisplayMessage.get_width()
                self.Display.blit(DisplayMessage, ((self.realWidth-DisplayMessageWidth)/2, self.realHeight-120))

                TextFontRendered = LoadingTextFont.render(f"{text}", self.aa, self.FontCol)
                TextFontRenderedWidth = TextFontRendered.get_width()
                self.Display.blit(TextFontRendered, ((self.realWidth-TextFontRenderedWidth)/2, self.realHeight-100))
            except Exception as error:
                print(error)
    

        def Play(self):
            try:
                self.mod_Pygame__.mixer.Channel(2).fadeout(2000)
                
                self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_WAIT)
                                
                if self.Load3D == True:
                    self.Thread_CalculateObjectData = self.mod_Threading__.Thread(target=self.mod_ThreadingUtil__.GetData.LoadMapData, args=(self,))
                    self.Thread_CalculateObjectData.start()
                    self.Thread_CalculateObjectData.name = "Thread_GetObjectData"
                    
                    self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Loading")

                    MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
                    SecondaryFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                    LoadingFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                    LoadingTextFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                        
                    text = self.mod_TextUtils__.GenerateText.LoadQuickText(self)
                                    
                    self.Progress_Line = [(100, self.realHeight-100), (100, self.realHeight-100)]
                    Percentage_Line_Calculation = (((self.realWidth-200)/100)*((100/self.Total_Vertices)*self.Load_Progress))+100
                            
                    self.Progress_Line.append((Percentage_Line_Calculation, self.realHeight-100))
                
                    while not self.ThreadStatus == "Finished":
                        Percentage_Line_Calculation = (((self.realWidth-200)/100)*((100/self.Total_Vertices)*self.Load_Progress))+100

                        self.Progress_Line.append((Percentage_Line_Calculation, self.realHeight-100))
                        self.CompletePercent = (100/self.Total_Vertices)*self.Load_Progress
                        self.ProgressMessageText = f"Pycraft Loading Map: {round(self.CompletePercent, 1)}% complete"
                        self.mod_MainGameEngine__.CreateEngine.GenerateLoadDisplay(self, LoadingFont, text, MainTitleFont, SecondaryFont, LoadingTextFont)
                    
                        for event in self.mod_Pygame__.event.get():
                            if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):
                                return None, "Undefined"
                        
                        self.clock.tick(self.FPS)
                        self.mod_Pygame__.display.flip()
                    
                    self.Total_Vertices = self.Load_Progress
                                                                          
                Message = self.mod_DisplayUtils__.DisplayUtils.SetOPENGLdisplay(self)
                if not Message == None:
                    return Message, "Undefined"
                
                Message = self.mod_SkyBoxUtil__.SkyBox.LoadSkyBox(self)
                if not Message == None:
                    return Message, "Undefined"
                
                Message = self.mod_MapTextureUtil__.MapTexture.LoadMapTexture(self)
                if not Message == None:
                    return Message, "Undefined"
                
                Jump = False
                JumpID = 0 
                FOV = 70 
                MouseUnlock = False 
                run = 0
                camera_x = 0
                camera_y = 0
                camera_z = 0
                MouseUnlock = True
                counter = 0
                rotationvectX, rotationvectY = 0, 0
                self.Total_move_x, self.Total_move_y, self.Total_move_z = 0, 0, 0
                WKeyPressed, AKeyPressed, SKeyPressed, DKeyPressed = False, False, False, False
                run = 0
                stop = False
                firstRUN = 0                
                prev_camera_x = camera_x
                prev_camera_y = camera_y
                prev_camera_z = camera_z
                self.X = camera_x
                self.Y = camera_y
                self.Z = camera_z
                prev_collisions = 0
                WkeydownTimer = 0
                AkeydownTimer = 0
                SkeydownTimer = 0
                DkeydownTimer = 0
                self.Load3D = False
                self.TotalRotation = 0
                
                self.mod_OpenGL_GLU_.gluPerspective(FOV, (self.realWidth/self.realHeight), 1, 8000000)
                
                self.mod_OpenGL_GL_.glShadeModel(self.mod_OpenGL_GL_.GL_SMOOTH)
                
                self.mod_OpenGL_GL_.glMatrixMode(self.mod_OpenGL_GL_.GL_MODELVIEW)
                
                if self.aa == True:
                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_MULTISAMPLE)
                elif self.aa == False:
                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_MULTISAMPLE)
                    
                self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_FRAMEBUFFER_SRGB)
                
                self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_CROSSHAIR)
                                
                #dima 2021-10-25 BEGIN
                mapVBOVertsId = self.mod_OpenGL_GL_.glGenBuffers(1)
                vertsArr = self.mod_Numpy__.array(self.Map.vertices, 'f')
                
                self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, mapVBOVertsId)
                self.mod_OpenGL_GL_.glBufferData(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, vertsArr.nbytes, vertsArr.data, self.mod_OpenGL_GL_.GL_STATIC_DRAW)
                self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, 0)
                
                mapVBOMeshInds = []
                for mesh in self.Map.mesh_list:
                    mapVBOIndsId = self.mod_OpenGL_GL_.glGenBuffers(1)
                    facesArr = self.mod_Numpy__.array(mesh.faces, 'i')
                    
                    mapVBOMeshInds.append([mapVBOIndsId, facesArr.size])
                    
                    self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, mapVBOIndsId)
                    self.mod_OpenGL_GL_.glBufferData(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, facesArr.nbytes, facesArr.data, self.mod_OpenGL_GL_.GL_STATIC_DRAW)
                    self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, 0)
                #dima 2021-10-25 END

                mouseMovement = (0, 0)
                
                self.mod_Pygame__.mouse.set_visible(False)
                self.mod_Pygame__.mouse.set_pos((self.realWidth/2), (self.realHeight/2))
                
                self.mod_OpenGL_GL_.glTranslatef(0, 0, -2)
                
                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Playing")

                countr = 0
                while True:
                    countr -= 0.5
                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_DEPTH_TEST)
                    #self.mod_GetWorldCollisions__.GetMapCollisions.GetCollisions(self)

                    self.eFPS = self.clock.get_fps()
                    self.aFPS += self.eFPS
                    self.Iteration += 1
                    firstRUN += 1
                    x = self.mod_OpenGL_GL_.glGetDoublev(self.mod_OpenGL_GL_.GL_MODELVIEW_MATRIX)
                    camera_x = x[3][0]
                    camera_y = (x[3][1]-71407.406)
                    camera_z = x[3][2]

                    self.X = camera_x
                    self.Y = camera_y
                    self.Z = camera_z
                    run += 1
                    counter += 1
                    self.realWidth, self.realHeight = self.mod_Pygame__.display.get_window_size()
                    
                    if self.mod_Pygame__.mixer.get_busy() == False:
                        self.mod_SoundUtils__.PlaySound.PlayAmbientSound(self)

                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):
                            self.CurrentlyPlaying = None
                            self.LoadMusic = True
                            return None, "Undefined"
                        if event.type == self.mod_Pygame__.KEYDOWN:
                            if event.key == self.mod_Pygame__.K_a:
                                AKeyPressed = True
                            if event.key == self.mod_Pygame__.K_d:
                                DKeyPressed = True
                            if event.key == self.mod_Pygame__.K_e:
                                if self.Fullscreen == False:
                                    myScreenshot = self.mod_Pyautogui__.screenshot(region=((0, 0, self.FullscreenX, self.FullscreenY)))
                                    myScreenshot.save(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))
                                else:
                                    PosX, PosY = self.mod_DisplayUtils__.DisplayUtils.GetDisplayLocation(self)
                                    myScreenshot = self.mod_Pyautogui__.screenshot(region=((PosX, PosY, self.realWidth, self.realHeight)))
                                    myScreenshot.save(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))
                                return None, "Inventory"
                            if event.key == self.mod_Pygame__.K_F11:
                                Message = self.mod_DisplayUtils__.DisplayUtils.UpdateOPENGLdisplay(self)
                                self.mod_OpenGL_GLU_.gluPerspective(FOV, (self.realWidth/self.realHeight), 1, 8000000)
                                self.mod_OpenGL_GL_.glShadeModel(self.mod_OpenGL_GL_.GL_SMOOTH)
                                self.mod_OpenGL_GL_.glMatrixMode(self.mod_OpenGL_GL_.GL_MODELVIEW)
                                if self.aa == True:
                                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_MULTISAMPLE)
                                elif self.aa == False:
                                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_MULTISAMPLE)
                                self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_FRAMEBUFFER_SRGB)
                            if event.key == self.mod_Pygame__.K_r:
                                return None, "MapGUI"
                            if event.key == self.mod_Pygame__.K_w:
                                WKeyPressed = True
                            if event.key == self.mod_Pygame__.K_s:
                                SKeyPressed = True
                            if event.key == self.mod_Pygame__.K_SPACE and Jump == False: 
                                Jump = True
                            if event.key == self.mod_Pygame__.K_l:
                                if MouseUnlock == True:
                                    MouseUnlock = False
                                    self.mod_Pygame__.mouse.set_visible(True)
                                elif MouseUnlock == False:
                                    MouseUnlock = True
                                    self.mod_Pygame__.mouse.set_visible(False)
                            if event.key == self.mod_Pygame__.K_q:
                                self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)
                                self.mod_Pygame__.mouse.set_pos((self.realWidth/2), (self.realHeight/2))
                        if event.type == self.mod_Pygame__.KEYUP:
                            if event.key == self.mod_Pygame__.K_w:
                                WKeyPressed = False
                            if event.key == self.mod_Pygame__.K_a:
                                AKeyPressed = False
                            if event.key == self.mod_Pygame__.K_s:
                                SKeyPressed = False
                            if event.key == self.mod_Pygame__.K_d:
                                DKeyPressed = False
                        
                        if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:
                            if event.button == 4:
                                self.mod_OpenGL_GL_.glTranslatef(0, 0, 1)
                            if event.button == 5:
                                self.mod_OpenGL_GL_.glTranslatef(0, 0, -1)

                        if event.type == self.mod_Pygame__.MOUSEMOTION and MouseUnlock == True:
                            Mx, My = self.mod_Pygame__.mouse.get_pos()
                            mouseMovement = (Mx-int(self.realWidth/2), My-int(self.realHeight/2))
                            self.mod_Pygame__.mouse.set_pos(int(self.realWidth/2), int(self.realHeight/2))

                    if WKeyPressed == True:
                        WkeydownTimer += 1
                        if stop == False:
                            time = self.eFPS*3
                            stop = True
                        if time >= 0:
                            self.Total_move_z += 35
                            if WkeydownTimer/(self.aFPS/self.Iteration) >= ((self.mod_Random__.randint(75, 100))/100):
                                if self.sound == True:
                                    self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                                WkeydownTimer = 0
                        elif time <= 0:
                            if WkeydownTimer/(self.aFPS/self.Iteration) >= ((self.mod_Random__.randint(40, 50))/100):
                                if self.sound == True:
                                    self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                                WkeydownTimer = 0
                            self.Total_move_z += 100

                        time -= 1
                    else:
                        stop = False
                        WkeydownTimer = 0

                    if AKeyPressed == True:
                        self.Total_move_x += -35 
                        AkeydownTimer += 1

                        if AkeydownTimer/(self.aFPS/self.Iteration) >= ((self.mod_Random__.randint(75, 100))/100):
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                            AkeydownTimer = 0
                    else:
                        AkeydownTimer = 0

                    if SKeyPressed == True:
                        self.Total_move_z += -35 
                        SkeydownTimer += 1

                        if SkeydownTimer/(self.aFPS/self.Iteration) >= ((self.mod_Random__.randint(75, 100))/100):
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                            SkeydownTimer = 0
                    else:
                        SkeydownTimer = 0

                    if DKeyPressed == True:
                        self.Total_move_x += 35 
                        DkeydownTimer += 1

                        if DkeydownTimer/(self.aFPS/self.Iteration) >= ((self.mod_Random__.randint(75, 100))/100):
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                            DkeydownTimer = 0
                    else:
                        DkeydownTimer = 0

                    
                    if Jump == True:
                        JumpID += 1
                        if JumpID <= 20:
                            JumpID += 1
                            self.Total_move_y += 100
                        if JumpID >= 21:
                            JumpID += 1
                            self.Total_move_y -= 100
                        if JumpID >= 40:
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                            Jump = False
                            JumpID = 0

                    if MouseUnlock == True:
                        if mouseMovement[0] >= 1:
                            self.TotalRotation += 1
                            rotationvectX += 0.5
                            
                        if mouseMovement[0] <= -1:
                            self.TotalRotation -= 1
                            rotationvectX += -0.5

                    self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT)
                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_DEPTH_TEST)
                    self.mod_OpenGL_GL_.glPushMatrix()
                    self.mod_OpenGL_GL_.glDepthMask(self.mod_OpenGL_GL_.GL_FALSE)
                    self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT|self.mod_OpenGL_GL_.GL_STENCIL_BUFFER_BIT)
                    self.mod_OpenGL_GL_.glDepthMask(self.mod_OpenGL_GL_.GL_TRUE)
                    self.mod_OpenGL_GL_.glPopMatrix()
                    self.mod_OpenGL_GL_.glPolygonMode(self.mod_OpenGL_GL_.GL_FRONT_AND_BACK, self.mod_OpenGL_GL_.GL_FILL)
                    self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Playing")
                    '''if camera_x == prev_camera_x and camera_y == prev_camera_y and camera_z == prev_camera_z and (not firstRUN == 1):
                        self.Collisions = prev_collisions
                    else:
                        prev_camera_x = camera_x
                        prev_camera_y = camera_y
                        prev_camera_z = camera_z
                        prev_collisions = self.Collisions
                    #print(self.Collisions)
                    if self.Collisions[0] == False:
                        self.Total_move_y -= 1
                    elif self.Collisions[0] == True:
                        if self.Collisions[1] < camera_y and self.Collisions[1] < camera_y-1:
                            self.Total_move_y -= 1
                        elif self.Collisions[1] > camera_y and self.Collisions[1] > camera_y+1:
                            self.Total_move_y += 1'''
                    if firstRUN == 1:
                        self.mod_OpenGL_GL_.glTranslatef(0, 50000, 0)
                        prev_camera_x = camera_x
                        prev_camera_y = camera_y
                        prev_camera_z = camera_z
                    else:
                        firstRUN = 2
                    if camera_x >= (1150*self.G3Dscale) or camera_x <= (-1150*self.G3Dscale) or camera_z >= (700*self.G3Dscale) or camera_z <= (-1150*self.G3Dscale):
                        print("World Boarder Reached")

                    Message = self.mod_SkyBoxUtil__.SkyBox.DrawSkyBox(self)
                    if not Message == None:
                        return Message, "Undefined"
                    
                    if not Message == None:
                        return Message, "Undefined"
                    
                    self.mod_MapTextureUtil__.MapTexture.DrawMapTexture(self)
                    if not Message == None:
                        return Message, "Undefined"

                    #dima 2021-10-25 BEGIN
                    self.mod_OpenGL_GL_.glPushMatrix()
                    self.Map_trans[0] = self.Map_trans[0]+self.Total_move_x
                    self.Map_trans[1] = self.Map_trans[1]-(self.Total_move_y)
                    self.Map_trans[2] = self.Map_trans[2]+self.Total_move_z
                    self.mod_OpenGL_GL_.glScalef(*self.Map_scale)
                    self.mod_OpenGL_GL_.glTranslatef(*self.Map_trans)
                    
                    self.mod_OpenGL_GL_.glRotatef(self.TotalRotation, 0, 1, 0)
                
                    for meshVBO in mapVBOMeshInds:
                        self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_CULL_FACE)
                        self.mod_OpenGL_GL_.glCullFace(self.mod_OpenGL_GL_.GL_BACK)
                        self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, mapVBOVertsId)
                        self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, meshVBO[0])
                        
                        self.mod_OpenGL_GL_.glVertexPointer(3, self.mod_OpenGL_GL_.GL_FLOAT, vertsArr.itemsize * 3, None)
                        self.mod_OpenGL_GL_.glEnableClientState(self.mod_OpenGL_GL_.GL_VERTEX_ARRAY)

                        self.mod_OpenGL_GL_.glDrawElements(self.mod_OpenGL_GL_.GL_TRIANGLES, meshVBO[1], self.mod_OpenGL_GL_.GL_UNSIGNED_INT, None)
                        
                        self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, 0)
                        self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, 0)
                        
                        self.mod_OpenGL_GL_.glDisableClientState(self.mod_OpenGL_GL_.GL_VERTEX_ARRAY)
                    
                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_CULL_FACE)
                    
                    self.mod_OpenGL_GL_.glBindTexture(self.mod_OpenGL_GL_.GL_TEXTURE_2D, 0)
                    
                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_BLEND)

                    self.mod_OpenGL_GL_.glPopMatrix()

                    #dima 2021-10-25 END

                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_LIGHTING)
                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_LIGHT0)
                    self.mod_OpenGL_GL_.glLightfv(self.mod_OpenGL_GL_.GL_LIGHT0, self.mod_OpenGL_GL_.GL_POSITION, (0, camera_y+100, 0))
                    self.mod_OpenGL_GL_.glLightfv(self.mod_OpenGL_GL_.GL_LIGHT0, self.mod_OpenGL_GL_.GL_AMBIENT, (1, 0, 1, 1))
                    self.mod_OpenGL_GL_.glLightfv(self.mod_OpenGL_GL_.GL_LIGHT0, self.mod_OpenGL_GL_.GL_DIFFUSE, (1, 0, 1, 1))
                    self.mod_OpenGL_GL_.glLightfv(self.mod_OpenGL_GL_.GL_LIGHT0, self.mod_OpenGL_GL_.GL_SPECULAR, (1, 0, 1, 1))
                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_COLOR_MATERIAL)
                    self.mod_OpenGL_GL_.glColorMaterial(self.mod_OpenGL_GL_.GL_FRONT_AND_BACK, self.mod_OpenGL_GL_.GL_AMBIENT_AND_DIFFUSE)
                    self.mod_OpenGL_GL_.glMaterial(self.mod_OpenGL_GL_.GL_FRONT_AND_BACK, self.mod_OpenGL_GL_.GL_SPECULAR, (0, 1, 0, 1))
                    self.mod_OpenGL_GL_.glMaterial(self.mod_OpenGL_GL_.GL_FRONT_AND_BACK, self.mod_OpenGL_GL_.GL_EMISSION, (0, 1, 0, 1))

                    self.mod_OpenGL_GL_.glTranslatef(0, 0-camera_y, 0)
                    PlayerModel_pos_x, PlayerModel_pos_y, PlayerModel_pos_z = -self.Total_move_x, -self.Total_move_y, -self.Total_move_z
                    self.Total_move_x, self.Total_move_y, self.Total_move_z = 0, 0, 0
                    self.mod_Pygame__.display.flip()
                    self.clock.tick(self.FPS)
            except Exception as Message:
                print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))
                return Message, "Undefined"
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()