import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()   #初始化背景设置
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))    #设置屏幕
    pygame.display.set_caption("Alien Invasion")
    ship=Ship(ai_settings,screen)
    while True:     #控制时间循环以及管理屏幕更新
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)


run_game()