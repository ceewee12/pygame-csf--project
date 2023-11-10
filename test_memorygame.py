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
    assert leftMargin == 190
    assert rightMargin == 190
    assert topMargin == 156
    assert bottomMargin == 156

def test_colors(setup):
    assert WHITE == (255, 255, 255)
    assert BLACK == (0, 0, 0)

def test_selections_initialized(setup):
    assert selection1 == None 
    assert selection2 == None

