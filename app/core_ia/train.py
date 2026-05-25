import torch
from datasets import load_dataset
from transformers import AutoTokenizer,AutoModelForSequenceClassification,TrainingArguments,Trainer

print("Running")
dataset = load_dataset("pubmed_qa","pqa_labeled", split="train")
dataset = dataset.train_test_split(test_size=0.2)

model_name= "distilbert-base-uncased"
tokenizer== AutoTokenizer.from_pretrained(model_name)

def tokenizer_function(examples):
    
    textos = [f"Context : {c} Question {q}" for c, q in zip(examples['context'],examples['question'])]
    label_mapping = {"yes": 0, "no": 1, "maybe":2}
    label= [label_mapping[l] for l in examples['final_decision']]
    
