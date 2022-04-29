"""
This file is part of mcpit.

mcpit is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

mcpit is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with mcpit. If not, see <https://www.gnu.org/licenses/>.
"""
from PIL import Image

POSITIONS = {
    # Row 1
    "grass_carried": (0, 0, 16, 16),
    "stone": (16, 0, 32, 16),
    "dirt": (32, 0, 48, 16),
    "grass_side_carried": (48, 0, 64, 16),
    "planks_oak": (64, 0, 80, 16),
    "stone_slab_side": (80, 0, 96, 16),
    "stone_slab_top": (96, 0, 112, 16),
    "brick": (112, 0, 128, 16),
    "tnt_side": (128, 0, 144, 16),
    "tnt_top": (144, 0, 160, 16),
    "tnt_bottom": (160, 0, 176, 16),
    "web": (176, 0, 192, 16),
    "flower_rose": (192, 0, 208, 16),
    "flower_dandelion": (208, 0, 224, 16),
    "sapling_oak": (240, 0, 256, 16),
    # Row 2
    "cobblestone": (0, 16, 16, 32),
    "bedrock": (16, 16, 32, 32),
    "sand": (32, 16, 48, 32),  # I love these blocks
    "gravel": (48, 16, 64, 32),
    "oak_log": (64, 16, 80, 32),
    "oak_log_top": (80, 16, 96, 32),
    "iron_block": (96, 16, 112, 32),
    "gold_block": (112, 16, 128, 32),
    "diamond_block": (128, 16, 144, 32),
    "chest_top": (144, 16, 160, 32),
    "chest_side": (160, 16, 176, 32),
    "chest_front": (176, 16, 192, 32),
    "mushroom_red": (192, 16, 208, 32),
    "mushroom_brown": (208, 16, 224, 32),
    "fire_0_placeholder": (240, 16, 256, 32),
    # Row 3
    "gold_ore": (0, 32, 16, 48),
    "iron_ore": (16, 32, 32, 48),
    "coal_ore": (32, 32, 48, 48),
    "bookshelf": (48, 32, 64, 48),
    "cobblestone_mossy": (64, 32, 80, 48),
    "obsidian": (80, 32, 96, 48),
    "grass_side": (96, 32, 112, 48),
    "tallgrass": (112, 32, 128, 48),
    "grass_top": (128, 32, 144, 48),
    "crafting_table_top": (176, 32, 192, 48),
    "furnace_front": (192, 32, 208, 48),
    "furnace_side": (208, 32, 224, 48),
    "fire_1_placeholder": (240, 32, 256, 48),
    # Row 4
    "glass": (16, 48, 32, 64),
    "diamond_ore": (32, 48, 48, 64),
    "redstone_ore": (48, 48, 64, 64),
    "leaves_oak_carried": (64, 48, 80, 64),
    "leaves_big_oak_carried": (80, 48, 96, 64),
    "stonebrick": (96, 48, 112, 64),
    "deadbush": (112, 48, 128, 64),
    "shrub": (128, 48, 144, 64),
    "crafting_table_side": (176, 48, 192, 64),
    "crafting_table_front": (192, 48, 208, 64),
    "furnace_front_on": (208, 48, 224, 64),
    "furnace_top": (224, 48, 240, 64),
    "spruce_sapling": (240, 48, 256, 64),
    # Row 5
    "white_wool": (0, 64, 16, 80),
    "snow": (32, 64, 48, 80),
    "ice": (48, 64, 64, 80),
    "grass_block_snow": (64, 64, 80, 80),
    "cactus_top": (80, 64, 96, 80),
    "cactus_side": (96, 64, 112, 80),
    "cactus_bottom": (112, 64, 128, 80),
    "clay": (128, 64, 144, 80),
    "sugarcane_extracted": (144, 64, 160, 80),
    "birch_sapling": (240, 64, 256, 80),
    # Row 6
    "torch": (0, 80, 16, 96),
    "oak_door_top": (16, 80, 32, 96),
    "iron_door_top": (32, 80, 48, 96),
    "ladder": (48, 80, 64, 96),
    "oak_trapdoor": (64, 80, 80, 96),
    "farmland_moist": (96, 80, 112, 96),
    "farmland": (112, 80, 128, 96),
    "wheat_stage0": (128, 80, 144, 96),
    "wheat_stage1": (144, 80, 160, 96),
    "wheat_stage2": (160, 80, 176, 96),
    "wheat_stage3": (176, 80, 192, 96),
    "wheat_stage4": (192, 80, 208, 96),
    "wheat_stage5": (208, 80, 224, 96),
    "wheat_stage6": (224, 80, 240, 96),
    "wheat_stage7": (240, 80, 256, 96),
    # Row 7
    "oak_door_bottom": (16, 96, 32, 112),
    "iron_door_bottom": (32, 96, 48, 112),
    "mossy_stone_bricks": (48, 96, 64, 112),
    "cracked_stone_bricks": (64, 96, 80, 112),
    "netherrack": (96, 96, 112, 112),
    "soul_sand": (112, 96, 128, 112),
    "glowstone": (128, 96, 144, 112),
    "melon_stem": (240, 96, 256, 112),
    # Row 8
    "black_wool": (16, 112, 32, 128),
    "gray_wool": (32, 112, 48, 128),
    "dark_oak_log": (64, 112, 80, 128),
    "birch_log": (80, 112, 96, 128),
    "attached_melon_stem": (240, 112, 256, 128),
    # Row 9
    "red_wool": (16, 128, 32, 144),
    "pink_wool": (32, 128, 48, 144),
    "birch_leaves": (48, 128, 64, 144),
    "birch_leaves_fast": (32, 128, 48, 144),
    "bed1": (48, 128, 64, 144),
    "bed2": (64, 128, 80, 144),
    "melon_side": (80, 128, 96, 144),
    "melon_top": (96, 128, 112, 144),
    # Row 10
    "lapis_block": (0, 144, 16, 160),
    "green_wool" : (16, 144, 32, 160), 
    "lime_wool" : (32, 144,48 , 160),
    "glass_pane_top" : (64, 144, 80, 160),
    "bed3" : (80, 144, 96, 160),
    "bed4" : (96, 144, 112, 160),
    "bed5" : (112, 144, 128, 160),
    # Row 11
    "lapis_ore" : (0, 160, 16, 176),
    "brown_wool" : (16, 160, 32, 176),
    "yellow_wool" : (32, 160, 48, 176),
    "stonecutter_side" : (128, 160, 144, 176),
    "stonecutter_top" : (144, 160, 160, 176),
    # Row 12
    "sandstone_top" : (0, 176, 16, 192),
    "blue_wool" : (16, 176, 32, 192),
    "light_blue_wool" : (32, 176, 48, 192),
    # Row 13
    "sandstone" : (0, 192, 16, 208),
    "purple_wool" : (16, 192, 32, 208),
    "magenta_wool" : (32, 192, 48, 208),
    "quartz_block_top" : (64, 192, 80, 208),
    "quartz_pillar_top" : (80, 192, 96, 208),
    "chiseled_quartz_block_top" : (96, 192, 112, 208),
    "grass_block_top_tinted" : (192, 192, 208, 208),
    "water_1" : (208, 192, 224, 208),
    "water_2" : (224, 192, 240, 208),
    "water_3" : (240, 192, 256, 208),
    # Row 14
    "sandstone_bottom" : (0, 208, 16, 224),
    "cyan_wool" : (16, 208, 32, 224),
    "orange_wool" : (32, 208, 48, 224),
    "quartz_block_bottom" : (48, 208, 64, 224),
    "quartz_block_side" : (64, 208, 80, 224),
    "quartz_pillar" : (80, 208, 96, 224),
    "chiseled_quartz_block" : (96, 208, 112, 224),
    "glowing_obsidian" : (160, 208, 176, 224), 
    "spruce_leaves":(176, 208, 192, 224), 
    "spruce_leaves_fast":(192, 208, 208, 224), 
    "more_button":(208, 208, 224, 224), 
    "water_4":(224, 208, 240, 224), 
    "water_5":(240, 208, 256, 224), 
    # Row 15
    "nether_bricks":(0, 224, 16, 240), 
    "light_gray_wool":(16, 224, 32, 240), 
    "chiseled_sandstone":(64, 224, 80, 240), 
    "cut_sandstone":(80, 224, 96, 240), 
    "nether_reactor_2":(128, 224, 144, 240), 
    "nether_reactor_1":(144, 224, 160, 240),
    "nether_reactor_0":(160, 224, 176, 240),
    "dark_oak_leaves":(176, 224, 192, 240),
    "dark_oak_leaves_fast":(192, 224, 208, 240),
    "lava_1":(208, 224, 224, 240),
    "lava_2":(224, 224, 240, 240),
    "lava_3":(240, 224, 256, 240),
    # Row 16
    "break_0":(0, 240, 16, 256), 
    "break_1":(16, 240, 32, 256),
    "break_2":(32, 240, 48, 256),
    "break_3":(48, 240, 64, 256),
    "break_4":(64, 240, 80, 256),
    "break_5":(80, 240, 96, 256),
    "break_6":(96, 240, 112, 256),
    "break_7":(112, 240, 128, 256),
    "break_8":(128, 240, 144, 256),
    "break_9":(144, 240, 160, 256),
    "update":(192, 240, 208, 256), 
    "ateupd":(208, 240, 224, 256), 
    "lava_4":(224, 240, 240, 256), 
    "lava_5":(240, 240, 256, 256), 
}



if __name__ == "__main__":
    with Image.open(
        "/usr/lib/minecraft-pi-reborn-client/data/images/terrain.png"
    ) as img:
        region = img.crop(POSITIONS["nether_reactor_2"])
        region.show()
