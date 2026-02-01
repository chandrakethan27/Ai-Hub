import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4.1-mini")
tokens = encoding.encode("Hi my name is Kethan and I like Brownies")

print(tokens)

word = encoding.decode([12178])
print(word)