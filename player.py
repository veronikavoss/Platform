from setting import *

# https://youtu.be/YWN8GcmJ-jA?t=3548

class Player(pygame.sprite.Sprite):
    def __init__(self,asset,topleft):
        super().__init__()
        self.asset=asset
        self.action='idle'
        self.frame_index=0
        self.animation_speed=0
        self.image=self.asset.character_images[self.action][self.frame_index]
        self.flip=False
        
        self.rect=self.image.get_rect(topleft=topleft)
        self.direction=pygame.math.Vector2(0,0)
        self.dx,self.dy=self.direction.x,self.direction.y
        self.move_speed=5
        self.jump_speed=-15
        self.gravity=0.8
        self.jumped=False
    
    def animation(self):
        animation=self.asset.character_images[self.action]
        self.frame_index+=0.1
        if self.frame_index>=len(animation):
            self.frame_index=0
        self.image=animation[int(self.frame_index)]
    
    def set_key_input(self):
        key_input=pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            self.flip=True
            self.dx=-self.move_speed
        elif key_input[pygame.K_RIGHT]:
            self.flip=False
            self.dx=self.move_speed
        else:
            self.dx=0
        
        if key_input[pygame.K_UP]:
            if not self.jumped:
                self.dy=self.jump_speed
                self.jumped=True
        else:
            self.jumped=False
    
    def set_action(self):
        if self.dy<0:
            self.action='jump'
        elif self.dy>1:
            self.action='fall'
        else:
            if self.dx!=0:
                self.action='run'
            else:
                self.action='idle'
    
    def collision(self,tiles):
        self.dy+=self.gravity
        self.rect.y+=self.dy
        for tile in tiles:
            if pygame.sprite.collide_rect(self,tile):
                if self.dy>=0:
                    self.dy=0
                    self.rect.bottom=tile.rect.top
        
        self.rect.x+=self.dx
        for tile in tiles:
            if pygame.sprite.collide_rect(self,tile):
                if self.dx<0:
                    self.rect.left=tile.rect.right
                elif self.dx>0:
                    self.rect.right=tile.rect.left
    
    def update(self,tiles):
        self.animation()
        self.set_key_input()
        self.set_action()
        self.collision(tiles)