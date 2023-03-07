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

#player1が石を置く関数
def player1_put(board, x, y):
    board[y][x] = 1

#player1が置いた場合にひっくり返せる石をリスト化(x方向:右)
def player1_reversible_xright(board, x, y):
    reversible_stones = [] #空リスト作成
    stone_xposition = x #置いた石のx座標の値を取得
    while stone_xposition+1 < 8: #置いた位置から右へ移動しながら判定する
        if board[y][stone_xposition+1] == 1: #自分の石に当たったら、以降の処理を中断
            break
        if board[y][stone_xposition+1] == 2: #もしも相手の石だった場合
            reversible_stones.append([y,stone_xposition+1])
        stone_xposition += 1
    return reversible_stones #リストを返す



#player1が置いた場合にひっくり返せる石をリスト化(x方向:左)
def player1_reversible_xleft(board, x, y):
    reversible_stones = [] #空リスト作成
    stone_xposition = x #置いた石のx座標の値を取得
    while stone_xposition-1 > 0: #置いた位置から左へ移動しながら判定する
        if board[y][stone_xposition+1] == 1: #自分の石に当たったら、以降の処理を中断
            break
        if board[y][stone_xposition-1] == 2: #もしも相手の石だった場合
            reversible_stones.append([y,stone_xposition-1])
        stone_xposition -= 1
    return reversible_stones #リストを返す


#player1が石をひっくり返す関数
def player1_reverse_stones(board, reversible_stones): 
    print(f"reversible_stones: {reversible_stones}")
    for reversible_stone in reversible_stones: #for文でひっくり返せる石のリストから順に石をひっくり返す
        board[reversible_stone[0]][reversible_stone[1]] = 1 #ひっくり返す

#メイン関数（実行）
def main():
    #ボード作成＆初期配置設定(0:none 1:black 2:white)
    board = [[0 for _ in range(8)] for _ in range(8)]
    board[3][3] = 1
    board[4][4] = 1
    board[3][4] = 2
    board[4][3] = 2

    show_board(board=board) #show_board関数実行（キーワード引数活用）

    #player1が石を置く
    x = int(input('x:')) 
    y = int(input('y:'))
    
    player1_put(board=board, x=x, y=y) #player1が石を置く関数の実行

    reversible_stones_xright = player1_reversible_xright(board=board, x=x, y=y) #返り値を変数に代入する
    player1_reverse_stones(board=board, reversible_stones=reversible_stones_xright) #関数の返り値を引用する際は、変数に格納してからそれを引数とする
    reversible_stones_xleft = player1_reversible_xleft(board=board, x=x, y=y) #返り値を変数に代入する
    player1_reverse_stones(board=board, reversible_stones=reversible_stones_xleft) #関数の返り値を引用する際は、変数に格納してからそれを引数とする
 
    show_board(board=board) #ボードを表示する関数の実行


#player1と2が交互に石を打つ
#置ける箇所がなくなるまで上記を繰り返す
#各playerの置いてある石の数をカウントし、勝敗表示

if __name__ == '__main__':
    main()