spam = 'ham'
print(spam)

# print(egg)
## exec print(egg) ##
# Traceback (most recent call last):
#  File "/Users/babaShumpei/Desktop/work/shbaba/perfect-python/part2/2-6_variable.py", line 4, in <module>
#    print(egg)
#          ^^^
# NameError: name 'egg' is not defined

del spam
# print(spam)

## exec print(spam)
# ham
# Traceback (most recent call last):
#   File "/Users/babaShumpei/Desktop/work/shbaba/perfect-python/part2/2-6_variable.py", line 13, in <module>
#     print(spam)
#           ^^^^
# NameError: name 'spam' is not defined

spam = 'ham'
def egg():
	spam = 'egg'
	print(spam)

egg()

print(spam)

# print('exception')
# spam = 'ham'
# def egg():
# 	print(spam)
# 	spam='egg'
# 
# egg()

## 実行結果 ##
# Traceback (most recent call last):
#   File "/Users/babaShumpei/Desktop/work/shbaba/perfect-python/part2/2-6_variable.py", line 38, in <module>
#     egg()
#   File "/Users/babaShumpei/Desktop/work/shbaba/perfect-python/part2/2-6_variable.py", line 35, in egg
#     print(spam)
#           ^^^^
# UnboundLocalError: cannot access local variable 'spam' where it is not associated with a value

