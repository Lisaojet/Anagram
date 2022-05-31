dev find_anagram(word, anagram)
    str1 = input("word:")
    str2 = input("anagram:")
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

if sorted_str1 == sorted_str2:
    return True
else:
     return False 
print(find_anagram("below", "elbow"))
