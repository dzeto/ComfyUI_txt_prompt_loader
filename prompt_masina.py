import os

class TxtFolderIndexer:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "folder_path": ("STRING", {"default": ""}),
                "index": ("INT", {
                    "default": 0, 
                    "min": 0, 
                    "max": 0xffffffffffffffff, 
                    "step": 1,
                    # This line adds the "fixed/increment/randomize" options
                    "control_after_generate": True 
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "read_text"
    CATEGORY = "CustomNodes/PromptHelpers"

    def read_text(self, folder_path, index):
        if not os.path.isdir(folder_path):
            return (f"Error: Folder path '{folder_path}' does not exist.",)

        # Get list of .txt files and sort them alphabetically
        files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt")])

        if not files:
            return ("Error: No .txt files found in folder.",)

        # Use modulo to wrap around if index exceeds file count
        actual_index = index % len(files)
        file_path = os.path.join(folder_path, files[actual_index])

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            return (content,)
        except Exception as e:
            return (f"Error reading file: {str(e)}",)

NODE_CLASS_MAPPINGS = {
    "TxtFolderIndexer": TxtFolderIndexer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TxtFolderIndexer": "Text Folder Indexer"
}
