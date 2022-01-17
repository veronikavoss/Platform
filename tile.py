from setting import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(tile_size)
        self.image.fill('brown')
        self.rect=self.image.get_rect(x=x,y=y)