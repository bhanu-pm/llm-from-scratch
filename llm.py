# Model Architecture 
import torch
import bpe
import tokenizer
import token_loader


device = "cuda" if torch.cuda.is_available() else "cpu"
vocab_size = 99		# Total size of all possible vocabulary. Get it from bpe_essentials builder function.
vocab_dimensions = 3 	# No. of dims used to represent a single vocab token vector.


class LLM(torch.nn.module):
	def __init__(self, ):
		pass

	def forward(self, ):
		pass