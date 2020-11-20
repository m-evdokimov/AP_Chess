def main():
    while 1:
        try:
            k, l, m, n = map(int, input('Input k, l, m, n with space: ').strip().split())
            if not ((1 <= k <= 8 and 1 <= l <= 8 and 1 <= m <= 8 and 1 <= n <= 8)) or (k == m and l == n):
                raise KeyError
            else:
                break
        except ValueError:
            print('Input error, try again...')
        except KeyError:
            print('Some of the coordinates are not in [1, 8] or you entered the same square coordinates')


    #task a:
    if (k + l) % 2 == (m + n) % 2:
        print('a) The Same square color')
    else:
        print('a) Not the same square color')

    #task b:
    if k == m or l == m or abs(k - l) == abs(m - n):
        print('b) The queen may capture these square')
    else:
        print('b) The queen may not capture these square')

    #task c:
    if abs(k - m) + abs(l - n) == 3:
        print('c) The knight may capture these square')
    else:
        print('c) The knight may not capture these square')

    #task d:
    if k == m or l == n:
        print('d) The rook may move to these square by 1 move')
    else:
        print(f'd) Move the rook to ({k}, {l}) to ({m}, {l}) and then to ({m}, {n})')

    #task e
    if k == m or l == m or abs(k - l) == abs(m - n):
        print('e) The queen may move to these square by 1 move')
    else:
        print(f'e) Move the queen to ({k}, {l}) to ({m}, {l}) and then to ({m}, {n})')

    #taks f
    if abs(k - m)  == abs(l - n):
        print('f) The bishop may move to these square by 1 move')
    elif (k + l) % 2 == (m + n) % 2:
        print(f'f) Move the bishop to ({int(k + abs(k + l - m - n ) / 2)}, {int(l + abs(k + l - m - n ) / 2)}) and then to ({m}, {n})')
    else:
        print('f) The bishop may not move to these square')


if __name__ == '__main__':
    main()