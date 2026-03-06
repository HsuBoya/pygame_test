import pygame as pg

#pygame初始化
pg.init()

#設定視窗
width,height= 640,480
screen =pg.display.set_mode((width,height))
pg.display.set_caption("BOYA's Game") #程式標題

#畫布BG
#背景變數 = pygame.Surface(screen.get_size())    #get_size()取得視窗尺寸
#背景變數 = 背景變數.convert()                    
#convert()建立副本，加快畫布在視窗顯示速度
#背景變數.fill((0,0,0))      #黑色
#視窗變數.blit(背景變數, 繪製位置)  #繪製覆蓋整個視窗
bg = pg.Surface(screen.get_size())
bg = bg.convert()
bg.fill((255,255,255)) #白色

#顯示
screen.blit(bg,(0,0))
pg.display.update()

#繪製幾何圖形
#矩形 pygame.draw.rect(畫布, 顏色, [x坐標, y坐標, 寬度, 高度], 線寬)
#圓形 pygame.draw.circle(畫布, 顏色, (x坐標, y坐標), 半徑, 線寬)
#橢圓形 pygame.draw.ellipse(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 線寬)
#圓弧形 pygame.draw.arc(畫布, 顏色, [x坐標, y坐標, x直徑, y直徑], 起始角, 結束角, 線寬)
#直線 pygame.draw.line(畫布, 顏色, (x坐標1, y坐標1), (x坐標2, y坐標2), 線寬)


#關閉程式的程式碼
running = True

while running:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False

pg.quit()