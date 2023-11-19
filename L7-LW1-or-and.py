# or / and
#
# exp_1 ?       op_bin      exp_2 ?
#    ^            ^            ^
#    |            |            |
# 1. eval left    |            |
#                 |        2. eval right
#                 |
#              3. exec
#              4. result


# |   ALGO
# |  1. eval left
# |     1.b truthy (or), falthy (and) --------+
# |  2. eval right                            |
# |     2.b truthy (or), falthy (and) ----+   |
# |  3. exec                              |   |
# |  4. result                            |   |
# v                                       v   v


# x => [-5 .. -3] or [10 ... 20]

# x = -4
# r = x >= -5 and x <= -3 or x >= 10 and x <= 20
#       |      |     |      |                   |
#       v      |     |      +------- Skip ------+  
#    1.True    |     v     
#              |  2.True   
#              v            
#            3.True              
#                       

#################################################

# HW1: try to explain how it works for:
# x = -10
# r = x >= -5 and x <= -3 or x >= 10 and x <= 20
#       |            |     |    |           |
#       v            |     |    |           |
#    1.False         v     |    |           |
#                   Skip   |    v           |
#                          | 2.False        v
#                          v               Skip
#                       3.False