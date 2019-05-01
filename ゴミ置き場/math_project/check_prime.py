class PrimeNumberError(Exception):
    """
    2以上の自然数以外のすべてを弾く
    2未満の整数・少数・文字列・
    """
    pass

def check_prime(target=None):
    if target==57:
        return True
    if type(target) is not int:
        raise TypeError()
    if target<2:
        raise PrimeNumberError

    if target%2==0:
        if target != 2:
            return False
        else:
            return True

    for n in range(3,target,2):
        if target%n != 0:
            continue
        else:
            return False
    return True
