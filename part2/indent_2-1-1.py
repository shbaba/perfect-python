# -*- coding: utf-8 -*-
# 2章 Pythonの基本
def main():
	for i in range(1, 6):	# 1から5までのループ処理
		if i % 2 == 0:	# 偶数チェック
			print("%sは偶数です。" %i)	# 偶数の場合に出力
		else:
			print("%sは奇数です。" %i)	# 奇数の場合に出力

if __name__ == "__main__":	# コマンドラインからの実行かどうかの判定
	main()			# main()関数を呼び出す
