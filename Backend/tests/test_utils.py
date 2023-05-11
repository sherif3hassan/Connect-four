def bold(string):
    return f"\033[1m{string}\033[0m"


def red(string):
    return f"\033[91m{string}\033[0m"


def green(string):
    return f"\033[92m{string}\033[0m"


def ensure(func, args, value):
    output = func(*args)
    a = output == value

    if not a:
        prefix = ""
        # emoji = "\U0001F6D1"
        # prefix += f"{emoji} "
        prefix += f"{red(bold('FAILED'))}"
    else:
        prefix = ""
        # emoji = "\U00002705"
        # prefix += f"{emoji} "
        prefix += f"{green(bold('PASSED'))}"

    print(f"""{prefix} {func.__name__}({
        ', '.join(str(x) for x in args)
        }), Expected: {value}, Output: {output}""")


if __name__ == "__main__":
    ensure(max, [1, 2], 2)
    ensure(sum, [[1, 2]], 3)
