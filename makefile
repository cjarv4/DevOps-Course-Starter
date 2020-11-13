build: ## build the image
	docker build --tag todo-app .

server: ## build the container
	docker run -it --rm --name=todo -p 80:5000 -d todo-app

kill: ## kill the container
	docker kill todo

shell: ## Connect shell to a running container
	docker exec -it todo /bin/bash