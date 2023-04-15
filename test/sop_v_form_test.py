import pandas as pd
from utils.sop_v_form import sop_v_form

df = pd.read_csv('data/processed/osm_data.csv')

sop_v_form_dict = sop_v_form(df)

# test the function if the counter style_of_play is true
# based on prior knowledge of the data

def test_sop_v_form_0():
    """
    test data index 0:
    strength                : weak
    result                  : won
    opponent_style_of_play  : shoot on sight
    style_of_play           : shoot on sight
    opponent_formation      : 4-3-3 b
    formation               : 4-2-3-1

    expected sop_v_form_dict return:
    'shoot on sight' in sop_v_form_dict['4-3-3 b']['weak']
    """
    assert 'shoot on sight' in sop_v_form_dict['4-3-3 b']['weak']

def test_sop_v_form_1():
    """
    test data index 1:
    strength                : strong
    result                  : won
    opponent_style_of_play  : passing game
    style_of_play           : shoot on sight
    opponent_formation      : 4-2-3-1
    formation               : 4-2-3-1

    expected sop_v_form_dict return:
    'shoot on sight' in sop_v_form_dict['4-2-3-1']['strong']
    """
    assert 'shoot on sight' in sop_v_form_dict['4-2-3-1']['strong']


def test_sop_v_form_3():
    """
    test data index 3:
    strength                : equal
    result                  : won
    opponent_style_of_play  : passing game
    style_of_play           : counter-attack
    opponent_formation      : 4-2-3-1
    formation               : 6-3-1 b

    expected sop_v_form_dict return:
    'counter-attack' in sop_v_form_dict['4-2-3-1']['equal']
    """
    assert 'counter-attack' in sop_v_form_dict['4-2-3-1']['equal']

def test_sop_v_form_5():
    """
    test data index 5:
    strength                : strong
    result                  : won
    opponent_style_of_play  : wing play
    style_of_play           : wing play
    opponent_formation      : 4-4-2 b
    formation               : 4-3-3 b

    expected sop_v_form_dict return:
    'wing play' in sop_v_form_dict['4-4-2 b']['strong']
    """
    assert 'wing play' in sop_v_form_dict['4-4-2 b']['strong']

def test_sop_v_form_6():
    """
    test data index 6:
    strength                : strong
    result                  : won
    opponent_style_of_play  : long ball
    style_of_play           : wing play
    opponent_formation      : 3-3-4 a
    formation               : 4-3-3 b	

    expected sop_v_form_dict return:
    'wing play' in sop_v_form_dict['3-3-4 a']['strong']
    """
    assert 'wing play' in sop_v_form_dict['3-3-4 a']['strong']

def test_sop_v_form_9():
    """
    test data index 9:
    strength                : strong
    result                  : won
    opponent_style_of_play  : shoot on sight
    style_of_play           : passing game
    opponent_formation      : 3-3-2-2
    formation               : 4-4-2 b

    expected sop_v_form_dict return:
    'passing game' in sop_v_form_dict['3-3-2-2']['strong']
    """
    assert 'passing game' in sop_v_form_dict['3-3-2-2']['strong']

def test_sop_v_form_15():
    """
    test data index 15:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : shoot on sight
    style_of_play           : shoot on sight
    opponent_formation      : 4-3-3 b
    formation               : 4-5-1

    expected sop_v_form_dict return:
    'shoot on sight' in sop_v_form_dict['4-5-1']['strong']
    """
    assert 'shoot on sight' in sop_v_form_dict['4-5-1']['strong']

def test_sop_v_form_20():
    """
    test data index 20:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : wing play
    style_of_play           : shoot on sight
    opponent_formation      : 4-3-3 a
    formation               : 4-5-1

    expected sop_v_form_dict return:
    'wing play' in sop_v_form_dict['4-5-1']['strong']
    """
    assert 'wing play' in sop_v_form_dict['4-5-1']['strong']

def test_sop_v_form_27():
    """
    test data index 27:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : wing play
    style_of_play           : passing game
    opponent_formation      : 4-3-3 a
    formation               : 4-4-2 b

    expected sop_v_form_dict return:
    'wing play' in sop_v_form_dict['4-4-2 b']['strong']
    """
    assert 'wing play' in sop_v_form_dict['4-4-2 b']['strong']

def test_sop_v_form_87():
    """
    test data index 87:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : wing play
    style_of_play           : wing play
    opponent_formation      : 4-3-3 b
    formation               : 4-3-3 a

    expected sop_v_form_dict return:
    'wing play' in sop_v_form_dict['4-3-3 a']['strong']
    """
    assert 'wing play' in sop_v_form_dict['4-3-3 a']['strong']

def test_sop_v_form_104():
    """
    test data index 104:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : passing game
    style_of_play           : shoot on sight
    opponent_formation      : 4-3-3 a
    formation               : 4-5-1

    expected sop_v_form_dict return:
    'passing game' in sop_v_form_dict['4-5-1']['strong']
    """
    assert 'passing game' in sop_v_form_dict['4-5-1']['strong']

def test_sop_v_form_118():
    """
    test data index 118:
    strength                : weak
    result                  : lost
    opponent_style_of_play  : wing play
    style_of_play           : shoot on sight
    opponent_formation      : 4-3-3 b
    formation               : 4-5-1

    expected sop_v_form_dict return:
    'wing play' in sop_v_form_dict['4-5-1']['strong']
    """
    assert 'wing play' in sop_v_form_dict['4-5-1']['strong']
