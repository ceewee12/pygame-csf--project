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