.PHONY: setup/

setup: venv/bin/activate ## Project setup
  . venv/bin/activate; pip install --upgrade pip
  . venv/bin/activate; pip install -r requirements.txt





