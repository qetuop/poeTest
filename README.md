# poeTest
```
git clone https://github.com/qetuop/poeTest.git poeData
cd poed
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
```cp config.json.default config.json```

edit config.json

set module paths ex: (in bash)
```export PYTHONPATH=$PYTHONPATH:$HOME/PycharmProjects/poeQuery```

```python3 poeTest.py``` 

in webbrowser goto: http://127.0.0.1:5000/
