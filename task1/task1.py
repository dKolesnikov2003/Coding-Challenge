import sys


def fatal_log():
    print('Указаны неверные параметры при запуске!', file=sys.stderr)
    sys.exit(1)


def args_parse(args):
    if len(args) != 5:
        fatal_log()

    try:
        params = [int(x) for x in args[1:]]
    except ValueError:
        fatal_log()
    for p in params:
        if p < 2: fatal_log()

    return params


def path_gen(n, m):
    path = [1]
    while (i := (path[-1] + (m - 1)) % n) != 1:
        path.append(i)
    return ''.join(list(map(str, path))).replace('0', str(n))


if __name__ == '__main__':
    p = args_parse(sys.argv)
    print(path_gen(p[0], p[1]) + path_gen(p[2], p[3]))
