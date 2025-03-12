def get_sentence_input() -> str:
    """
    Prompts the user to enter a sentence and returns the input string.
    
    Returns:
        str: The sentence entered by the user.
    """
    sentence = input("Enter a sentence: ")
    return sentence

def count_words(sentence: str) -> int:
    """
    Counts the number of words in the given sentence.
    
    Args:
        sentence (str): The sentence to count words in.
    
    Returns:
        int: The number of words in the sentence.
    """
    # Use the split method to break the sentence into words and count the words
    words = sentence.split()  # split() will handle multiple spaces as well
    return len(words)

def main():
    """
    Main function to execute the program.
    """
    # Get the user's sentence
    sentence = get_sentence_input()
    
    # Count the words in the sentence
    word_count = count_words(sentence)
    
    # Display the result
    print(f"The sentence has {word_count} words.")

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()