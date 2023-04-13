import random
import pygame


'''стена'''
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


'''Еда'''
class Food(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, bg_color, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y


''' класс игроков'''
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, role_image_path):
        pygame.sprite.Sprite.__init__(self)
        self.role_name = role_image_path.split('/')[-1].split('.')[0]#обсудить с аней
        self.base_image = pygame.image.load(role_image_path).convert()
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.prev_x = x
        self.prev_y = y
        self.base_speed = [30, 30]
        self.speed = [0, 0]
        self.is_move = False
        self.tracks = []
        self.tracks_loc = [0, 0]
    '''Изменить направление скорости'''
    def changeSpeed(self, direction):
        if direction[0] < 0:
            self.image = pygame.transform.flip(self.base_image, True, False)
        elif direction[0] > 0:
            self.image = self.base_image.copy()
        elif direction[1] < 0:
            self.image = pygame.transform.rotate(self.base_image, 90)
        elif direction[1] > 0:
            self.image = pygame.transform.rotate(self.base_image, -90)
        self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]
        return self.speed
    '''Обновить позицию персонажа'''
    def update(self, wall_sprites, gate_sprites,numba):
        if not self.is_move:
            return False
        x_prev = self.rect.left
        y_prev = self.rect.top
        if numba == 1:
            if x_prev < 0:
                self.rect.x = 587
            elif x_prev > 606:
                self.rect.x = 17
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, False)
        if gate_sprites is not None:
            if not is_collide:
                is_collide = pygame.sprite.spritecollide(self, gate_sprites, False)
        if is_collide:
            self.rect.left = x_prev
            self.rect.top = y_prev
            return False
        return True
    '''Создавать случайные направления'''
    def randomDirection(self):
        return random.choice([[-0.5, 0], [0.5, 0], [0, 0.5], [0, -0.5]])