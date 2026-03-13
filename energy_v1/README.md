
# energy_v1

energy_v1 is the first experimental version of the Energy educational language model.
This version is created by fine-tuning the GPT-2 Medium model on a custom instruction dataset designed for university-related interactions.

The purpose of this version is to explore how a general language model can be adapted into a structured assistant capable of answering academic queries, responding using context, and generating structured tool calls.

---

## Base Model: GPT-2 Medium

The base model used for this project is GPT-2 Medium.

GPT-2 (Generative Pre-trained Transformer 2) is a transformer-based language model developed by OpenAI for natural language generation tasks. GPT-2 Medium contains approximately **355 million parameters** and is trained using a **decoder-only transformer architecture**.

Key characteristics of GPT-2 Medium:

* 355 million parameters
* Transformer decoder architecture
* Pre-trained on large internet text datasets
* Capable of generating coherent natural language text

### GPT-2 Architecture Overview

GPT-2 uses a stacked transformer decoder architecture consisting of multiple layers of:

* Multi-head self-attention
* Feed-forward neural networks
* Layer normalization
* Residual connections

The model processes tokens sequentially and predicts the next token in a sequence.

```
Input Text
   │
Tokenization
   │
Embedding Layer
   │
Transformer Decoder Blocks (Self Attention + Feed Forward)
   │
Language Modeling Head
   │
Next Token Prediction
```

Instead of training a language model from scratch, this project **fine-tunes GPT-2 Medium on a specialized instruction dataset**.

---

## Model Development

In this project, GPT-2 Medium was fine-tuned on a custom dataset to create a university assistant called **Energy**.

The fine-tuning process teaches the model to:

* behave like a conversational assistant
* answer questions using context
* generate structured tool calls
* ask for missing parameters when necessary
* maintain a consistent assistant identity

The dataset used for training contains **10,000 instruction samples**.

---

## Training Dataset

The instruction dataset is divided into several categories that represent different assistant behaviors.

| Category             | Samples | Purpose                                 |
| -------------------- | ------- | --------------------------------------- |
| Identity             | 300     | Maintain consistent assistant identity  |
| General conversation | 1,700   | Greetings and basic student interaction |
| RAG examples         | 4,000   | Answer questions using provided context |
| Tool calling         | 2,500   | Generate structured function calls      |
| Tool fallback        | 1,500   | Ask for missing parameters              |

This structure allows the model to behave like a **task-oriented assistant rather than a generic chatbot**.

---

## Dataset Format

Each training example follows a structured JSON format containing an instruction and the expected assistant response.

### Example: General Conversation

```json
{
 "type": "general",
 "instruction": "Hello",
 "output": "Hello! I'm Energy, your MIT WPU assistant. How can I help you today?"
}
```

### Example: RAG Style Response

```json
{
 "type": "rag",
 "context": "MIT WPU Notice: The university will remain closed on 15 August for Independence Day.",
 "instruction": "Will MIT WPU be closed on Independence Day?",
 "output": "The university will remain closed on 15 August for Independence Day."
}
```

### Example: Tool Calling

```json
{
 "type": "tool",
 "instruction": "Give me the timetable for Computer Engineering year 2 panel H",
 "output": "TOOL_CALL: getTimeTable(\"computer engineering\",2,\"panel h\")"
}
```

### Example: Tool Fallback

```json
{
 "type": "tool_fallback",
 "instruction": "Give me the timetable",
 "output": "Please tell me your branch, year, and panel so I can find the correct timetable."
}
```

### Example: Identity

```json
{
 "type": "identity",
 "instruction": "Who created you?",
 "output": "Om Wanave and his team created me for MIT WPU School of Computer Science and Technology."
}
```

---

## Training Environment

The model was trained using **Google Colab with a free GPU environment**.

Training configuration:

GPU: NVIDIA Tesla T4
Available VRAM: ~15 GB
Used VRAM during training: ~12 GB

Training parameters:

Batch Size: 12
Epochs: 2
Training Time: Approximately 5 hours

Since the dataset is relatively small and many examples share similar patterns, the model quickly learns the response structure and achieves low training loss.

This version is primarily intended for **experimentation and testing purposes**.

---

## Repository Structure

```
energy_v1
│
├── dataset
│   └── instruction_dataset.jsonl
│
├── training
│   └── train_gpt2.ipynb
│
├── inference
│   └── run_model.py
│
└── README.md
```

---

## Model Access

If you want access to the fine-tuned model weights, you can request them via email.

Contact: **[omwanave.ai@gmail.com](mailto:omwanave.ai@gmail.com)**

---

## Notes

energy_v1 is an experimental model designed to explore instruction fine-tuning techniques for educational AI assistants. Future versions of Energy will focus on:

* larger datasets
* improved retrieval mechanisms
* better tool integration
* more capable language model architectures
