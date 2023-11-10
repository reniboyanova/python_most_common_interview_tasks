# 4. Write a function. For a given sentence, return the average word length.
# Note: Remember to remove punctuation first.

# sentence1 = "Hi all, my name is Tom...I am originally from Australia."
# sentence2 = "I need to work very hard to learn more about algorithms in Python!"

#1 variant
def average_word_length(sentence):
    signs = ",-!?'@&()[]{}:"
    new_sentence = ''
    for letter in sentence:
        if letter in signs:
            continue
        elif letter in '...':
            new_sentence += ' '
            continue
        new_sentence += letter
        # print(letter)
    new_sentence = new_sentence.split()
    average_word_len = sum(len(word) for word in new_sentence) / len(new_sentence)
    print(f"Average len of word in this sentence:\n'{sentence}'\nis: {average_word_len:.2f}")


# 2 variant: 
def average_word_length_2(sentence):
    signs = ".,-!?'@&()[]{}:"
    new_sentence = ''
    for letter in sentence:
        if letter in signs:
            continue
        new_sentence += letter
    new_sentence = new_sentence.split()
    average_word_len = sum(len(word) for word in new_sentence) / len(new_sentence)
    print(f"Average len of word in this sentence:\n'{sentence}'\nis: {average_word_len:.2f}")


if __name__ == "__main__":
    average_word_length("Hi all, my name is Tom...I am originally from Australia.")
    average_word_length_2("Hi all, my name is Tom...I am originally from Australia.")

