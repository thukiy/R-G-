# R-G-

This project requires a local Python environment and Ollama for model inference.  
Please follow the steps below carefully to ensure a clean and correct setup.

---

## for a clean setup create a new environment
```bash
conda create -n <ENV_NAME> python=<VERSION>
```

## in our case:
```bash
conda create -n math-qa python=3.9
```

## activate your environment:
```bash
conda activate math-qa
```

## install all the mandatory environments
```bash
pip install -r requirements.txt
```

## adapt the paths in file "bm25_retriever.py"
```bash
BASE_DATA_DIR_THE = Path("/Users/.../R-G-/data_processed/")
BASE_DATA_DIR_EXE = Path("/Users/.../R-G-/data_processed/")
```

## for the execution you need ollama installed on your desktop on the official website https://ollama.com/download

## next you need to start ollama in the terminal 
```bash
ollama serve
```

## now you need to pull all the models from ollama which you need (can take some minutes because the models are quite large
```bash
ollama pull deepseek-r1:32b #(this model is mandatory)
ollama pull qwen2.5-vl #(optional for vision)
```

## finally you need to start the app.py file in your terminal 
```bash
streamlit run app.py
```
