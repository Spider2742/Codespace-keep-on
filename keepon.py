import random
import time

def write_number(filename):
  """Writes a random single-digit number to a text file.

  Args:
    filename: The name of the text file to write to.
  """
  # Generate random single-digit number (0-9)
  number = random.randint(0, 9)
  with open(filename, "a") as f:
    f.write(str(number) + "\n")

# Set the filename and time interval
filename = "numbers.txt"
interval = 120  # Seconds (2 minutes)

while True:
  write_number(filename)
  time.sleep(interval)
  
