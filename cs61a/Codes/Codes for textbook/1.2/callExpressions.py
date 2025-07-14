# a elementary call expressions
print(max(1, 2))

# the sequence of operands is important
print(pow(100, 2))
print(pow(2,100))

# The call expression can be nested multiple times as you wish.
#  An important role for you as a programmer is to structure expressions
#  so that they remain interpretable by yourself, your programming partners, 
# and other people who may read your expressions in the future.
print(max(min(1, -2), min(pow(3, 5), -4)))

