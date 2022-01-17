#%%
import pygame,os
#%%
title='Platformer'
screen_size=screen_width,screen_height=1280,720 # 32 18
FPS=60

player_size=player_w,player_h=40,40
tile_size=tile_w,tile_h=40,40

player_speed=5

current_path=os.path.dirname(os.path.abspath(__file__))
image_path=os.path.join(current_path,'image')
character_image_path=os.path.join(image_path,'character')
character_action_image_path=os.path.join(character_image_path,'action')
print(character_action_image_path)