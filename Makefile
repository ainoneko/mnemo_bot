
BOT_NAME=neko_mnemo_bot

all: venv unzip config bot

venv:
	test -d .venv || ./setup_venv.sh

unzip:
	./unzip_data_files.sh ${ZIP_DIR} ${DATA_DIR}

config:
	test -d config.yml || echo "Add the 'config.yml' file (see config_SAMPLE.yml for reference)"

bot: venv
	( . .venv/bin/activate && \
	./main.py )

run: bot


docker_build:
	@echo Build the docker image
	docker build -t $(BOT_NAME) .

docker_run:
	@echo Run the docker image, as daemon
	docker run -d $(BOT_NAME)

docker: docker_build docker_run


clean:
	rm -rf .venv
	rm -rf __pycache__
	rm -rf .pytest_cache


