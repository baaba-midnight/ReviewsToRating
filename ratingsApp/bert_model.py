import torch
from transformers import DistilBertTokenizerFast, DistilBertModel
from torch import nn

tokenizer = DistilBertTokenizerFast.from_pretrained("ratingsApp\models\G15_tokenizer\G15_tokenizer")

# Load the model architecture
class CustomDistilBertModel(nn.Module):
    def __init__(self, base_model, num_labels, freeze_base=True, use_custom_head=True):
        super(CustomDistilBertModel, self).__init__()
        self.base_model = base_model
        if freeze_base:
            for param in self.base_model.parameters():
                param.requires_grad = False

        if use_custom_head:
            self.dropout = nn.Dropout(p=0.3)
            self.classifier = nn.Linear(768, num_labels)  # Assuming 768 is the base model output size
        else:
            self.classifier = nn.Identity()

        self.use_custom_head = use_custom_head

    def forward(self, input_ids, attention_mask):
        outputs = self.base_model(input_ids=input_ids, attention_mask=attention_mask)
        hidden_state = outputs.last_hidden_state[:, 0, :]
        if self.use_custom_head:
            hidden_state = self.dropout(hidden_state)
        logits = self.classifier(hidden_state)
        return logits

# Initialize the model
base_model = DistilBertModel.from_pretrained("distilbert-base-uncased")
model = CustomDistilBertModel(base_model, num_labels=5)
model.load_state_dict(torch.load('ratingsApp\models\G15_model.pth', map_location=torch.device('cpu')))





# class BertModel:
#     def __init__(self):
#         # Load model and tokenizer from the saved directory
#         self.tokenizer = tokenizer = DistilBertTokenizerFast.from_pretrained("/content/drive/MyDrive/Colab Notebooks/Final Project AI/tokenizer/G15_tokenizer")
#         self.model = TFBertModel.from_pretrained('./bert_model')

#     def get_embeddings(self, text):
#         # Tokenize input text
#         inputs = self.tokenizer(text, return_tensors='tf', truncation=True, padding=True, max_length=512)

#         # Get the embeddings from BERT
#         outputs = self.model(**inputs)

#         # The embeddings are in the last_hidden_state
#         return outputs.last_hidden_state
    
# bert_model = BertModel()