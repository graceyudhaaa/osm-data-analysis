import pandas as pd
from utils.style_of_play_recommendation import style_of_play_recommendation

df = pd.read_csv('data/processed/osm_data.csv')

style_of_play_dict = style_of_play_recommendation(df)

# test the function if the counter style_of_play is true
# based on prior knowledge of the data

def test_style_of_play_recommendation_0():
    """
    test data index 0:
    strength                : weak
    result                  : won
    opponent_style_of_play  : shoot on sight
    style_of_play           : shoot on sight

    expected style_of_play_dict return:
    'shoot on sight' in style_of_play_dict['shoot on sight']['weak']
    """
    assert 'shoot on sight' in style_of_play_dict['shoot on sight']['weak']

def test_style_of_play_recommendation_1():
    """
    test data index 1:
    strength                : strong
    result                  : won
    opponent_style_of_play  : passing game
    style_of_play           : shoot on sight

    expected style_of_play_dict return:
    'shoot on sight' in style_of_play_dict['passing game']['strong']
    """
    assert 'shoot on sight' in style_of_play_dict['passing game']['strong']


def test_style_of_play_recommendation_3():
    """
    test data index 3:
    strength                : equal
    result                  : won
    opponent_style_of_play  : passing game
    style_of_play           : counter-attack

    expected style_of_play_dict return:
    'counter-attack' in style_of_play_dict['passing game']['equal']
    """
    assert 'counter-attack' in style_of_play_dict['passing game']['equal']

def test_style_of_play_recommendation_5():
    """
    test data index 5:
    strength                : strong
    result                  : won
    opponent_style_of_play  : wing play
    style_of_play           : wing play

    expected style_of_play_dict return:
    'wing play' in style_of_play_dict['wing play']['strong']
    """
    assert 'wing play' in style_of_play_dict['wing play']['strong']

def test_style_of_play_recommendation_6():
    """
    test data index 6:
    strength                : strong
    result                  : won
    opponent_style_of_play  : long ball
    style_of_play           : wing play

    expected style_of_play_dict return:
    'wing play' in style_of_play_dict['long ball']['strong']
    """
    assert 'wing play' in style_of_play_dict['long ball']['strong']

def test_style_of_play_recommendation_9():
    """
    test data index 9:
    strength                : strong
    result                  : won
    opponent_style_of_play  : shoot on sight
    style_of_play           : passing game

    expected style_of_play_dict return:
    'passing game' in style_of_play_dict['shoot on sight']['strong']
    """
    assert 'passing game' in style_of_play_dict['shoot on sight']['strong']

def test_style_of_play_recommendation_15():
    """
    test data index 15:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : shoot on sight
    style_of_play           : shoot on sight

    expected style_of_play_dict return:
    'shoot on sight' in style_of_play_dict['shoot on sight']['strong']
    """
    assert 'shoot on sight' in style_of_play_dict['shoot on sight']['strong']

def test_style_of_play_recommendation_20():
    """
    test data index 20:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : wing play
    style_of_play           : shoot on sight

    expected style_of_play_dict return:
    'wing play' in style_of_play_dict['shoot on sight']['strong']
    """
    assert 'wing play' in style_of_play_dict['shoot on sight']['strong']

def test_style_of_play_recommendation_27():
    """
    test data index 27:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : wing play
    style_of_play           : passing game

    expected style_of_play_dict return:
    'wing play' in style_of_play_dict['passing game']['strong']
    """
    assert 'wing play' in style_of_play_dict['passing game']['strong']

def test_style_of_play_recommendation_87():
    """
    test data index 87:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : wing play
    style_of_play           : wing play

    expected style_of_play_dict return:
    'wing play' in style_of_play_dict['wing play']['strong']
    """
    assert 'wing play' in style_of_play_dict['wing play']['strong']

def test_style_of_play_recommendation_104():
    """
    test data index 104:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : passing game
    style_of_play           : shoot on sight

    expected style_of_play_dict return:
    'passing game' in style_of_play_dict['shoot on sight']['strong']
    """
    assert 'passing game' in style_of_play_dict['shoot on sight']['strong']

def test_style_of_play_recommendation_118():
    """
    test data index 118:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : wing play
    style_of_play           : shoot on sight

    expected style_of_play_dict return:
    'wing play' in style_of_play_dict['shoot on sight']['strong']
    """
    assert 'wing play' in style_of_play_dict['shoot on sight']['strong']
