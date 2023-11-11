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


def test_prepare_game_assets():
    # Load memoryPictures from images folder
    memoryPictures = []
    for item in os.listdir('images'):
        memoryPictures.append(item.split('.')[0])

    # Create a copy of memoryPictures and extend it with itself
    memoryPicturesCopy = memoryPictures.copy()
    memoryPictures.extend(memoryPicturesCopy)
    memoryPicturesCopy.clear()

    # Shuffle the memoryPictures list
    random.shuffle(memoryPictures)

    # Load images and prepare game assets
    memPics = []
    memPicsRect = []
    hiddenImages = []

    for item in memoryPictures:
        picture = pygame.image.load(f'images/{item}.png')
        picture = pygame.transform.scale(picture, (picSize, picSize))
        memPics.append(picture)
    for i in range(len(memPicsRect)):
        pictureRect = picture.get_rect()
        pictureRect.left = leftMargin + ((picSize + padding) * (i % gameColumns))
        pictureRect.top = topMargin + ((picSize + padding) * (i % gameRows))
        memPicsRect.append(pictureRect)

        hiddenImages.append(False)

    # Verify the length of memoryPictures
    assert len(memoryPictures) == 20

    # Verify the length of memPics, memPicsRect, and hiddenImages
    assert len(memPics) == 20
    # Verify the positions of memPicsRect
    for i, pictureRect in enumerate(memPicsRect):
        assert pictureRect.left == leftMargin + ((picSize + padding) * (i % gameColumns))
        assert pictureRect.top == topMargin + ((picSize + padding) * (i % gameRows))

