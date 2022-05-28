str1 = input("word:")
str2 = input("anagram:")
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if sorted_str1 == sorted_str2:
    print("This is an Anagram")
else:
     print("This is not an Anagram")
    