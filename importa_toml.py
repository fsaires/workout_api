import toml

# Carregar o pyproject.toml
with open('pyproject.toml', 'r') as f:
    pyproject = toml.load(f)

# Ler o requirements.txt
with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

# Adicionar dependências ao pyproject.toml
for req in requirements:
    package, version = req.strip().split('==')
    pyproject['tool']['poetry']['dependencies'][package] = version

# Escrever de volta ao pyproject.toml
with open('pyproject.toml', 'w') as f:
    toml.dump(pyproject, f)

print("Dependências adicionadas ao pyproject.toml")
