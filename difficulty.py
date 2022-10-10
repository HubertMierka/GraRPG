import pygame

import settings
from settings import *

class Difficulty:
    def __init__(self):
        self.dispay_surface = pygame.display.get_surface()

        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.selection_index = 0
        self.selection_time = None
        self.can_move = True

        self.atribute_nr = 2
        self.difficulty = settings.DIFFICULTY

        self.height = self.dispay_surface.get_size()[1] * 0.8
        self.width = self.dispay_surface.get_size()[0] // (self.atribute_nr + 1)


    def input(self):
        keys = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_RIGHT] and self.selection_index < self.atribute_nr -1:
                self.selection_index += 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            elif keys[pygame.K_LEFT] and self.selection_index >= 1:
                self.selection_index -= 1
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
            if keys[pygame.K_SPACE]:
                self.can_move = False
                self.selection_time = pygame.time.get_ticks()
                #self.item_list[self.selection_index].trigger(self.player)
                print('index')

    def create_items(self):
        self.item_list = []

        for item, index in enumerate(range(self.atribute_nr)):

            top = self.dispay_surface.get_size()[1] * 0.1
            full_width = self.dispay_surface.get_size()[0]
            increment = full_width // self.atribute_nr
            left = (item * increment) + (increment - self.width) // 2

            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)

    def selection_cooldown(self):
        if not self.can_move:
            currenttime =  pygame.time.get_ticks()
            if currenttime - self.selection_time >= 300:
                self.can_move = True

    def display(self):
        self.input()
        self.selection_cooldown()
        self.create_items()

        for index, item in enumerate(self.item_list):
            name = self.difficulty[index]
            #value = self.player.get_value_by_index(index)
            #max_value = self.max_values[index]
            #cost = self.player.get_cost_by_index(index)
            item.dispaly(self.dispay_surface,self.selection_index,name)

class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font

    def display_names(self, surface, name, selected):
        color = UI_BORDER_COLOR_ACTIVE if selected else TEXT_COLOR
        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 20))

        surface.blit(title_surf, title_rect)


    def dispaly(self,surface,selection_num,name):
        if self.index == selection_num:
            pygame.draw.rect(surface, UI_SELECTED_BOX_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        else:
            pygame.draw.rect(surface,UI_BG_COLOR,self.rect)
            pygame.draw.rect(surface,UI_BORDER_COLOR,self.rect,4)
        self.display_names(surface,name,self.index == selection_num)