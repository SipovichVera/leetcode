def check_valid_parentheses_2(text, opening_parenthese, closing_parenthese):
    count_open_parentheses = len([char for char in text if char == opening_parenthese])
    count_close_parentheses = len([char for char in text if char == closing_parenthese])
    return count_open_parentheses, count_close_parentheses


def enter_text():
    return input("enter some text: ")


def main():
    text = enter_text()
    list_parentheses = ['()', '[]', '{}']
    for item in list_parentheses:
        count_open_parentheses, count_close_parentheses = check_valid_parentheses_2(text, item[0], item[1])
        print(item ,compare_count_parentheses(count_open_parentheses, count_close_parentheses))


def compare_count_parentheses(count_open_parentheses, count_close_parentheses):
    if count_open_parentheses == count_close_parentheses:
        return True
    return False


main()