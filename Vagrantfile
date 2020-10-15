Vagrant.configure("2") do |config|
config.vm.box = "hashicorp/bionic64"
    config.vm.network :forwarded_port, guest: 5000, host: 5000

    config.vm.provision "shell", privileged: false, inline: <<-SHELL
        sudo apt-get update

        # TODO: Install pyenv prerequisites
        sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
        libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
        xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
        
        # TODO: Install pyenv
        git clone https://github.com/pyenv/pyenv.git ~/.pyenv

        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
        echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile

        echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
        echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile

        echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile
        echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.profile

        echo Finished pyenv install
    SHELL

    config.vm.provision "shell", privileged: false, inline: <<-SHELL

        #install python3 3.8.3
        pyenv install 3.8.3
        pyenv global 3.8.3

        #install poetry
        curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
    SHELL

    config.trigger.after :up do |trigger|
        trigger.name = "Launching App"
        trigger.info = "Running the TODO app setup script"
        trigger.run_remote = {privileged: false, inline: "
            # Install dependencies and launch
            cd /vagrant
            poetry install
            cd todo_files
            poetry run flask run --host 0.0.0.0
        "}
    end
end
