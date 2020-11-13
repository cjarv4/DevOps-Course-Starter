build: ## build the image
	docker build --target development --tag todo-app:dev .
	docker build --target production --tag todo-app:prod .

dev_server: ## build the container
	docker run -it --rm --name=todo -p 80:5000  \
	--env-file todo_files/.env \
	--env FLASK_ENV=development \
	-v "`pwd`/todo_files:/app/todo_files" \
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