dev find_anagram(word, anagram)
    str1 = word
    str2 = anagram
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted(str1) == sorted(str2):
        return True
    else:
        return False 

    
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))
