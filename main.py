#プレイヤーを交互に変更する関数：
def switch_player(player):
    if player == 1:
        return 2
    else:
        return 1

def create_board():
    #ボード作成＆初期配置設定(0:none 1:black 2:white)
    board = [[0 for _ in range(8)] for _ in range(8)]
    board[3][3] = 1
    board[4][4] = 1
    board[3][4] = 2
    board[4][3] = 2    
    return board

#数値(0,1,2)を文字列(-,●,○)で返す関数作成
def int2stone(i: int) -> str:
    if i == 0:
        return '-'
    if i == 1:
        return '●'
    if i == 2:
        return '○'

#ボードを表示する関数
def show_board(board):
    for row in board: #確認！！！！！！！
        print(*[int2stone(i) for i in row]) #int2stone関数から条件を受け取り代入し表示　確認！！！！！！
    
#横軸でリーバス可能なマスを表示
def reversible_stones(board, x, y) -> list:
    right_stones = reversible_right_stones(board=board, x=x, y=y)
    left_stones = reversible_left_stones(board=board, x=x, y=y)
    return right_stones + left_stones

#リバース可能な値を表示
def show_reversible_stones(board, x, y):
    stones = reversible_stones(board=board, x=x, y=y)
    return stones

#入力値の正誤ジャッチ
def judge_input(board, x, y) -> tuple:
    while True:
        if x.isdecimal() == False or y.isdecimal() == False: #10進数に変換できない値が入力された場合の処理
            print('不正な入力です。再度入力してください。')
            show_board(board=board)
            x = input('x:')
            y = input('y:')
        else:
            return (x, y)

#入力(x,y)の正誤ジャッジ&正しい入力を返す関数
def judge_input_stone(board) -> tuple:
    while True:
        print('下記からマスを選択してください。')
        # stones = show_reversible_stones(board=board, x=x, y=y)
        # print(stones)
        x_str = input('x:')
        y_str = input('y:')
        x_str, y_str = judge_input(board=board, x=x_str, y=y_str) #正しい10進数に変換できる値だけ通す
        x = int(x_str)
        y = int(y_str)

        #有効なマスを選択していない場合
        if (x < 0 or x > 7) or (y < 0 or y > 7):
            show_board(board=board)
            print("有効なマスではありません。")
            
        #既に石が置いてある場合
        elif board[y][x] != 0:
            show_board(board=board)
            print("既に石が存在します。") 

        #リバースできる石が無い場合
        elif not reversible_stones(board=board, x=x, y=y):
            show_board(board=board)
            print("リバースできる石がありません。") 

        #正しいマスに置かれた場合
        else:
            return (x, y)

#player1が石を置く関数
def put(board, x, y):
    board[y][x] = 1

#player1が置いた場合にリバースできる石をリスト化(x方向:右)
def reversible_right_stones(board, x, y) -> list:
    list = [] #空リスト作成
    stone_position = x #置いた石のx座標の値を取得
    while stone_position+1 < 8: #置いた位置から右へ移動しながら判定する
        if board[y][stone_position+1] == 1: #自分の石に当たったら、以降の処理を中断
            break
        elif board[y][stone_position+1] == 0: #もしも空だった場合
            break
        elif board[y][stone_position+1] == 2: #もしも相手の石だった場合
            list.append([y, stone_position+1])
        stone_position += 1
    return list #リストを返す

#置いた場合にリバースできる石をリスト化(x方向:左)
def reversible_left_stones(board, x, y) -> list:
    list = [] #空リスト作成
    stone_position = x #置いた石のx座標の値を取得
    while stone_position-1 > 0: #置いた位置から右へ移動しながら判定する
        if board[y][stone_position-1] == 1: #自分の石に当たったら、以降の処理を中断
            break
        elif board[y][stone_position-1] == 0: #もしも空だった場合
            break
        elif board[y][stone_position-1] == 2: #もしも相手の石だった場合
            list.append([y, stone_position-1])

        stone_position -= 1
    return list #リストを返す

#石をリバースする関数
def reverse_stones(board, x, y): 
    for stone in reversible_stones(board=board, x=x, y=y): #for文でリバースできる石のリストから順に石をひっくり返す
        board[stone[0]][stone[1]] = 1 #石をリバースする

#メイン関数（実行）
def main():
    board = create_board()

    player = 1
    while True:
        #show_board関数実行（キーワード引数活用）
        show_board(board=board) 

        print("player",player,"の手番です。")
        player = switch_player(player)

        #palyer1が置いた石の正誤ジャッジ&正しい入力を返す関数の実行
        x, y = judge_input_stone(board=board)

        #player1が石を置く関数の実行
        put(board=board, x=x, y=y)

        #player1が石をリバースする関数の実行
        reversible_right_list = reversible_right_stones(board=board, x=x, y=y) #返り値を変数に代入する
        reverse_stones(board=board, reversible_stones=reversible_right_list, x=x, y=y) #関数の返り値を引用する際は、変数に格納してからそれを引数とする
    
        reversible_left_list = reversible_left_stones(board=board, x=x, y=y) #返り値を変数に代入する
        reverse_stones(board=board, reversible_stones=reversible_left_list, x=x, y=y) #関数の返り値を引用する際は、変数に格納してからそれを引数とする

        #リバース後のボードを表示する関数の実行
        show_board(board=board)

if __name__ == '__main__':
    main()



#誤った入力の場合、ボードを表示してあげる　✓
#座標番号を示したい 
#繰り返しをなるべくなくす
#文字列など入力した場合、例外処理してあげる　✓
#置けない（１，４）に置けてしまうt　✓