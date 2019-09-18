# for local development
.PHONY: run_unit_tests \
	build-n-deploy-local \
	build-images \
	push-images \
	deploy-local

run-unit-tests:
	docker exec -it  blueprint_webapp_1 python tests/test_base.py --verbose

build-n-deploy-local:
	docker-compose build
	make deploy-local

build-images:
	docker build -t $(KIT_REGISTRY)/$(AWS_DEFAULT_ECR):blueprint_webapp -f webapp/Dockerfile webapp
	docker build -t $(KIT_REGISTRY)/$(AWS_DEFAULT_ECR):blueprint_proxy -f proxy/Dockerfile proxy

push-images:
	docker push $(KIT_REGISTRY)/$(AWS_DEFAULT_ECR):blueprint_webapp
	docker push $(KIT_REGISTRY)/$(AWS_DEFAULT_ECR):blueprint_proxy

deploy-local:
	docker-compose up -d --remove-orphans --force-recreate
