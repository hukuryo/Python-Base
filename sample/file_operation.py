def file_operation():
    # f = open('file.txt')
    # for line in f:
    #     print(line)
    
    # for line in f:
    #     print(line.strip())

    # f.close()
    
    # 'w'を付けることでファイルに書き込むことを宣言する。
    f = open('file.txt', 'w')
    f.write('Hello, World!\n')
    f.close()