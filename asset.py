from re import I
from setting import *

class Asset:
    def __init__(self):
        self.get_character_image()
    
    def get_character_image(self):
        self.character_images={'idle':[],'run':[],'jump':[],'fall':[]}
        for status in self.character_images.keys():
            for file in os.listdir(os.path.join(character_action_image_path,status)):
                self.character_images[status].append(pygame.image.load(\
                    os.path.join(character_action_image_path+'/'+status,file)).convert_alpha())