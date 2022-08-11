from typing import Optional


# Task 1
def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:  # todo check typing error
    if exp < 0:
        raise ValueError('This function works only with exp > 0')
    elif exp == 1:
        return x
    num = x * to_power(x, (exp - 1))
    return num


print(to_power(2, 4))


# Task 2
def is_palindrome(looking_str: str, index: int = 0) -> bool:  # version 1.0
    if index == 0:
        if len(looking_str) % 2 == 1:
            index_mid_l = len(looking_str) // 2 + 1
            print(index_mid_l)
        else:
            index_mid_l = (len(looking_str) / 2)
            print(index_mid_l)
    if index == index_mid_l:
        return True
    else:
        if looking_str[index] == looking_str[-(index + 1)]:
            index += 1
            is_palindrome(looking_str, index)


# is_palindrome('noon')


def is_palindrome1(word, index=0):  # version 1.1
    try:
        if word[index] == word[-(index + 1)]:
            index += 1
            is_palindrome1(word, index)
        else:
            return False
    except IndexError:
        return True

    return True


print(is_palindrome1('tenet'))
print(is_palindrome1('k'))
print(is_palindrome1('bob'))
print(is_palindrome1('keyboard'))
print(is_palindrome1('sassas'))


# Task 3
def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError('This function works only with positive integers')
    elif n == 0:
        return 0
    else:
        return a + mult(a, n - 1)


print(mult(2, 5))


# Task 4
def reverse(input_str: str) -> str:
    if len(input_str) <= 0:
        return input_str
    if len(input_str) == 1:
        return input_str
    if len(input_str) == 2:
        lst_input_str: list = list(input_str)
        lst_input_str[0], lst_input_str[1] = lst_input_str[1], lst_input_str[0]
        return ''.join(lst_input_str)
    else:
        return input_str[-1] + reverse(input_str[:-1])


print(reverse('hello'))


# Task 5
def sum_of_digits(digit_string: str) -> int:
    if len(digit_string) <= 0:
        return digit_string
    if len(digit_string) == 1:
        return int(digit_string)
    else:
        try:
            return int(digit_string[0]) + sum_of_digits(digit_string[1:])
        except ValueError:
            print('input string must be digit string')


print(sum_of_digits('123'))
print(sum_of_digits('t45n'))
