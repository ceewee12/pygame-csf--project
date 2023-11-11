import pytest
import pygame
from memorygame import *


@pytest.fixture
def setup():
    pygame.init()

def test_game_dimensions(setup):
    assert gameWidth == 840
    assert gameHeight == 640

def test_pic_size(setup):
    assert picSize == 128 

def test_columns_rows(setup):
    assert gameColumns == 5
    assert gameRows == 4

def test_padding(setup):
    assert padding == 10

def test_margins(setup):
    assert leftMargin == 75
    assert rightMargin == 75
    assert topMargin == 44
    assert bottomMargin == 44

def test_colors(setup):
    assert WHITE == (255, 255, 255)
    assert BLACK == (0, 0, 0)


def test_set_up_display():
    # Act 
    pygame.display.set_mode((gameWidth, gameHeight)) 
    pygame.display.set_caption('Memory Game')

    # Assert
    assert pygame.display.get_caption()[0] == 'Memory Game'

    assert pygame.display.get_surface().get_size() == (gameWidth, gameHeight)

def test_pygame_mixer():

  # Arrange
  mixer.init()
  mixer.music.load('bensound-summer_ogg_music.ogg')

  # Act
  mixer.music.play()
  sound = pygame.mixer.Sound('bensound-summer_ogg_music.ogg')
  sound.play()

  # Assert
  assert mixer.music.get_busy() 
  assert pygame.mixer.get_init()
  assert sound.get_length() > 0

  import pygame

def test_load_and_scale_image():

  # Arrange
  game_width = 840
  game_height = 640
  image_file = 'bground.png'

  # Act
  bg_image = pygame.image.load(image_file)
  scaled_bg = pygame.transform.scale(bg_image, (game_width, game_height))
  bg_rect = scaled_bg.get_rect()

  # Assert 
  assert bg_image.get_width() > 0
  assert bg_image.get_height() > 0
  assert scaled_bg.get_width() == game_width
  assert scaled_bg.get_height() == game_height
  assert bg_rect.width == game_width
  assert bg_rect.height == game_height


def test_load_and_shuffle_images():

    # Arrange
    image_dir = 'images'
    expected_num_images = 4

    
    # Act
    memory_pictures = []
    for item in os.listdir(image_dir):
        memory_pictures.append(item.split('.')[0])
    
    memory_pictures_copy = memory_pictures.copy()
    memory_pictures.extend(memory_pictures_copy)
    memory_pictures_copy.clear()
    
    random.shuffle(memory_pictures)
    
    # Assert
    assert len(memory_pictures) == expected_num_images * 5
    assert set(memory_pictures[:expected_num_images]) == set(memory_pictures[expected_num_images:])
    assert memory_pictures != sorted(memory_pictures)

import os
import pygame

def test_load_scale_images():

    # Arrange
    import os
import pygame

def test_load_scale_images():

    # Arrange
    image_files = ['image1.png', 'image2.png']
    pic_size = 128
    expected_num_images = len(image_files)
    
    # Act
    mem_pics = []
    mem_pics_rect = []
    
    for item in image_files:
        picture = pygame.image.load(f'images/{item}')
        scaled_pic = pygame.transform.scale(picture, (pic_size, pic_size))
        mem_pics.append(scaled_pic)
        
        pic_rect = scaled_pic.get_rect()
        mem_pics_rect.append(pic_rect)

    # Assert
    assert len(mem_pics) == expected_num_images
    assert len(mem_pics_rect) == expected_num_images
    
    for pic in mem_pics:
        assert pic.get_width() == pic_size
        assert pic.get_height() == pic_size
    # Act
    mem_pics = []
    mem_pics_rect = []
    
    for item in image_files:
        picture = pygame.image.load(f'images/{item}')
        scaled_pic = pygame.transform.scale(picture, (pic_size, pic_size))
        mem_pics.append(scaled_pic)
        
        pic_rect = scaled_pic.get_rect()
        mem_pics_rect.append(pic_rect)

    # Assert
    assert len(mem_pics) == expected_num_images
    assert len(mem_pics_rect) == expected_num_images
    
    for pic in mem_pics:
        assert pic.get_width() == pic_size
        assert pic.get_height() == pic_size

import pygame 

def test_position_and_hide_images():

    # Arrange
    mem_pics_rect = [pygame.Rect(0,0,100,100) for _ in range(8)] 
    game_columns = 5
    game_rows = 4
    left_margin = 50
    top_margin = 75
    pic_size = 128
    padding = 10

    # Act
    for i in range(len(mem_pics_rect)):
        mem_pics_rect[i][0] = left_margin + ((pic_size + padding) * (i % game_columns))
        mem_pics_rect[i][1] = top_margin + ((pic_size + padding) * (i % game_rows))

    hidden_images = [False] * len(mem_pics_rect)

    # Assert
    expected_x = [50, 160, 270, 380, 50, 160, 270, 380]
    expected_y = [75, 75, 75, 75, 185, 185, 185, 185]

    for i, rect in enumerate(mem_pics_rect):
        assert rect.x == expected_x[i] 
        assert rect.y == expected_y[i]
    
    assert hidden_images == [False] * len(mem_pics_rect)


