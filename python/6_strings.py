# 1. Different ways of creating a string
str1 = 'Hello'
str2 = "World"
str3 = '''Multiline
String'''
str4 = str("Using str constructor")
print(str1, str2, str3, str4)

print()

# 2. Concatenating two strings using + operator
greeting = str1 + " " + str2
print(greeting)

print()

# 3. Finding the length of the string (without len())
count = 0
for _ in greeting:
    count += 1
print(count)

print()

# 4. Extract a string using Substring (manual slicing)
start = 0
end = 5
substring = ""
i = 0
for ch in greeting:
    if i >= start and i < end:
        substring += ch
    i += 1
print(substring)

print()

# 5. Searching in strings using index() (manual search)
search = "World"
found = -1
for i in range(count - len(search) + 1):
    match = True
    for j in range(len(search)):
        if greeting[i + j] != search[j]:
            match = False
            break
    if match:
        found = i
        break
print(found)

print()

# 6. Matching a String Against a Regular Expression With matches()
# (Manual match for exact pattern "Hello World")
pattern = "Hello World"
is_match = True
if count != len(pattern):
    is_match = False
else:
    for i in range(count):
        if greeting[i] != pattern[i]:
            is_match = False
            break
print(is_match)

print()

# 7. Comparing strings
a = "apple"
b = "banana"
equal = True
if len(a) != len(b):
    equal = False
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            equal = False
            break
print(equal)
print(a < b)  # Lexicographical comparison still works

print()

# 8. startsWith(), endsWith(), and compareTo()
prefix = "Hello"
suffix = "World"
starts = True
for i in range(len(prefix)):
    if greeting[i] != prefix[i]:
        starts = False
        break
print(starts)

ends = True
for i in range(len(suffix)):
    if greeting[-len(suffix) + i] != suffix[i]:
        ends = False
        break
print(ends)

# compareTo equivalent
if a == b:
    print(0)
elif a < b:
    print(-1)
else:
    print(1)

print()

# 9. Trimming strings with strip() (manual)
messy = "   spaced out   "
start = 0
end = len(messy) - 1
while start <= end and messy[start] == ' ':
    start += 1
while end >= start and messy[end] == ' ':
    end -= 1
trimmed = ""
for i in range(start, end + 1):
    trimmed += messy[i]
print(trimmed)

print()

# 10. Replacing characters in strings with replace() (manual)
text = "banana"
new_text = ""
for ch in text:
    if ch == 'a':
        new_text += 'o'
    else:
        new_text += ch
print(new_text)

print()

# 11. Splitting strings with split() (manual)
sentence = "This is a test"
words = []
word = ""
for ch in sentence:
    if ch == ' ':
        words.append(word)
        word = ""
    else:
        word += ch
if word:
    words.append(word)
print(words)

print()

# 12. Converting integer objects to Strings (manual)
num = 123
digits = "0123456789"
num_str = ""
n = num
if n == 0:
    num_str = "0"
else:
    while n > 0:
        digit = n % 10
        num_str = digits[digit] + num_str
        n //= 10
print(num_str + " is now a string")

print()

# 13. Converting to uppercase and lowercase (manual)
# Only works for ASCII letters
upper = ""
lower = ""
for ch in greeting:
    if 'a' <= ch <= 'z':
        upper += chr(ord(ch) - 32)
    else:
        upper += ch
    if 'A' <= ch <= 'Z':
        lower += chr(ord(ch) + 32)
    else:
        lower += ch
print(upper)
print(lower)
