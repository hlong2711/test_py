def main():
    print("Hello from test!")
    if 3 > 2:
        print("five greater than two")

        data = {
            "a": 0,
            "b": [
                [1, 2],
            ],
        }

        print("data", data, type(data))

        val = ({"a": 1}, 1, 2)

        a, *b, c = val
        print("value: ", a, b, c)

        a["a"] = 2
        c = 3

        print("after change ", a, val, sep=" | ")

    x = 1  # int
    y = 2.8  # float
    z = 1j  # complex

    print(type(x))
    print(type(y))
    print(type(z))


if __name__ == "__main__":
    main()
