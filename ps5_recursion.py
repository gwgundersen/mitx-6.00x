# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if aStr == "":
        return aStr
    else:
        return reverseString(aStr[1:]) + aStr[0]


#
# Problem 4: Erician
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """

    if x == '':
        return True
    elif word == '':
        return False
    elif x[0] == word[0]:
        return x_ian(x[1:], word[1:])
    else:
        return x_ian(x, word[1:])

#
# Problem 5: Typewriter
#
lineLength = 15
text = 'While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.'

def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    L = lineLength

    if len(text) <= L or text.find(' ') == -1:
        return text
    elif text[L-1] == ' ':
        return text[:L] + "\n" + insertNewlines(text[L:], L)
    else:
        if text[L:].find(' ') == -1:
            return text[:L+1] + "\n" + insertNewlines(text[L+text[L:].find(' ')+1:], L)
        else:
            return text[:L+text[L:].find(' ')+1] + "\n" + insertNewlines(text[L+text[L:].find(' ')+1:], L)












    
