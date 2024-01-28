#===============================MATTHEW'S DISCLAIMER (important but dw)======================================#
# Before actually running the program, just download the 1 ttf file named Specialfont to your Control Panel
# This basically allows you to view the font that the title has
# Also, install rainbow CSV so that your eyes don't burn... That is all!!!!!
# Made by: Ryan Schnur, Matthew De Guzman (De Guzzi if ur Ryan) ft. Ethan LacayoDalton (bro was on Destiny 2 for 13 hours)
#==========================================IMPORT STATEMENTS=================================================#
import pygame as p, sys, time as t, pandas as pd, matplotlib.pyplot as plot
#======================================initilization and startup=============================================#
p.init() # initializing pygame
surface = p.display.set_mode((1200, 1000))
p.display.set_caption("De Guzzi") # ryan bruh moemnt
FPS = p.time.Clock()
#Images - loading images to be more specific
time_travel = p.image.load("time-travel.png")
p.display.set_icon(time_travel)
Clock = p.image.load("express.png")
Clocker = p.image.load("time-travelling.png")
# the states - fields
main = "main"
playAlt = "playAlt" #duplicate play field
play = "play"
quit = "quit"
state = main
running = True
#font
Normal_font = p.font.Font(None, 28)
Bigger_font = p.font.Font("Specialfont.ttf", 50)
#text
Stext = Normal_font.render("Start", True, "black")
Etext = Normal_font.render("Exit", True, "black")
#flag - magically useful, but also why idek bro y i made this just trust me i swear or ask ryan he made the function
def Flagg1():
    global Flag1
    Flag1 = False
    t.sleep(.15)
    Flag1 = True
Flag1 = True
#Decorations
def decor():
    surface.blit(Clock, (100, 1000))
    surface.blit(Clocker, (100, 200))
    surface.blit(Clock, (800, 1100))
    surface.blit(Clocker, (800, 700))
#Button class - pain
class Button:
    def __init__(self, x, y, color, width, height, text, size, font):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.rect = p.Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.size = size
        self.font = font
        Normal_font = p.font.Font(self.font, self.size)
        self.text = Normal_font.render(self.text, True, "black")
    def play(self):
        p.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text, (self.x, self.y))
    def playAlt(self): #play function but I duplicated
        p.draw.rect(surface, self.color, self.rect)
        surface.blit(self.text, (self.x, self.y))
    def collision(self):
        global state
        global Flag1
        # Updates mouse position
        pos = p.mouse.get_pos()
        #Checks if you click the PlayBtn rect, right click with mouse, and if the state is in main. If it is then the state turns to play and the new screen is shown - look below.
        if PlayBtn.rect.collidepoint(pos) and p.mouse.get_pressed()[0] and state == main: # start button collision
            if Flag1 == True:
                state = play
                Flagg1()
        if ExitBtn.rect.collidepoint(pos) and p.mouse.get_pressed()[0] and state == main: # exit button collision
            if Flag1 == True:
                state = quit
        if PlayBtn2.rect.collidepoint(pos) and p.mouse.get_pressed()[0] and state == main: # 2nd panel collision detection 
            if Flag1 == True:
                state = playAlt
                Flagg1()
PlayBtn = Button(430, 515, "green", 140, 50, "View US Inflation", 22, None) # end me - Matthew
PlayBtn2 = Button(430, 430, "blue", 140, 50, "View US National Debt", 18, None) # 2nd play button for other chart.
ExitBtn = Button(630, 515, "red", 100, 50, "Exit", 28, None) # end button
TravelBtn = Button(375,200, (231,255,153), 300, 100, "Go View History...Through the US!", 45, "Specialfont.ttf") # have to download ttf file to control panel - Matthew
og_state = main #because I couldnt find way to revert the value of exit to main, I just added a placeholder value for it
# ^^^ btw og just stands for original if u didnt know hence original state -Matthew
while running: # actual project - where it runs
    if state == main:
        surface.fill((231,255,153))
        PlayBtn.play()
        PlayBtn2.play()
        ExitBtn.play()
        decor()
        TravelBtn.play()
        PlayBtn2.collision() # dw dont mind the order. SOurce: Trust me bro
        PlayBtn.collision()
    if state == play:
        surface.fill((255, 255, 255))
        ExitBtn.play()
        ExitBtn = Button(1100, 115, "red", 100, 50, "Exit", 28, None)
        if ExitBtn.rect.collidepoint(pos) and p.mouse.get_pressed()[0]: # dont include "and state == main" bc state already main
            state = og_state # resets back to main screen
            ExitBtn = Button(630, 515, "red", 100, 50, "Exit", 28, None) #just reets exit button position, no biggie
        fig, ax = plot.subplots() #Creates subplot so that plot isnt permanent later on in program -Matthew
        #Reads file, when does my gd addiction end: will the pain ever stop, or does the grind continue - Matthew
        data = pd.read_csv("InflationData.csv", header=0) 
        ax.plot(data['Year'], data['Ave'], color='green')
        ax.set_ylabel('Year') #have to set each of the labels to transfer it on to pyagem srceen
        ax.set_xlabel('Average Inflation Rate') 
        ax.set_title('Average US Inflation per Year')
        plot.savefig("inflation_plot.png", format='png') #temporarliy svaing plot onto a png
        #Load plot, saves png onto Pygame (so its not a pop-up window)
        img = p.image.load("inflation_plot.png")
        # Display Matplotlib plot on Pygame surface
        surface.blit(img, (100, 100))  # Adjust the position as needed
    if state == playAlt: # almost the same as the other PlayBtn, but few tweaks
        surface.fill((255,255,255))
        ExitBtn.play()
        ExitBtn = Button(1100, 115, "red", 100, 50, "Exit", 28, None)
        if ExitBtn.rect.collidepoint(pos) and p.mouse.get_pressed()[0]: #copy and paste of the other btn exit
            state = og_state                                            # except removed commetns
            ExitBtn = Button(630, 515, "red", 100, 50, "Exit", 28, None) 
        fig, ax2 = plot.subplots()
        data_debt = pd.read_csv("DebtData.csv", header=0)
        ax2.plot(data_debt['Date'], data_debt['National_Debt'], color='blue')
        ax2.set_ylabel('Debt (USD)')
        ax2.set_xlabel('Year)')
        ax2.set_title('US NATIONAL DEBT')
        plot.savefig("debt_plot.png", format ='png') #saves debt plot temporarily
        img_debt = p.image.load("debt_plot.png") #loads it onto pygame screen
        surface.blit(img_debt, (100, 100))
    if state == quit:
        p.quit()
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    pos = p.mouse.get_pos()# resets mouse pos inside the loop

    FPS.tick(60) # ask ryan
    p.display.update() # updates "game"
#======================================================END=(me pls, finsihed 1:13 A.M.)===================================================#