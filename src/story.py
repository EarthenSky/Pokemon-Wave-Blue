import sys
import time
import pygame
import __builtin__

import npc

sys.path.insert(0, 'src/managers/')  # This line tells the importer where to look for the module.
import desc_manager
import pokemon_manager


class Story:

    def __init__(self, surface):
        self.inlab=False
        self.current_story_level = 0    # Current part of the story you're in
        self.player_pos = __builtin__.g_player.position # Gets players position
        self.oak_grass_pos = __builtin__.g_oak_grass.position_offset    # Gets oaks position in grass
        self.surface = surface  # Display surface

        self.oak_list = __builtin__.g_oak_list
        self.trainer_one = g_trainer_one

    def update(self):
        #print self.player_pos
        if self.inlab == True:

            desc_manager.add_message_to_queue("Here, have a few pokemon", "they will protect you-")

            pokemon_manager.pokemon_list.append( pokemon_manager.create_random_enemy() )  # Give player a random pokemon.
            pokemon_manager.pokemon_list.append( pokemon_manager.create_random_enemy() )  # Give player a random pokemon.
            pokemon_manager.pokemon_list.append( pokemon_manager.create_random_enemy() )  # Give player a random pokemon.
            pokemon_manager.pokemon_list.append( pokemon_manager.create_random_enemy() )  # Give player a random pokemon.
            pokemon_manager.pokemon_list.append( pokemon_manager.create_random_enemy() )  # Give player a random pokemon.

            desc_manager.check_queue(self.surface)
            desc_manager.add_message_to_queue("when you are in danger.", "You can also battle with them.")
            desc_manager.check_queue(self.surface)
            desc_manager.add_message_to_queue("Try to get as strong a pokemon", "as possible Good luck!")
            desc_manager.check_queue(self.surface)

            self.current_story_level = 1

            self.oak_list.remove(g_oak_grass)

            self.inlab = False

        if self.player_pos[1] <= -16 and self.current_story_level == 0:
            self.oak_grass_pos[1] = -80

            desc_manager.add_message_to_queue("Come with me to my lab", "...")
            desc_manager.add_message_to_queue("Watch out for the tall grass,", "pokemon might be hiding there.")
            desc_manager.check_queue(self.surface)
            __builtin__.g_current_scene = LAB
            __builtin__.g_player.set_pos( (448, 384) )
            self.inlab = True

        #if self.current_story_level == 1:
        #    if self.player_pos[1] == -656:
        #        for i in range(1):
        #            self.trainer_one.walk_left(1, 2)
        #        desc_manager.add_message_to_queue("Fight me bro!", "")
        #        desc_manager.check_queue(self.surface)
        #        self.current_story_level = 2
