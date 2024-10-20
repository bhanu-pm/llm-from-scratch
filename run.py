# Running the whole pipeline 
import torch
import bpe
import bpe_essentials as e
import tokenizer
import token_loader
import llm


if __name__ == "__main__":
	device = "cuda" if torch.cuda.is_available() else "cpu"

	byte_pair_tokenizer = bpe.BytePairEncoding()
	bpe_tokens = byte_pair_tokenizer.encoder()

	tk_loader = token_loader.TokenLoader()

	# embedding
	# positional embedding

	# train loop
	