# install nginx, configure, redirect and customize 404 message with puppet

exec {'apt update':
    command => 'sudo apt-get update',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }

package {'nginx': ensure    => 'installed'}
package {'ufw': ensure      => 'installed'}

exec {'grant ufw access to http':
    command => 'sudo ufw allow "Nginx Full"',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }

file {'/var/www/html/index.html':
    ensure  => 'present',
    content => 'Hello world!\n',
    }

file {'/var/www/html/custom_404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page\n",
    }

file {'/etc/nginx/sites-enabled/default':
    ensure  => 'present',
    content => "server {
                    listen 80 default_server;
                    listen [::]:80 default_server;
                    root /var/www/html;
                    index index.html;
                    server_name _;
                    location / {
                        try_files \$uri \$uri/ =404;
                    }
                    error_page 404 /custom_404.html;
                    location /custom_404.html {
                        internal;
                    }
                    location ~ /redirect_me {
                        return 301 /www.google.com;
                    }
                }",
        }

exec {'Restart nginx':
    command => 'service nginx restart',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    }
