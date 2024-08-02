from ..cli import welcome_user


def greeting():
    print('Welcome to the Brain Games!')
    welcome_user()


def main():
    greeting()


if __name__ == '__main__':
    main()
