def merge_sort(words):
    if len(words) <= 1:
        return words

    mid = len(words) // 2
    left = merge_sort(words[:mid])
    right = merge_sort(words[mid:])

    return merge(left, right, words)


def merge(left_word: list, right_word, merged):
    char_left_list = list(left_word)
    char_right_list = list(right_word)
    merged_list = list(merged)
    left_word_idx, right_word_idx = 0, 0

    while left_word_idx < len(char_left_list) and right_word_idx < len(
        char_right_list
    ):
        if ord(char_left_list[left_word_idx]) <= ord(
            char_right_list[right_word_idx]
        ):
            merged_list[left_word_idx + right_word_idx] = char_left_list[
                left_word_idx
            ]
            left_word_idx += 1
        else:
            merged_list[left_word_idx + right_word_idx] = char_right_list[
                right_word_idx
            ]
            right_word_idx += 1

    for left_word_idx in range(left_word_idx, len(char_left_list)):
        merged_list[left_word_idx + right_word_idx] = char_left_list[
            left_word_idx
        ]

    for right_word_idx in range(right_word_idx, len(char_right_list)):
        merged_list[left_word_idx + right_word_idx] = right_word[
            right_word_idx
        ]

    return merged_list


def is_anagram(first_string, second_string):
    string_lower1 = first_string.lower()
    string_lower2 = second_string.lower()

    sort_merge1 = merge_sort(string_lower1)
    sort_merge2 = merge_sort(string_lower2)

    join_sort1 = "".join(sort_merge1)
    join_sort2 = "".join(sort_merge2)

    if len(sort_merge1) == 0 or len(sort_merge2) == 0:
        return (join_sort1, join_sort2, False)

    if join_sort1 == join_sort2:
        return (join_sort1, join_sort2, True)

    return (join_sort1, join_sort2, False)
