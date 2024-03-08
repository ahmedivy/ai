def is_palindrome(s):
    return s.lower() == s[::-1].lower()


print(f'Dad is a palindrome: {is_palindrome("Dad")}')
print(f'aibohphobia is a palindrome: {is_palindrome("aibohphobia")}')
print(f'Bad is a palindrome: {is_palindrome("bad")}')
