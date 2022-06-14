
def find_anagram(word, anagram):
    word = word.replace(" ", "")
    anagram = anagram.replace(" ", "")
    if sorted(word) == sorted(anagram):
        return True
    else:
        return False


print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
