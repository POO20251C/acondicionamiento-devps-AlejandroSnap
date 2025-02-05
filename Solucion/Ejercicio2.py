vowels = ["a", "e", "i", "o", "u"]

def main():
  text = input("")
  result = 0
  for char in text:
    char = char.lower()
    if char in vowels:
      result += 1

  print(result)

main()