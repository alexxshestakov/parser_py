import pytest
import pandas as pd
import numpy as np
from lib.pre_parser import cleaning
from lib.pre_parser import init_cleaning
from lib.parser import make_list_for_dataframe  # Создание списка удобного вида для парсинга в датафрейм
from lib.post_parser import make_dataframe  # Создание датафрейма



@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_pre_parser(filename):
    """
    Check correctness of replacing a number with * in data
    :param filename:
    :return:
    """
    with open(filename, encoding='UTF-8') as f:
        list_init = f.read().splitlines()
    test_list = [item for i in cleaning(list_init) for item in i]
    assert '1*' or '2*' not in test_list


def test_pre_parser2():
    """
    Check correctness of data cleansing
    :return:
    """
    input = ["'W3' 'LGR1' 10 10  2   2 	OPEN 	1* 	1	2 	1 	3* 			1.0918 /"]
    output = ['W3 LGR1 10 10 2 2 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 1.0918']
    assert init_cleaning(input) == output



@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_pre_parser3(filename):
    """
    Check the correct operation of the function with different key_words_for_delete
    :param filename:
    :return:
    """
    with open(filename, encoding='UTF-8') as f:
        list_init = f.read().splitlines()
    test_list_1 = [item for i in cleaning(list_init, key_words_for_delete=["WEFAC"]) for item in i]
    test_list_2 = [item for i in cleaning(list_init, key_words_for_delete=["WEFAC", 'COMPDAT']) for item in i]
    test_list_3 = [item for i in cleaning(list_init, key_words_for_delete=["WEFAC", 'COMPDAT', 'COMPDATL']) for
                   item in i]
    assert 'COMPDAT' and 'COMPDATL' in test_list_1 and 'WEFAC' not in test_list_1
    assert 'COMPDAT' and 'WEFAC' not in test_list_2 and 'COMPDATL' in test_list_2
    assert 'COMPDAT' and 'COMPDATL' and 'WEFAC' not in test_list_3


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_main_parser(filename):
    """
    Check are there np.nans in the data
    :param filename:
    :return:
    """
    with open(filename, encoding='UTF-8') as f:
        list_init = f.read().splitlines()
    list_after_main_parser = make_list_for_dataframe(cleaning(list_init))
    test_list = [item for i in list_after_main_parser for item in i]
    assert np.nan in test_list


@pytest.mark.parametrize('filename', [('input_data_test/test_schedule.inc')])
def test_post_parsing(filename):
    """
    Check type of data after function make_dataframe()
    :param filename:
    :return:
    """
    with open(filename, encoding='UTF-8') as f:
        list_init = f.read().splitlines()
    list_after_main_parser = make_list_for_dataframe(cleaning(list_init))
    data_frame = make_dataframe(list_after_main_parser)
    assert type(data_frame) == pd.core.frame.DataFrame


