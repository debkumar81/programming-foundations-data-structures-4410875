def has_unique_characters(data):
    char=set()
    for str in data:
        if str in char:
            return False
        else:
            char.add(str)
    return True

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
