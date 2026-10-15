def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def words_counter(file_contents: str) -> int:
    return len(file_contents.split())

def symbols_counter(file_contents: str) -> dict[str, int]:
    sym_count = {}
    for symbol in file_contents:
        sym = symbol.lower()
        if sym in sym_count:
            sym_count[sym] += 1
        else:
            sym_count[sym] = 1
    return sym_count

def sort_on(sort_tuple: tuple[str, int]) -> int:
    return sort_tuple[1]

def chars_dict_to_sorted_list(sym_count: dict[str, int]) -> list[tuple[str, int]]:
    result = []
    for dict_key in sym_count:
        result.append((dict_key, sym_count[dict_key]))
    return sorted(result, reverse=True, key=sort_on)