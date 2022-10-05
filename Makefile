include .env
export $(shell sed 's/=.*//' .env)

core-build:
	docker-compose build ia2-core

core-run:
	docker-compose run ia2-core

jupyter-build: core-build
	docker-compose build ia2-jupyter

jupyter-run: jupyter-build
	docker-compose up ia2-jupyter-gpu

jupyter-run-cpu: jupyter-build
	docker-compose up ia2-jupyter-cpu