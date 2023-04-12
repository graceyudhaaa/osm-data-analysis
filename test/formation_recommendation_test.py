import pandas as pd
import sys
sys.path.append("..") # resolve annoying import error from pytest

from utils.formation_recommendation import formation_recommendation

df = pd.read_csv('data/processed/osm_data.csv')

formation_dict = formation_recommendation(df)

# test the function if the counter formation is true
# based on prior knowledge of the data

def test_formation_recommendation_0():
    """
    test data index 0:
    strength            : weak
    result              : won
    opponent_formation  : 4-3-3 b
    formation           : 4-2-3-1

    expected formation_dict return:
    '4-2-3-1' in formation_dict['4-3-3 b']['weak']
    """
    assert '4-2-3-1' in formation_dict['4-3-3 b']['weak']

def test_formation_recommendation_1():
    """
    test data index 1:
    strength            : strong
    result              : won
    opponent_formation  : 4-2-3-1
    formation           : 4-2-3-1

    expected formation_dict return:
    '4-2-3-1' in formation_dict['4-2-3-1']['strong']
    """
    assert '4-2-3-1' in formation_dict['4-2-3-1']['strong']

def test_formation_recommendation_2():
    """
    test data index 2:
    strength            : weak
    result              : won
    opponent_formation  : 4-4-2 b
    formation           : 4-2-3-1

    expected formation_dict return:
    '4-2-3-1' in formation_dict['4-4-2 b']['weak']
    """
    assert '4-2-3-1' in formation_dict['4-4-2 b']['weak']

def test_formation_recommendation_3():
    """
    test data index 3:
    strength            : equal
    result              : won
    opponent_formation  : 4-2-3-1
    formation           : 6-3-1 b

    expected formation_dict return:
    '6-3-1 b' in formation_dict['4-2-3-1']['equal']
    """
    assert '6-3-1 b' in formation_dict['4-2-3-1']['equal']

def test_formation_recommendation_15():
    """
    test data index 15:
    strength            : weak
    result              : lost
    opponent_formation  : 4-3-3 b
    formation           : 4-5-1

    expected formation_dict return:
    '4-3-3 b' in formation_dict['4-5-1']['strong']
    """
    assert '4-3-3 b' in formation_dict['4-5-1']['strong']

def test_formation_recommendation_24():
    """
    test data index 24:
    strength            : weak
    result              : lost
    opponent_formation  : 4-4-2 b
    formation           : 4-2-3-1

    expected formation_dict return:
    '4-4-2 b' in formation_dict['4-2-3-1']['strong']
    """
    assert '4-4-2 b' in formation_dict['4-2-3-1']['strong']

def test_formation_recommendation_27():
    """
    test data index 27:
    strength            : weak
    result              : lost
    opponent_formation  : 4-3-3 a
    formation           : 4-4-2 b

    expected formation_dict return:
    '4-3-3 a' in formation_dict['4-4-2 b']['strong']
    """
    assert '4-3-3 a' in formation_dict['4-4-2 b']['strong']

def test_formation_recommendation_31():
    """
    test data index 31:
    strength            : weak
    result              : lost
    opponent_formation  : 4-2-3-1
    formation           : 4-5-1

    expected formation_dict return:
    '4-2-3-1' in formation_dict['4-5-1']['strong']
    """
    assert '4-2-3-1' in formation_dict['4-5-1']['strong']

def test_formation_recommendation_87():
    """
    test data index 87:
    strength            : weak
    result              : lost
    opponent_formation  : 4-3-3 b
    formation           : 4-3-3 a

    expected formation_dict return:
    '4-3-3 b' in formation_dict['4-3-3 a']['strong']
    """
    assert '4-3-3 b' in formation_dict['4-3-3 a']['strong']
