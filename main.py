from stats import get_book_text, words_counter, symbols_counter, chars_dict_to_sorted_list
import sys

if len(sys.argv) >= 2:
    path = sys.argv[1]
else:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
str_text_file = get_book_text(path)
w_count = words_counter(str_text_file)
s_count = symbols_counter(str_text_file)
sort_counts_symbols = chars_dict_to_sorted_list(s_count)


def print_report(path_to_file: str, words_count: int, sort_sym_count: list[tuple[str, int]]) -> str:
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path_to_file}...')
    print('----------- Word Count ----------')
    print(f'Found {words_count} total words')
    print('--------- Character Count -------')
    for i in sort_sym_count:
        if i[0].isalpha():
            print(f'{i[0]}: {i[1]}')
    print('============= END ===============')

def main():
    print_report(path, w_count, sort_counts_symbols)

main()