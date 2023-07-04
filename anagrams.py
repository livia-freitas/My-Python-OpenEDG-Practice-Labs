def anagram():
    line1 = input("Please type a word.")
    line2 = input("Please input another word.")
    letters1 = [*line1]
    letters2 = [*line2]
    list1 = sorted(letters1)
    list2 = sorted(letters2)
    if (list1 == list2):
        print("Anagrams")
    else:
        print("Not anagrams")

anagram()