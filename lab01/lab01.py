def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        f = 1
    else:
        m = n
        f = m
        while n > m-k+1 :
            n -= 1
            f = f * n
    return f



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    s = str(y)
    sd = 0
    for i in range(len(s)):
    	sd += int(s[i])
    return sd



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    for i in range(len(str(n))):
    	if int(str(n)[i]) == 8 and i != len(str(n))-1 and int(str(n)[i+1]) == 8:
    		m = True
    		break
    	else:
    		m = False
    return m



