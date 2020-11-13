build: ## build the image
	docker build --tag todo-app .

dev_server: ## build the container
	docker run -it --rm --name=todo -p 80:5000  \
	--env TRELLO_KEY=d3cfc4a193b13c194d0ca2484808d1f2 \
	--env TRELLO_TOKEN=0ee7c15267a7a7fee3f90ebed124aa5e14652888ce7fc40b444ab7b9ebcbd019 \
	--env FLASK_ENV=development \
	-d todo-app

server: ## build the container
	docker run -it --rm --name=todo -p 80:5000  \
	--env TRELLO_KEY=d3cfc4a193b13c194d0ca2484808d1f2 \
	--env TRELLO_TOKEN=0ee7c15267a7a7fee3f90ebed124aa5e14652888ce7fc40b444ab7b9ebcbd019 \
	-d todo-app

kill: ## kill the container
	docker kill todo

shell: ## Connect shell to a running container
	docker exec -it todo /bin/bash

logs: ## Connect shell to a running container
	docker logs todo