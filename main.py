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
    
#横軸でリーバス可能なマス
def reversible_stones(board, x, y, player) -> list:
    right_stones = reversible_right_stones(board=board, x=x, y=y, player=player)
    left_stones = reversible_left_stones(board=board, x=x, y=y, player=player)
    upper_stones = reversible_upper_stones(board=board, x=x, y=y, player=player)
    bottom_stones = reversible_bottom_stones(board=board, x=x, y=y, player=player)
    return right_stones + left_stones + upper_stones + bottom_stones

#リバース可能な値を表示
def show_reversible_stones(board, x, y, player):
    stones = reversible_stones(board=board, x=x, y=y, player=player)
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
def judge_input_stone(board, player) -> tuple:
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
        elif not reversible_stones(board=board, x=x, y=y, player=player):
            show_board(board=board)
            print("リバースできる石がありません。") 

        #正しいマスに置かれた場合
        else:
            return (x, y)

#player1が石を置く関数
def put(board, x, y, player):
    board[y][x] = player

#player1が置いた場合にリバースできる石をリスト化(x方向:右)
def reversible_right_stones(board, x, y, player) -> list:
    stones = [] #空リスト作成
    stone_position = x #置いた石のx座標の値を取得
    while stone_position+1 <= 8: #置いた位置から右へ移動しながら判定する
        if board[y][stone_position+1] == player: #自分の石に当たったら、以降の処理を中断
            break
        elif board[y][stone_position+1] == 0: #もしも空だった場合
            break
        elif board[y][stone_position+1] != player: #もしも相手の石だった場合
            stones.append([stone_position+1, y])
        stone_position += 1
    print('右リスト',stones)
    return stones #リストを返す

#置いた場合にリバースできる石をリスト化(x方向:左)
def reversible_left_stones(board, x, y, player) -> list:
    stones = [] #空リスト作成
    stone_position = x #置いた石のx座標の値を取得
    while stone_position-1 >= 0: #置いた位置から右へ移動しながら判定する
        if board[y][stone_position-1] == player: #自分の石に当たったら、以降の処理を中断
            break
        elif board[y][stone_position-1] == 0: #もしも空だった場合
            break
        elif board[y][stone_position-1] != player: #もしも相手の石だった場合
            stones.append([stone_position-1, y])
        stone_position -= 1
    print('左リスト',stones)
    return stones #リストを返す



#player1が置いた場合にリバースできる石をリスト化(y方向:上)
def reversible_upper_stones(board, x, y, player) -> list:
    stones = [] #空リスト作成
    stone_position = y #置いた石のy座標の値を取得

    while board[stone_position-1][x] != player and board[stone_position-2][x] == player : #置いた位置から下へ移動しながら判定する #次のマスを探索して相手の石があり続ける限り       
            stones.append([x, stone_position-1])   
            stone_position -= 1
            print('下リスト',stones)
    return stones #リストを返す

#1. 着手した石の周囲8方向に対して、隣接する石が相手の石である場合に限り、その方向に進みながら相手の石を探索します。この探索を繰り返して、相手の石が続いている限り進みます。

#置いた場合にリバースできる石をリスト化(y方向:下)
def reversible_bottom_stones(board, x, y, player) -> list:
    stones = [] #空リスト作成
    stone_position = y #置いた石のy座標の値を取得
    while board[stone_position+1][x] != player and board[stone_position+2][x] == player : #置いた位置から下へ移動しながら判定する #次のマスを探索して相手の石があり続ける限り       
            stones.append([x, stone_position+1])   
            stone_position += 1
            print('下リスト',stones)
    return stones #リストを返す

#石をリバースする関数
def reverse_stones(board, x, y, player): 
    stones = reversible_stones(board=board, x=x, y=y, player=player)
    for stone in stones: #for文でリバースできる石のリストから順に石をひっくり返す
        x_position = stone[0]
        y_position = stone[1] 
        board[y_position][x_position] = player #石をリバースする

#メイン関数（実行）
def main():
    board = create_board()

    player = 2
    while True:
        #show_board関数実行（キーワード引数活用）
        show_board(board=board) 


        player = switch_player(player)
        print("player",player,"の手番です。")
        #palyer1が置いた石の正誤ジャッジ&正しい入力を返す関数の実行
        x, y = judge_input_stone(board=board, player=player)

        #player1が石を置く関数の実行
        put(board=board, x=x, y=y, player=player)

        #player1が石をリバースする関数の実行
        reverse_stones(board=board, x=x, y=y, player=player) #関数の返り値を引用する際は、変数に格納してからそれを引数とする

        print("---player change!---")

if __name__ == '__main__':
    main()



#誤った入力の場合、ボードを表示してあげる　✓
#座標番号を示したい 
#繰り返しをなるべくなくす
#文字列など入力した場合、例外処理してあげる　✓
#置けない（１，４）に置けてしまうt　✓

#縦と斜めのリバース可能な石を探索したい


#player1が置いた場合にリバースできる石をリスト化(y方向:上)
def reversible_upper_stones(board, x, y, player) -> list:
    stones = [] #空リスト作成
    stone_position = y #置いた石のy座標の値を取得
    while stone_position-1 >= 0: #置いた位置から上へ移動しながら判定する
        if board[stone_position-1][x] == player: #自分の石に当たったら、以降の処理を中断
            break
        elif board[stone_position-1][x] == 0: #もしも空だった場合
            break
        elif board[stone_position-1][x] != player and board[stone_position-2][x] == player: #もしも相手の石だった場合
            stones.append([x, stone_position-1])
        stone_position -= 1
        print('上リスト',stones)
    return stones #リストを返す