import numpy as np


def minimal_weighings(number_of_balls):
  """
  Calculates the minimum number of weighings needed to
  find the heavier ball among `number_of_balls` balls.

  Args:
    number_of_balls: The number of balls (int type).

  Returns:
    The minimum number of weighings (int type).
  """

  if number_of_balls <= 1:
    return 0
  else:
    # Calculate the minimum number of weighings
    minimal_number_of_weighings = int(np.floor(np.log2(number_of_balls - 1)) / np.log2(3)) + 1

  return minimal_number_of_weighings


# Get the number of balls from the user
number_of_balls = int(input("Enter the number of balls: "))

# Calculate the minimum number of weighings
minimal_number_of_weighings = minimal_weighings(number_of_balls)

# Display the result
print(f"The minimum number of weighings is: {minimal_number_of_weighings}")
