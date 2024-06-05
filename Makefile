
all: venv bot

venv:
	./setup_venv.sh

unzip:
	./unzip_data_files.sh ${ZIP_DIR} ${DATA_DIR}

bot:
	( . .venv/bin/activate && \
	./main.py )

run: bot

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache


