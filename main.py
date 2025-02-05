from inter import *
import inter as i
import pygame  
import sys
from makescene import *
import constants as c
# import heartrate
# heartrate.trace(browser=True,files=heartrate.files.all)
def loop(me,clock,win):
    fpscnt=0
    back_ground_color=(200, 200, 200)
    while True:
        win.fill(back_ground_color)
        clock.tick(c.FPS)
        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #me.dx=1
        #me.dy=0
        #me.moving=10
        # me.keyboard()
        catchKeyboard(me,dialoger)

        a=i.thisMap
        me.clock(a)
        # me.draw(3,fpscnt,(0,0),win)
        car=i.thisMap.genCamera()
        i.thisMap.clock()
        i.thisMap.draw(fpscnt,car,win)

        # segmentDraw.drawR(1,15,4,car,win)
        # segmentDraw.drawC(1,15,4,car,win)
        # segmentDraw.drawSqure(9,4,6,2,car,win)

        # dialoger.keyboard()
        dialoger.draw(win)
        bottomBar.drawHP(me.hp,win)
        # print(car)
        # print(me.hp)
        # print(me.gx, me.gy)
        fpscnt+=1
        pygame.display.update()

def main(win):
    import imageconstants as cc
    pygame.display.set_caption("Bubbles Valley")#窗口名字和图标
    img = pygame.image.load('./assets/utils/icon1.ico')
    pygame.display.set_icon(img)

    backgroundMusic[0].play(-1)
    """
    地图初始化
    """
    i.thisMap=Mapper(50,50,style=0)
    mapGener(i.thisMap) # 田野
    maps.append(i.thisMap)
    i.thisMap=Mapper(50,50,style=1)
    nw=i.thisMap
    mapGenerTown(i.thisMap) # 城镇
    maps.append(i.thisMap)
    i.thisMap=Mapper(50,50,style=2)
    #thisMap.me=me
    mapGenerShop(i.thisMap) # 商店
    #thisMap.me=None
    maps.append(i.thisMap) #"山洞"
    i.thisMap=Mapper(50,50,style=0)
    mapGenerDeep(i.thisMap)
    maps.append(i.thisMap)
    i.thisMap=nw
    ###
    # thisMap=Mapper(50,50,style=0)
    # tempMapGener(thisMap)
    ###

    me=player(id=0,gx=3,gy=17,imagesdir='./assets/player/',layer=3)

    clock = pygame.time.Clock() # 用于控制循环刷新频率的对象
    i.thisMap.me=me

    #for i in i.thisMap.mp[me.gx][me.gy]["entity"]:
    #    print(i)
    """
    开始界面
    """
    start = True
    win.fill((255, 255, 255))
    button = 0

    while start:
        win.convert()
        clock.tick(c.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if button > 0:
                        button -= 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if button < 1:
                        button += 1
                if event.key == pygame.K_RETURN:
                    if button == 0:
                        start = False
                        stop_music(backgroundMusic[0])
                        play_music(backgroundMusic[1+1])
                        # i.thisMapId = 1
                        break
                    elif button == 1:
                        pygame.quit()
                        sys.exit()
        win.blit(cc.startSceneImg, cc.startSceneRect)
        if button == 0:
            win.blit(cc.arrowImg, cc.arrowRect1)
        elif button == 1:
            win.blit(cc.arrowImg, cc.arrowRect2)
        if c.BottomBarMode==1 : bottomBar.draw([f'./assets/scene/obstacle0.{i}.png' for i in range(1,12)]+[f'./assets/scene/object{i}.png' for i in range(1,6)],win)
        pygame.display.update()
    # 开始界面 End

    try:
        loop(me,clock,win)
    except Exception as inst:
        Img=cc.GameOverImg
        print(inst)
        match str(inst):
            case "GAMEOVER":
                Img=cc.GameOverImg
            case "Ending1":
                Img=cc.Ending1Img
            case "Ending2":
                Img=cc.Ending2Img
            case _ : raise inst 
    
        while True:
            clock.tick(c.FPS)
            flag=False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key==c.KeyboardConDialog:
                    flag=True
            if flag:
                for t in backgroundMusic:stop_music(t)
                break
            win.blit(Img,Img.get_rect())
            if str(inst)=="GAMEOVER" and c.BottomBarMode==1 : bottomBar.draw(['./assets/scene/bomb0.png']*3,win)
            pygame.display.update()
    """重新启动程序"""
    import os
    python = sys.executable
    os.execl(python, python, *sys.argv)

if __name__ == "__main__":
    pygame.init()
    win=displayCreateWin()
    while(True):main(win)
