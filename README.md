# Energy – Educational Large Language Model

Energy is a research project focused on building a Large Language Model (LLM) assistant designed for university environments.

The goal of Energy is to develop an AI system capable of assisting students and faculty with college-related tasks such as academic information, university notices, schedules, and administrative queries.

Unlike general-purpose chatbots, Energy models are trained on structured instruction datasets specifically designed for educational use cases.

---

## Project Goal

The objective of this project is to develop an AI assistant capable of supporting common academic interactions within a university setting. The system is designed to:

* Answer college-related questions
* Understand and respond to university notices and information
* Generate structured tool calls for system integrations
* Handle missing information through intelligent fallback responses
* Maintain a consistent assistant identity

Energy serves as an experimental platform for exploring instruction tuning, tool usage, and retrieval-based responses in academic environments.

---

## Model Versions

This repository contains different versions of the Energy model as the project evolves.

| Version   | Description                                                                           |
| --------- | ------------------------------------------------------------------------------------- |
| energy_v1 | First experimental version fine-tuned on GPT-2 Medium using a 10K instruction dataset |

Each version includes the dataset, training pipeline, and inference examples required to reproduce the model.

---

## Training Data Categories

Energy models are trained using structured instruction datasets composed of multiple categories:

* Identity samples — maintain assistant identity
* General conversation — student interaction and greetings
* RAG examples — answering questions using provided context
* Tool calling — generating structured function calls
* Tool fallback — requesting missing parameters when necessary

This dataset structure allows the model to behave more like a task-oriented assistant rather than a generic chatbot.

---

## Current Architecture

The first version of Energy is built using the following configuration:

Base Model: GPT-2 Medium
Training Method: Instruction Fine-Tuning
Dataset Size: Approximately 10,000 samples
Framework: Hugging Face Transformers

Future versions may explore larger models, improved datasets, and more advanced training strategies.

---

## Repository Structure

```
Energy
│
├── energy_v1
│   │
│   ├── dataset/
│   │   └── instruction_dataset.jsonl
│   │
│   ├── training/
│   │   └── train_gpt2.ipynb
│   │
│   ├── inference/
│   │   └── run_model.py
│   │
│   └── README.md
│
└── README.md
```

---

## Future Development

Planned improvements for the Energy project include:

* Expanding the instruction dataset
* Implementing full Retrieval-Augmented Generation (RAG) pipelines
* Integrating tools with real university systems
* Experimenting with larger and more capable language models
* Improving response reliability and assistant capabilities

---

## Author

Energy is an experimental large language model project focused on AI research and practical educational applications.
