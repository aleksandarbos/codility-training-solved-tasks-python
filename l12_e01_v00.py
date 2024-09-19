def gdc_sub(a, b):
    if a == b:
        return a
    elif a > b:
        return gdc_sub(a-b, b)
    else:
        return gdc_sub(a, b-a)


def gdc_mod(a, b):
    if not a >= b:
        raise Exception(
            f'Parameter a, needs to be greater than or equal to b.')
    if a % b == 0:
        return b
    else:
        return gdc_mod(b, a % b)


def gdc_bin(a, b, res=1):
    if a == b:
        return a * res
    elif a % 2 == 0 and b % 2 == 0:
        return gdc_bin(a // 2, b // 2, res*2)
    elif a % 2 == 0:
        return gdc_bin(a // 2, b, res)
    elif b % 2 == 0:
        return gdc_bin(a, b // 2, res)
    elif a > b:
        return gdc_bin(a-b, b, res)
    else:
        return gdc_bin(a, b-a, res)


if __name__ == "__main__":
    assert gdc_sub(24, 10) == 2
    assert gdc_sub(12, 15) == 3
    import pdb
    pdb.set_trace()
    assert gdc_bin(12, 15) == 3
