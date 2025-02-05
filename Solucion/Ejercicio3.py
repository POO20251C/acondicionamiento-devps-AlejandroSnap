def is_palindrome(word: str):
  word = word.replace(" ", "")
  word = word.lower()
  result = False

  if word == word[::-1]:
    result = True
    
  return "Si" if result else "No"

def main():
  text = input("")
  print(is_palindrome(text))

main()