build: ## build the image
	docker build --target development --tag todo-app:dev .
	docker build --target production --tag todo-app:prod .
	docker build --target test --tag todo-app:test .

dev_server: ## build the container
	docker run -it --rm --name=todo -p 80:5000  \
	--env-file todo_files/.env \
	--env FLASK_ENV=development \
	--mount type=bind,source=`pwd`/todo_files,target=/app/todo_files/ \
	-d todo-app:dev

server: ## build the container
	docker run -it --rm --name=todo -p 80:5000  \
	--env-file todo_files/.env \
	--env FLASK_ENV=production \
	-d todo-app:prod

test: ## kill the container
	docker run -it --rm --name=todo_test \
	--env-file todo_files/.env \
	--env FLASK_ENV=test \
	--mount type=bind,source=`pwd`/todo_files,target=/app/todo_files/ \
	todo-app:test tests/unit_test.py tests/integration_test.py

kill: ## kill the container
	docker kill todo
	
killtest: ## kill the container
	docker kill todo_test

shell: ## Connect shell to a running container
	docker exec -it todo /bin/bash

logs: ## Connect shell to a running container
	docker logs todo