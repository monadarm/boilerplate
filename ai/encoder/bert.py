from transformers import BertTokenizer, BertModel
import torch

def get_embeddings(text):
    # Load pre-trained model tokenizer
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # Encode text
    encoded_input = tokenizer(text, return_tensors='pt')

    # Load pre-trained model
    model = BertModel.from_pretrained('bert-base-uncased')

    # Forward pass, get hidden states
    with torch.no_grad():
        outputs = model(**encoded_input)

    # Get the embeddings of the [CLS] token (the first token)
    embeddings = outputs.last_hidden_state[:, 0, :].squeeze()

    return embeddings

# Example usage
text = "Hello, how are you?"
embeddings = get_embeddings(text)
print(embeddings)
