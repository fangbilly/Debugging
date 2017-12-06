def main():
    # print(one())


def one():
    print('one!')
    return 1 + two()

def two():
    print('two!')
    return 1

def three():
    print('three!', two(), one())

main()
