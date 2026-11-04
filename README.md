Primero creen un entorno virtual.

Si están en WSL:
```bash
python3 -m venv .venv
```

Y después, actívenlo:
```bash
source .venv/bin/activate
```

Y después, instalamos las librerías:
```bash
pip install -r requirements.txt
```

Y por último exporten su clave de Gemini API key:
```bash
export GEMINI_API_KEY="xxxxxSU_CLAVExxxxx"
```
