A = input()

def is_palindrome(txt):
    if txt == txt[::-1]:
        return "Yes"
    return "No"

print(is_palindrome(A))