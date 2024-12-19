from gorgon import max_money

def test_gorgon_max_money():
    assert max_money(3, [100, 200, 300], 100) == 350
    assert max_money(4, [500, 500, 500, 500], 0) == 1000
    assert max_money(5, [10**9, 10**9, 10**9, 10**9, 10**9], 10**9) == 3500000000
    assert max_money(2, [1, 1], 1) == 2
    assert max_money(3, [100, 200, 300], 0) == 300