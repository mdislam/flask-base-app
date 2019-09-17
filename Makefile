# for local development
.PHONY: run_unit_tests build-n-deploy build-orcus deploy-orcus

run-unit-tests:
	docker exec -it  blueprint_webapp_1 python tests/test_base.py --verbose

build-n-deploy:
	make build-orcus
	make deploy-orcus

build-orcus:
	docker-compose build

deploy-orcus:
	docker-compose up -d --remove-orphans --force-recreate
