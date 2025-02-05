def countWords(word: str):
  return len(word.split())

def main():
  word = input("")
  print(countWords(word))

main()