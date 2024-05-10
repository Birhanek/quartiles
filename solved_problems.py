
# Anagram is a word or phrase formed by rearranging the letters of a different word phrase,
# typically using all the original letters exactly once

def anagram(s1:str, s2:str) -> bool:
    string_list = list(s2)

    for string in s1:
        if string in string_list:
            string_list.remove(string)
        else:
            return False
    return True

s1 = 'anagram'
s2 = 'nagaram'
# s1 = 'rat'
# s2 = 'car'

#print(anagram(s1,s2))

def isAnagram(s1:str, s2:str) ->bool:
    counter_1 = sorted(s1)
    counter_2 = sorted(s2)
    return counter_1 == counter_2

#print(isAnagram(s1, s2))

# returning the first letter to appear twice
def twoLetter(s1:str) -> str:
    s2 = s1.lower()
    seen_letters = []
    for c in s2:
        if c in seen_letters:
            return c
        else:
            seen_letters.append(c)
#print(twoLetter('Guaranteed'))

# running sum of 1D list

def running_sum(lst:list) ->list:
    sum_lst = []
    sum_two = 0
    for num in lst:
        sum_two += num
        sum_lst.append(sum_two)
    return sum_lst
print(running_sum([1,1,1,1,1]))