import time



def load_words():
  all_words = []
  start_time = time.time()
  
  with open('safedict_simple.txt', 'r') as f:
    for line in f:
      all_words.append(line.rstrip())
  end_time = time.time()

  elapsed_time = end_time - start_time

  print('Loaded ' + str(len(all_words)) + ' words in ' + f'{elapsed_time:.2f}' + ' seconds.')

  return all_words
# lines commented out in this function are future issues and extensions change 
def suggest(text, all_words):
  if text in all_words:
    print(text + ' is a word')
  else:
    print(text + ' is not a word. we suggest using:')
    suggest_list = []
    # suggest_list_final = []

    for word in all_words:
      listed_word = list(word)
      listed_text = list(text)
      # text_leangth = len(listed_text)
      # word_leangth = len(listed_word)
      
      if listed_text[0] == listed_word[0] and listed_text[-1] == listed_word[-1]:
        listed_word = ' '.join(listed_word)
        suggest_list.append(listed_word)
        # for word in suggest_list:
        #   if text_leangth == word_leangth:
        #     suggest_list_final.append(listed_word)
          # if text_leangth == word_leangth + 1 or text_leangth == word_leangth - 1:
          #   suggest_list_final.append(listed_word)
    for word in suggest_list[0:10]:
      print(word)


    






def main():
    all_words = load_words()
    print('Type some text, or type \"quit\" to stop')
    while True:
        text = input(':> ')
        if ('quit' == text):
          break
        suggest(text, all_words)

if __name__ == "__main__":
    main()

