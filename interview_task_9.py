# 9. Write a Python function that takes a list of words and return the longest word and the length of the longest one.

# Input: ["Python", "Exercises", "Great"]
# Output:
# Longest word:  Exercises
# Length of the longest word:  9

def longest_word_and_its_len_return(list_of_words: list):
    if not isinstance(list_of_words, list):
        raise TypeError("Invalid input type!")

    if not all(isinstance(word, str) for word in list_of_words):
        raise TypeError("Values ust be string")

    longest_word = max(list_of_words, key=len)
    return f"Longest word: {longest_word}\nLength of the longest word: {len(longest_word)}"



if __name__ == "__main__":
    print(longest_word_and_its_len_return(["Python", "Exercises", "Great"]))