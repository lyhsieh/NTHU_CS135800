def indent_list(L, level = 0):
    if L == None:
        return
    if type(L) in {list, tuple}:
        for child in L:
            indent_list(child, level + 1)
    else:
        print(f'{" " * 4 * level}{L}')

if __name__ == '__main__':
    L = ['F1', ['F4', 'F5',['F8']], 'F2', 'F3', 'D3', ['F6', 'F7']] 
    indent_list(L)
