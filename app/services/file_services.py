import os
import json
from typing import Dict, Any

class FileService:
    def __init__(self, filepath:str = "db.json"):
        self.filepath = filepath
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding='utf-8') as file:
                json.dump({}, file, indent=4)
    
    def read(self) -> Dict[str, Any]:
        try:
            print(self.filepath)
            with open(self.filepath, "r", encoding='utf-8') as file:
                  return json.load(file)
        except FileNotFoundError as error:
            print(error)
        except Exception as error:
            print(error)
        
    def write(self, txt: str):
        try:
            print(self.filepath)
            with open(self.filepath, "w") as file:
                file.write(f'{{"value": "{txt}"}}')
        except FileNotFoundError as error:
            print(error)
        except Exception as error:
            print(error)

