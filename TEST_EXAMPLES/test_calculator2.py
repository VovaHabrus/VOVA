def calculator(expression):
    allowed = '+-*/'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Має бути хоча б 1 знак ({allowed})')


if __name__ == '__main__':
    print(calculator('-32131'))
