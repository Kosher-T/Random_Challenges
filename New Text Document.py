def sum_of_digits(num: int) -> int:
    '''
    Calculate the sum of the digits of a given integer.
    '''
    # Write code here
    return sum(int(digit) for digit in str(num))