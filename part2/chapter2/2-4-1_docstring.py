# -*- encoding: utf-8 -*-
def docstring_test():
	"""この関数はドキュメンテーション文字列のテスト。"""
	return True

print(docstring_test.__doc__)
# ドキュメンテーション文字列に記述したテキストは定義した関数やクラスオブジェクトの特別なプロパティ"__doc__"に記述される。
