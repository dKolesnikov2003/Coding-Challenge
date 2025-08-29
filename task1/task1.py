import sys


def fatalLog():
    print('Указаны неверные парметры при запуске!', file=sys.stderr)
    sys.exit(1)


def argsParse(args):
    if len(args) != 5:
        fatalLog()

    try:
        params = [int(x) for x in args[1:]]
    except ValueError:
        fatalLog()
    for p in params:
        if p < 2: fatalLog()

    return params


def pathGen(n, m):
    path = [1]
    while (i := (path[-1] + (m - 1)) % n) != 1:
        path.append(i)
    return ''.join(list(map(str, path))).replace('0', str(n))


if __name__ == '__main__':
    p = argsParse(sys.argv)
    print(pathGen(p[0], p[1]) + pathGen(p[2], p[3]))
