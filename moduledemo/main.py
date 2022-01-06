#Solution1:
#import func as myfunc
#Solution2:
#import func # 因为是在当前目录
#Solution 3
from func import *


#########################################################
# 如果你要引入的不是模块，而是类的说话
#from mycore import Player, NBAPlayer
#########################################################

#From solution 1
#print(func.add(1,2))
#print(func.sub(5,2))

#from solution 2
#print(myfunc.add(1,2))
#print(myfunc.sub(10,2))

#from solution 3
print(add(1,6))