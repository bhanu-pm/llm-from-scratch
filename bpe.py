# Byte pair encoding for input text
import bpe_essentials as e


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
	vocab_builder_text = ""
	vocab_builder = e.BPE_Vocab_Builder(vocab_builder_text)
	vocab_dict = vocab_builder.builder()
	text_to_encode = ""
	bpe = BytePairEncoding()
	final_tokens = bpe.encoder(text_to_encode)
	print(final_tokens)