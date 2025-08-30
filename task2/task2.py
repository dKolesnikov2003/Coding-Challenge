import sys
from fractions import Fraction


def coords_read(line):
    try:
        x, y = line.strip().split()
        return Fraction(x), Fraction(y)
    except (ValueError, ZeroDivisionError):
        print(f'Некорректная строка: "{line}"', file=sys.stderr)
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print('Указаны неверные параметры при запуске!', file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], encoding="utf-8") as f:
        cx, cy = coords_read(f.readline())
        a, b = coords_read(f.readline())
    a2, b2 = a * a, b * b

    with open(sys.argv[2], encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            x, y = coords_read(line)
            s = (x - cx)**2 / a2 + (y - cy)**2 / b2
            if s == 1:
                print(0)  # на окружности
            elif s < 1:
                print(1)  # внутри
            else:
                print(2)  # снаружи


if __name__ == "__main__":
    main()
