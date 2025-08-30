import sys


def fatal_log():
    print('Указаны неверные параметры при запуске!', file=sys.stderr)
    sys.exit(1)


def nums_read(path):
    nums = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            nums.append(int(line))
    return nums


def main():
    try:
        nums = nums_read(sys.argv[1])
    except:
        fatal_log()

    if len(nums) < 2:
        return 0

    median = sorted(nums)[(len(nums) - 1) // 2]
    if (sum(abs(n - median) for n in nums)) <= 20:
        return sum(abs(n - median) for n in nums)
    return '20 ходов недостаточно для приведения всех элементов массива к одному числу'


if __name__ == '__main__':
    print(main())
