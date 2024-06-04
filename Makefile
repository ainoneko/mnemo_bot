
all: venv bot

venv:
	./setup_venv.sh

bot:
	( . .venv/bin/activate && \
	./main.py )

run: bot

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache


