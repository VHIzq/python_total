def no_repeat(word):
    single_char = list(set(word))
    sorting_chars = sorted(single_char)
    print(sorting_chars)


no_repeat('ferrocarril')
