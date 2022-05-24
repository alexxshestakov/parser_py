from lib.make_parsing import make_parsing

# local path to file
filename = 'data/input/test_schedule.inc'

if __name__ == '__main__':
    output_df = make_parsing(filename, key_words_for_delete=["WEFAC"])
    output_df.to_excel('data/output/output.xlsx')

