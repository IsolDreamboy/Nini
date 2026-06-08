import torch
from datasets import load_dataset
from transformers import AutoTokenizer,AutoModelForSequenceClassification,TrainingArguments,Trainer

print("Running")
dataset = load_dataset("pubmed_qa","pqa_labeled", split="train")
dataset = dataset.train_test_split(test_size=0.2)

model_name= "distilbert-base-uncased"
tokenizer= AutoTokenizer.from_pretrained(model_name)

def tokenizer_function(examples):
    
    textos = [f"Context : {c} Question {q}" for c, q in zip(examples['context'],examples['question'])]
    label_mapping = {"yes": 0, "no": 1, "maybe":2}
    labels = [label_mapping[l] for l in examples['final_decision']]

    tokenized = tokenizer(textos, truncation=True, padding="max_length", max_length=256)
    tokenized["labels"] = labels
    return tokenized
    
print("teste,teste,mic check OK")
tokenized_datasets = dataset.map(tokenizer_function, batched=True)

model=AutoModelForSequenceClassification.from_pretrained(model_name,num_labels=3)

training_args = TrainingArguments(
    output_dir = "./resultados_pubmed",
    eval_strategy = "epoch",
    save_strategy = "epoch",
    learning_rate = 2e-5,
    per_device_train_batch_size = 8,
    per_device_eval_batch_size = 8,
    num_train_epochs = 3,
    weight_decay = 0.01,
    logging_dir = "./logs",
    logging_steps = 10,
    fp16=torch.cuda.is.available(),  
)

trainer=Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['test'],

)

print("treinem, treinem e treinem!!1")
trainer.train() 

model.save_pretrained("./meu_modelo_medico_otimizado")
tokenizer.save_pretrained("./meu_modelo_medico_otimizado")
print("e isso é tutututututudo pepepepepessoal")