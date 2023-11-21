def count_letter_frequency_with_position(word_list):
    letter_frequency = {i: {} for i in range(6)}

    for word in word_list:
        for i, letter in enumerate(word):
            if letter not in letter_frequency[i]:
                letter_frequency[i][letter] = 1
            else:
                letter_frequency[i][letter] += 1

    return letter_frequency
