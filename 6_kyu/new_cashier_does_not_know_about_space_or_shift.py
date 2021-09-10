def get_order(order):
    menu = ('Burger', 'Fries', 'Chicken', 'Pizza',
            'Sandwich', 'Onionrings', 'Milkshake', 'Coke')
    lst, times = [], [order.count(i.lower()) for i in menu]
    for i, item in zip(times, menu):
        lst.extend([item] * i)
    return ' '.join(lst)