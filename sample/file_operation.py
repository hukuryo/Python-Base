import json

def file_operation():
    # f = open('file.txt')
    # for line in f:
    #     print(line)
    
    # for line in f:
    #     print(line.strip())

    # f.close()
    
    # 'w'を付けることでファイルに書き込むことを宣言する。
    # f = open('file.txt', 'w')
    # f.write('Hello, World!\n')
    # f.close()
    
    # with open('file.txt') as f:
    #     for line in f:
    #         print(line)
    
    # Jsonファイル読み込み
    # with open('example.json') as f:
    #     json_deta = json.load(f)
    #     print(json_deta)
    
    json_data = {
        "message": "Hello, World!",
        "items": [0, 1, 2],
        "ok": True,
    }
    
    with open("example2.json", "w") as f:
        json.dump(json_data, f)
    