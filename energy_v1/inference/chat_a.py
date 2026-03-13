import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, TextIteratorStreamer
from threading import Thread

model_path = "./energy_model"

# rebuild tokenizer like training
tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")

special_tokens = {
    "additional_special_tokens": ["<|user|>", "<|assistant|>"]
}

tokenizer.add_special_tokens(special_tokens)
tokenizer.pad_token = tokenizer.eos_token

# load trained model
model = GPT2LMHeadModel.from_pretrained(model_path)

# resize embeddings
model.resize_token_embeddings(len(tokenizer))

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

print("\n⚡ Energy AI Chat Mode ⚡")
print("Type 'exit' anytime to quit\n")

while True:

    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        print("Goodbye 👋")
        break

    prompt = f"<|user|>: {question}\n<|assistant|>:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    # streamer for token-by-token animation
    streamer = TextIteratorStreamer(
        tokenizer,
        skip_prompt=True,
        skip_special_tokens=True
    )

    generation_kwargs = dict(
        **inputs,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id,
        streamer=streamer
    )

    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    print("\nAI: ", end="", flush=True)

    for new_text in streamer:
        print(new_text, end="", flush=True)

    print("\n")