HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    if pos < 10:
        return int(pos == 8)
    else:
        return num_eights(pos // 10) + int(pos % 10 == 8)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    if n <= 8:
        return n 
    else:
        return int(pingpong(n - 1) + helper(n - 1))

def helper(n):

    if n % 8 == 0 or num_eights(n):
        return int(helper(n - 1) * -1)
    elif n < 8:
        return 1
    else:
        return int(helper(n - 1))

# Alternate solution 1


def pingpong_next(x, i, step):
    if i == n:
        return x
    return pingpong_next(x + step, i + 1, next_dir(step, i + 1))


def next_dir(step, i):
    if i % 8 == 0 or num_eights(i) > 0:
        return -step
    return step

# Alternate solution 2


def pingpong_alt(n):
    if n <= 8:
        return n
    return direction(n) + pingpong_alt(n - 1)


def direction(n):
    if n < 8:
        return 1
    if (n - 1) % 8 == 0 or num_eights(n - 1) > 0:
        return -1 * direction(n - 1)
    return direction(n - 1)


def missing_digits(n):
    """Given a number a that is in sorted, non-decreasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    if n < 10:
        return 0
    elif n % 10 == n // 10 % 10:
        return missing_digits(n // 10)
    else:
        return missing_digits(n // 10) + n % 10 - n // 10 % 10 - 1
# Alternate solution


def missing_digits_alt(n):
    def helper(n, digit):
        if n == 0:
            return 0
        last, rest = n % 10, n // 10
        if last == digit or last + 1 == digit:
            return helper(rest, last)
        return 1 + helper(n, digit - 1)
    return helper(n // 10, n % 10)


def ascending_coin(coin):
    """Returns the next ascending coin in order.
    >>> ascending_coin(1)
    5
    >>> ascending_coin(5)
    10
    >>> ascending_coin(10)
    25
    >>> ascending_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def descending_coin(coin):
    """Returns the next descending coin in order.
    >>> descending_coin(25)
    10
    >>> descending_coin(10)
    5
    >>> descending_coin(5)
    1
    >>> descending_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    def plan(change, largest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if largest_coin == None:
            return 0
        without_coin = plan(change, descending_coin(largest_coin))
        with_coin = plan(change - largest_coin, largest_coin)
        return without_coin + with_coin    
    return plan(change, 25)

    # def plan(change, largest_coin):
    #     if change == 0:
    #         return 1
    #     if change < 0:
    #         return 0
    #     if largest_coin == None:
    #         return 0
    #     without_coin = plan(change, descending_coin(largest_coin))
    #     with_coin = plan(change - largest_coin, largest_coin)
    #     return without_coin + with_coin
    # return plan(change, 25)
    
    # def constrained_count_desc(change, largest_coin):
    #     if change == 0:
    #         return 1
    #     if change < 0:
    #         return 0
    #     if largest_coin == None:
    #         return 0
    #     without_coin = constrained_count_desc(change, descending_coin(largest_coin))
    #     with_coin = constrained_count_desc(change - largest_coin, largest_coin)
    #     return without_coin + with_coin
    # return constrained_count_desc(change, 25)






    # def constrained_count(change, smallest_coin):
    #     if change == 0:
    #         return 1
    #     if change < 0:
    #         return 0
    #     if smallest_coin == None:
    #         return 0
    #     without_coin = constrained_count(change, ascending_coin(smallest_coin))
    #     with_coin = constrained_count(change - smallest_coin, smallest_coin)
    #     return without_coin + with_coin
    # return constrained_count(change, 1)

    # Alternate solution: using descending_coin
    # def constrained_count_desc(change, largest_coin):
    #     if change == 0:
    #         return 1
    #     if change < 0:
    #         return 0
    #     if largest_coin == None:
    #         return 0
    #     without_coin = constrained_count(change, descending_coin(largest_coin))
    #     with_coin = constrained_count(change - largest_coin, largest_coin)
    #     return without_coin + with_coin
    # return constrained_count(change, 25)


def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    if n == 1:
        print_move(start, end)
    else:
        other = 6 - start - end
        move_stack(n - 1, start, other)
        print_move(start, end)
        move_stack(n - 1, other, end)


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))
    # Alternate solution:
       return (lambda f: f(f))(lambda f: lambda x: 1 if x == 0 else x * f(f)(x - 1))
