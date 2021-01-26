build: ## build the image
	docker build --target development --tag todo-app:dev .
	docker build --target production --tag todo-app:prod .

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

kill: ## kill the container
	docker kill todo

shell: ## Connect shell to a running container
	docker exec -it todo /bin/bash

logs: ## Connect shell to a running container
	docker logs todo