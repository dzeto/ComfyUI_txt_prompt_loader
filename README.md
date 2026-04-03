# ComfyUI Txt Folder Indexer

A lightweight, high-efficiency custom node for **massive automated prompting** in ComfyUI. 

This node allows you to point to a local folder filled with `.txt` files and automatically cycle through them as prompts for each generation. It is perfect for batch testing models, LoRAs, or complex workflows against hundreds of different prompts without manual intervention.

## 🚀 Key Features
- **Folder-Path Input**: Simply paste the path to your prompts folder.
- **Alphabetical Indexing**: Files are sorted alphabetically to ensure a consistent sequence.
- **Auto-Increment**: Includes native support for ComfyUI's "control_after_generate" (fixed, increment, decrement, randomize).
- **Infinite Looping**: If the index exceeds the number of files, it automatically loops back to the first file.
- **Easy Integration**: Connects directly to any text input (like `CLIP Text Encode`) via the "Convert to Input" feature.

## 🛠️ Installation

1. Navigate to your ComfyUI installation: `ComfyUI/custom_nodes/`
2. Create a folder named `ComfyUI-Txt-Folder-Indexer`.
3. Place the following files inside that folder:
   - `prompt_masina.py` (The main code)
   - `__init__.py` (For ComfyUI to recognize the node)
4. Restart ComfyUI.

### Folder Structure
```text
/ComfyUI/custom_nodes/ComfyUI-Txt-Folder-Indexer/
├── prompt_masina.py
└── __init__.py
