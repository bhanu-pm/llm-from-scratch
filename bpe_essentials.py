# Byte Pair encoding Vocab builder and Merge rules

class BPE_Vocab_Builder():
	def __init__(self, vocab_builder_text):
		self.vocab_builder_text = vocab_builder_text
		self.vb_text_list = [i for i in self.vocab_builder_text]

		self.count = 0
		for i in self.vb_text_list:
			if (i == ' ') or (i == '/s'):
				self.count += 1
				if self.count == 1:
					pass
				else:
					self.vb_text_list.remove(i)

	def builder(self):
		pass
		

if __name__ == "__main__":
	vocab_text = ""
	vocab_builder = BPE_Vocab_Builder(vocab_text)
	vocab_dict = BPE_Vocab_Builder.builder()