count = 1
total = 0

# BUG: Missing a colon (:) at the end of the while condition line, causing a SyntaxError.
# BUG: The condition 'count < 5' stops the loop before 5 is added. Changed to 'count <= 5' to include 5.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Attempting to concatenate a string and an integer ('total') directly, causing a TypeError. Fixed using an f-string or converting total to str().
print(f"Sum of 1 to 5 is: {total}")

