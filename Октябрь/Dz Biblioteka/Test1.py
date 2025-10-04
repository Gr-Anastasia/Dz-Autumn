from Library import Library

def test_add(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    assert lib + other == result, f"{lib.get_count()} + {other} = {result}"

def test_radd(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    assert other + lib == result, f"{lib.get_count()} + {result} = {other}"

def test_sub(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    assert lib - other == result, f"{other} + {lib.get_count()} = {result}"

def test_rsub(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    assert other - lib == result, f"{other} - {lib.get_count()} = {result}"

def test_iadd(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    lib += other
    libs_count = lib.get_count()
    assert libs_count  == result, f"{count} + {other} = {lib.get_count()}"

def test_isub(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    lib -= other
    libs_count = lib.get_count()
    assert libs_count == result, f"{count} - {other} = {lib.get_count()}"

def test_lt(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    comparison = lib < other
    assert comparison == result, f"{lib.get_count()} < {other} = {result}"

def test_gt(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    comparison = lib > other
    assert comparison == result, f"{lib.get_count()} > {other} = {result}"

def test_le(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    comparison = lib <= other
    assert comparison == result, f"{lib.get_count()} <= {other} = {result}"

def test_ge(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    comparison = lib >= other
    assert comparison == result, f"{lib.get_count()} >= {other} = {result}"

def test_eg(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    comparison = lib == other
    assert comparison == result, f"{lib.get_count()} == {other} = {result}"

def test_ne(count, other, result):
    lib = Library(name="Ноябрьская",
              address="г. Уфа, проспект Октября 85",
                  count=count)
    comparison = lib != other
    assert comparison == result, f"{lib.get_count()} != {other} = {result}"

test_add(2, 2, 4)
test_radd(5, 3, 8)
test_sub(6,4, 2)
test_rsub(5, 6, 1)
test_iadd(10, 2, 12)
test_isub(10, 2, 8)
test_lt(5, 10, True)
test_gt(12, 10, True)
test_le(5, 5, True)
test_ge(8, 8, True)
test_eg(6, 6, True)
test_ne(9, 6, True)
