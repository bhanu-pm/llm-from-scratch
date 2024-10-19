# Byte pair encoding for input text

class BytePairEncoding():
	def __init__(self, input_text):
		self.input_text = input_text
		self.input_letter_list = [i for i in self.input_text]

	def counter(self):
		pass

	def merge_rule(self):
		pass

	def encoder(self):
		pass

	def decoder(self):
		pass


if __name__ == "__main__":
	text = ""
	bpe = BytePairEncoding()
	final_tokens = bpe.encoder(text)
	print(final_tokens)