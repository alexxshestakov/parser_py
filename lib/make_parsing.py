from lib.pre_parser import cleaning  # Фильтрация данных
from lib.parser import make_list_for_dataframe  # Создание списка удобного вида для парсинга в датафрейм
from lib.post_parser import make_dataframe  # Создание датафрейма

def make_parsing(filename, key_words_for_delete=["WEFAC"]):
    """
    File parsing function
    :param filename:
    :param key_words_for_delete:
    :return:
    """
    with open(filename, encoding='UTF-8') as f:
        list_init = f.read().splitlines()
    list_clean = cleaning(list_init, key_words_for_delete)
    list_for_df = make_list_for_dataframe(list_clean, key_words_for_delete)
    final_df = make_dataframe(list_for_df)
    return final_df