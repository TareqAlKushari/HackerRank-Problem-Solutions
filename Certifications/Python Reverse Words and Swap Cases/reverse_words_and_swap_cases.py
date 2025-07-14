"""
1. Python: Reverse Words and Swap Cases

Implement a function that takes a string consisting of words separated by single spaces and returns a string containing all those words but in the reverse order and such that all cases of letters in the original string are swapped, 
i.e. lowercase letters become uppercase and uppercase letters become lowercase.

Example
    sentence = "rUns dog"

Reverse the word order and swap the case of all letters, then return the string "DoG RUNS".

Function description
Complete the function reverse_words_order_and_swap_cases in the editor below.
The function has the following parameter(s):
    string sentence: a given string of space-separated words

Returns:
    string: a string containing all the words from the sentence but in the reverse order and such that all cases of letters in the sentence string are swapped.

Constraints
    sentence contains only English letters and spaces.
    sentence begins and ends with a letter.
    There are no two consecutive spaces in sentence.
    There are at most 10 words in sentence.
    The lengths of each of the words is at most 10.

Input Format Format for Custom Testing
Input from stdin will be processed as follows and passed to the function.

The first and only line contains the string, sentence, that will be passed to the function.

Sample Case 0
Sample Input
STDIN                                       Function
aWESOME is cODING "aWESOME is CODING" → sentence =

Sample Output
Coding IS Awesome

Explanation
sentence = "aWESOME is CODING"
Reverse the word order: "CODING IS AWESOME"
Swap the case: "Coding IS Awesome"
"""


def reverse_words_order_and_swap_cases(sentence):
    # Step 1: Swap the case of each character
    swapped = sentence.swapcase()
    
    # Step 2: Split the sentence into words, reverse them, and join back into a string
    reversed_words = swapped.split()[::-1]
    
    # Step 3: Join the reversed list into a string with single spaces
    result = ' '.join(reversed_words)
    
    return result


if __name__ == "__main__":
    print(reverse_words_order_and_swap_cases("aWESOME is CODING"))