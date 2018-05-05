import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()   #初始化背景设置
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))    #设置屏幕
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(ai_settings,screen)
    bullets=Group()
    while True:     #控制时间循环以及管理屏幕更新
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,bullets)


run_game()