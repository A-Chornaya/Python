'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''


def isValid(s: str) -> bool:
    s_new = s
    while True:
        ss = s_new.find('()')
        if ss == -1:
            ss = s_new.find('{}')
            if ss == -1:
                ss = s_new.find('[]')
        if ss != -1:
            s_new = s_new[:ss] + s_new[ss + 2:]
        else:
            break

    return True if not s_new else False


print(isValid('()'))            # True
print(isValid('()[]{}'))        # True
print(isValid('(]'))            # False
print(isValid('([)]'))          # False
print(isValid('{[]}'))          # True
