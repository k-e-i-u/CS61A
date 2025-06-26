from urllib.request import urlopen   #"urlopen" can access the content at a uniform resource locator (URL)

# an assignment statement
# associates the name shakespeare with the value of the expression that follows "="
# "urlopen('http://composingprograms.com/shakespeare.txt')" is an expression.
shakespeare = urlopen('https://raw.githubusercontent.com/maxg203/Python-for-Beginners/refs/heads/master/shakespeare.txt') 

# another assignment statement
words = set(shakespeare.read().decode().split())

print(words)

print({w for w in words if len(w) == 6 and w[::-1] in words})

for w in words:
    print(w)
    print(w[::-1])  # [::-1]在python中，可以用作将字符串取反

