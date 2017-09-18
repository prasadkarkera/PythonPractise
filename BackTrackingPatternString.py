# http://www.geeksforgeeks.org/match-a-pattern-and-string-without-using-regular-expressions/


def pattern_match_util(input_str: str, input_index: int,
                       pattern: str, pattern_index: int,
                       pattern_str_map: dict):
    input_length = len(input_str)
    pattern_length = len(pattern)
    if input_index == input_length and pattern_index == pattern_length:
        return True

    if input_index == input_length or pattern_index == pattern_length:
        return False

    # read next character from the pattern
    pattern_character = pattern[pattern_index]

    # if pattern exists in pattern_str_map
    if pattern_str_map.get(pattern_character):

        matched_str = pattern_str_map[pattern_character]
        matched_str_length = len(matched_str)

        if matched_str != input_str[input_index: input_index + matched_str_length]:
            return False

        return pattern_match_util(input_str, input_index + matched_str_length,
                                  pattern, pattern_index + 1, pattern_str_map)

    # for characters not seen try out all remaining characters in the pattern

    for length in range(1, input_length - input_index):

        pattern_str_map[pattern_character] = input_str[input_index: input_index + length]

        if pattern_match_util(input_str, input_index + length,
                              pattern, pattern_index + 1, pattern_str_map):
            return True

        pattern_str_map.pop(pattern_character)

    return False


def pattern_match(input_string, pattern):
    if len(input_string) < len(pattern):
        return False

    pattern_str_map = {}
    is_success = pattern_match_util(input_string, 0, pattern, 0, pattern_str_map)

    for key, value in pattern_str_map.items():
        print(f'{key}->{value}')

    return is_success


def main():
    input_str = 'GeeksForGeeks'
    pattern = 'gfg'

    if pattern_match(input_str, pattern):
        print('Solution Found')
    else:
        print('No Solution Found')


if __name__ == '__main__':
    main()
