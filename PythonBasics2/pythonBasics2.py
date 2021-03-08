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
  # Dictionary.
  nums = {
      "3": 0,
      "6": 0,
      "9": 0,
  }

  # Variables + Constants.
  highest = 0;
  value = 0;
  
  # Find all multiples of 3 and count them.
  for x in n:
      if x == '3':
          nums["3"] += 1;
      elif x == '6':
          nums["6"] += 1;
      else:
          nums["9"] += 1;
          
  # Find the multiple of 3 with the highest count.
  for x, x1 in nums.items():
      if x1 > highest:
          highest = x1;
          value = x;
  # Return the multiple of 3 with the highest count.
  return int(value); 

# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  # Dictionary.
  chars = {
  }
  
  # Variables + Constants.
  highest = 0;
  values = [];
  currentChar ='0';
  longestCharCount = 0;
  currentCharCount = 0;
  
  # Determine the longest consecutive repeating chars.
  for i in s:
     # Add a char if it is not in the dictionary.
     if currentChar != i:
         currentChar = i;
         chars[i] = 0;
     # Save the current char if it is longer than the previous one.
     if longestCharCount <= currentCharCount:
         longestCharCount = currentCharCount;
         # Set all other chars to 0 when a new longest consecutive char is found.
         for x in values:
             if chars[x] < chars[i]:
                 chars[x] = 0; 
     # Add 1 to the current char value.
     chars[i] += 1;
  
  # Find the highest value.
  for x, x1 in chars.items():
      if x1 > highest:
          highest = x1;
  # Find the chars with the highest values.
  
  for x, x1 in chars.items():
      if x1 == highest:
          values.append(x);
  # Return the chars with the highest values.
  return values;

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
 
