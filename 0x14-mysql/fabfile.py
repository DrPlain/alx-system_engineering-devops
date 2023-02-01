from fabric.api import sudo, put, env

def connect():
	env.hosts = ['ubuntu@100.26.233.107', 'ubuntu@18.204.8.41']

def install_mySQL():
	put('signature.key')
	sudo('sudo apt-key add signature.key')
	sudo('sh -c \'echo "deb http://repo.mysql.com/apt/ubuntu bionic mysql-5.7" >> /etc/apt/sources.list.d/mysql.list\'')
	sudo('apt-get update -y')
	sudo('apt install -f mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*')
