# DRG-Doc-QA

**Framework for Externalized Graph-Based Reasoning for Faithful Multilingual Question Answering over Documents**

---

## 📌 Overview

This project implements a **Document Reasoning Graph (DRG)** framework for faithful document question answering.
Instead of letting an LLM reason internally (which often causes hallucinations), reasoning is **externalized into an explicit graph** built from the document.

Pipeline:

```
PDF → sentence nodes → graph (DRG)
     → query grounding → graph reasoning
     → evidence nodes → answer generation
```

The system is designed for:

* rule-heavy documents (policies, manuals, guidelines)
* interpretable reasoning
* multilingual / paraphrased queries
* faithful answers grounded in document text

---

## 🧠 Key Idea

Large Language Models often:

* hallucinate
* ignore exceptions
* miss constraints

We fix this by:

1. Converting the document into a graph
2. Running reasoning on the graph
3. Sending only verified evidence to the LLM

So the LLM **writes the answer** but does **not perform reasoning**.

---

## 🏗 Project Structure

```
inlp_project/
│
├── parser/
│   ├── pdf_parser.py          # PDF → text
│   ├── sentence_splitter.py   # text → sentences
│   ├── section_utils.py       # detect sections
│   ├── drg_nodes.py           # build nodes
│   ├── drg_graph.py           # build graph
│   └── reasoning_engine.py    # graph reasoning
│
├── test_reasoning.py          # example run script
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone repo

```bash
git clone https://github.com/GauravPatel369/graph-based-qa.git
cd graph-based-qa
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Download NLTK tokenizer

Run once:

```python
import nltk
nltk.download("punkt")
nltk.download("punkt_tab")
```

---

## ▶️ How to Run

### Step 1 — Place PDF

Put your document in project folder:

```
sample.pdf
```

### Step 2 — Edit test file

Open:

```
test_reasoning.py
```

Set path:

```python
pdf_path = "sample.pdf"
query = "When is the deadline?"
```

### Step 3 — Run system

```bash
python test_reasoning.py
```

---

## 🧪 Example Output

```
FLAT
[0] Deadline: 5 March 2026, 11:59pm
[4] No extensions will be granted...

STRUCTURAL
...more context...

EMERGENT
[0] Deadline: 5 March 2026, 11:59pm
[4] No extensions will be granted...
```

These are the **evidence sentences** selected by graph reasoning.

---

## 🧩 Modules Explained

### 📄 PDF Parser

Extracts text page-wise.

### 🔹 Node Builder

Each sentence becomes a node with:

```
node_id
text
page
section
```

### 🔗 Graph Builder

Edges added:

* same page
* same section
* adjacent sentences
* semantic similarity

### 🧠 Reasoning Engine

Implements 3 strategies:

| Method     | Description           |
| ---------- | --------------------- |
| Flat       | embedding retrieval   |
| Structural | neighbor expansion    |
| Emergent   | graph-based reasoning |

Emergent reasoning is the main contribution.

---

## 🌍 Multilingual Support (Planned)

Future extension:

* Hinglish queries
* translation grounding
* multilingual embeddings

---

## 📊 Evaluation Plan

We compare:

* LLM-only baseline
* flat retrieval
* structural graph
* emergent reasoning

Metrics:

* faithfulness
* exception handling
* robustness to paraphrase
* interpretability

---

## 🚀 Example Query

```
Query: When is the assignment deadline?
```

System:

1. finds relevant nodes
2. expands graph
3. selects evidence
4. generates answer

---

## 🧱 Tech Stack

* Python
* NetworkX
* Sentence-Transformers
* PyMuPDF
* NLTK

---

## 📌 Future Work

* LLM answer generation
* reasoning visualization
* multilingual grounding
* UI demo (Streamlit)
* evaluation benchmark

---

## 👨‍💻 Team

**CTRL+ALT+DLT**

---

## 📜 License

MIT License
