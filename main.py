# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from operator import truediv


def find_anagram(word, anagram):
    # [assignment] Add your code here
   string_one = input ('string1:')
   string_two = input('string2:')
   sorted_string_one = sorted(string_one)
   sorted_string_two = sorted(string_two)

   if sorted_string_one == sorted_string_two:
       return True
   else:
       return False
find_anagram("below", "elbow")       
  

