#Author: Abigail Bowen aeb6095@psu.edu
def digit_sum(n):
  if n <= 1:
    return n
  else:
    return (n %10) + digit_sum(n//10)

def run ():
  n = int(input("Enter an int: "))
  sum1 = digit_sum(n)
  print(f"sum of digits of {n} is {sum1}.")

if __name__ == "__main__":
  run()