# Print split text in new line
print('hello \nworld')

# Pick a letter in string.
a = "hello Raj"
print("The text is", a[1])

# Checking string length
print(len(a))

# Using in Keyword to check for a text
txt = "all expensive things in life are not free"
if "free" in txt:
    print("text free is present")

# Checking not in text
if "offer" not in txt:
    print("Offer text is not present")

# Slicing Strings

print("The sliced text is", a[2:5])

# Slice text from Start
print("The sliced text is", a[:5])

# Slice text from End
print("The sliced text is", a[3:])

# Slice text using negative Indexing
print("The sliced text is", a[-6:-2])


# String Built in functions

# Convert text to upper case

free_text = "This is a sample text"
print(free_text.upper())

# Convert string to lower case
print(free_text.lower())

# Remove whitespaces between text
print(free_text.strip())

# Replace string in text
print(free_text.replace('H','J'))

# Split a string
print(free_text.split(","))

# Using format function in Strings

print("The quick brown fox {}".format("Inserted"))

print("The {0} {0} {0}".format("Quick", "Brown", "Fox"))

print("The {b} {c} {a}".format(a="quick", b="brown", c="fox"))

# Formating Values
# Syntax Float formatting follows "{value:width.precision f}"
# width is whitespace and precision is how many digits you need in float value

result = float(200*0.321)
print("The result of the number is {r:10.4f}".format(r=result))

# Format String
# Escape Characters
# String Methods
