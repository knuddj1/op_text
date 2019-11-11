# OP Text
A wrapper around the popular [transformers](https://github.com/huggingface/transformers)  machine learning library, by the HuggingFace team, providing a simplified, keras like, interface for fine-tuning, evaluating and inference of the popular pretrained BERT models.

## Installation
PyTorch is required as a prerequisite before installing OP Text. Head on over to the [getting started  page](https://pytorch.org/get-started/locally/) of their website and follow the installation instructions for your version of Python. 

>!Currently only Python versions 3.6 and above are supported

Use one of the following commands to install OP Text:

### with pip

    pip install op_text
    
### with anaconda

    conda install op_text
    
## Usage 
The entire purpose of this package is to allow users to leverage the power of the transformer models available in HuggingFace's library without needing to understand how to use PyTorch.

### Model Loading
Current the available models are:
 1. BERT from the paper [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding(https://arxiv.org/abs/1810.04805)](https://arxiv.org/abs/1810.04805) released by Google.

2. RoBERTa from the paper [Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692) released by Facebook.

3. DistilBERT from the paper [DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108) released by HuggingFace.

Loading a model is achieved in one line of code. The string can either be the name of a pretrained model or a path to a local fine-tuned model on disk.

    from op_text.models import Bert
	
	# Loading a pretrained model
	model = Bert("bert-base-uncased")
	
	# Loading a fine-tuned model
	model = Bert("path/to/local/model/")

Each model has contains a list of the available model pretrained models.
Use the **DOWNLOADABLES** property to access them.

    Bert.DOWNLOADBLES
    >> ['bert-base-uncased','bert-large-uncased']
    
	Roberta.DOWNLOADBLES
	>> ['roberta-base','roberta-large']
	
	DistilBert.DOWNLOADABLES
	>> ['distilbert-base-uncased']

