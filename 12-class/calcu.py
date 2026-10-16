class Cal:
    def plus(s, x, y):
        return x + y

    def minus(s, x, y):
        return x - y

    def multi(s, x, y):
        return x * y

    def divide(s, x, y):
        return x / y


if __name__ == "__main__":
    c = Cal()
    print(c.plus(1, 2))