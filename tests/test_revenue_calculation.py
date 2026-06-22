def calculate_revenue(quantity, unit_price):
    return quantity * unit_price


def test_revenue_calculation():
    assert calculate_revenue(2, 100) == 200
    assert calculate_revenue(1, 75) == 75
    assert calculate_revenue(4, 80) == 320


def test_revenue_with_decimal_price():
    assert calculate_revenue(2, 25.50) == 51.00
