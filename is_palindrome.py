# def is_palindrome(word):
#     """Return True if word is a palindrome, False if not."""
#     return word == word[::-1]
#solution steps #Racecar #racecar
#move through the list
#compare the present item to the last item, stop result in a container


from sysconfig import is_python_build


def is_palindrome(word:str)->bool:    
    if len(word) <= 1:
        return True
    
    else:
        return word[0] == word[-1] and is_palindrome(word[1,-1])