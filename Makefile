# This file is to mostly help me remember the locust api syntax

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo ""
	@echo "--- General Commands ---"
	@echo "                          run migrations against database"

install:
	pip3 install locust

locust:
	locust -f locust_files/hello_world.py



