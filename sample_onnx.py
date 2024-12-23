import onnxruntime as ort
import numpy as np
import torch

# Load the ONNX model
model_path = "model.onnx"
session = ort.InferenceSession(model_path, providers=["CPUExecutionProvider"])

# Tokenizer placeholder (replace with actual tokenizer)
def tokenize_input(text):
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("gemma2-2b")
    tokens = tokenizer(text, return_tensors="np", padding=True, truncation=True, max_length=512)
    return tokens["input_ids"]

# Preprocessing
input_text = "This is a test input for Gemma-2 2B."
tokens = tokenize_input(input_text)

# Prepare input
inputs = {session.get_inputs()[0].name: tokens}

# Run inference
outputs = session.run(None, inputs)

# Postprocessing (example)
def decode_output(output):
    from transformers import AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained("gemma2-2b")
    decoded_text = tokenizer.decode(np.argmax(output, axis=-1).squeeze(), skip_special_tokens=True)
    return decoded_text

result = decode_output(outputs[0])
print(f"Model Output: {result}")