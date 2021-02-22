# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE
  x = 0; # Hold the number of threes.
  x1 = 0; # Use to count from 0 to n.
  while x1 < n:
      x1 = 3 + x1;
      if x1 <= n:
          x += 1;
  return x; 
  


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  currentCharCount = 0;
  currentChar = s[0];
  longestCharCount = 0;
  longestChar = s[0];
  count = 0;
  
  for i in s:   
     if currentChar != i:
         currentChar = i;
         currentCharCount = 0;
         currentChar = i;
     if longestCharCount < currentCharCount:
         longestCharCount = currentCharCount;
         longestChar = i; 
     currentCharCount += 1;
     count += 1;
      
  return longestChar;
  

# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  
  s.lower(); # Convert string to lowercase.
  x = True;
  count = len(s)-1;
  for i in s:
    if i.lower() != s[count].lower() and 'z' >= i >= 'a' and 'z' >= s[count] >= 'a':
        x = False;
        break;
    count -= 1;
  return x;
  
    
  '''
  EG28
  '''