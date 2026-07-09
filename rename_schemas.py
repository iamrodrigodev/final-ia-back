import os

REPLACEMENTS = {
    "PerfilEstudiante": "PrediccionPeticion",
    "RespuestaPrediccion": "PrediccionRespuesta"
}

DIRECTORIES = ["app", "tests"]

def replace_in_files():
    for directory in DIRECTORIES:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    modified = False
                    for old, new in REPLACEMENTS.items():
                        if old in content:
                            content = content.replace(old, new)
                            modified = True
                    
                    if modified:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"Modificado: {filepath}")

if __name__ == "__main__":
    replace_in_files()
