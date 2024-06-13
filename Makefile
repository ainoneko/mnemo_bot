
all: venv bot

venv:
	test -d .venv || ./setup_venv.sh

unzip:
	./unzip_data_files.sh ${ZIP_DIR} ${DATA_DIR}

bot: venv
	( . .venv/bin/activate && \
	./main.py )

run: bot

docker:
	echo "Not implemented"

clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache


