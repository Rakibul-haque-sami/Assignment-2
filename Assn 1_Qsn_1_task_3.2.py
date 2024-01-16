# Qsn 1, task 3.2 : Using the ‘Auto Tokenizer’ function in the ‘Transformers’ library, write a  ‘function’ to count unique tokens in the text (.txt) and give the ‘Top 30’ words

from transformers import AutoTokenizer
def count_tokens(text_file):
  with open(text_file, "r") as f:
    text = f.read()
  tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
  tokens = tokenizer.tokenize(text)
  unique_tokens = set(tokens)
  print("Number of unique tokens:", len(unique_tokens))
  top_30_words = sorted(unique_tokens, key=lambda x: tokens.count(x), reverse=True)[:30]
  print("Top 30 words:", top_30_words)
