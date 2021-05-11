# How can a given string be reversed using recursion?
# Example: "abcdefg" ==> "gfedcba"

def reverse_str(s):
    return reverse_str(s[1:]) + s[0] if len(s) > 0 else s

# alternatively, using list reverse loop [start:end:-1]
def reverse_str_as_list(s):
    return s[::-1]

s = 'abcdefg'
print('input string: \t', s)
print('reversed string:', reverse_str(s))
print('reversed string:', reverse_str_as_list(s))
