def pascal(row, column):    #calculate each element
    if column == 0 or column == row:
        return 1
    else:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)

def print_Pascal_triangle(lines):    #formatedly print out the result
    print('col: ', end = '')
    for i in range(lines):
        print(f'{i:3d}', end = '')
    print()

    for i in range(lines):
        print(f'row{i}:', end = '')
        for j in range(i + 1):
            ans = pascal(i, j)
            print(f'{ans:3d}', end = '')
        print()


if __name__ == '__main__':    #main function
    lines_str = input()
    lines = int(lines_str)
    print_Pascal_triangle(lines)
    