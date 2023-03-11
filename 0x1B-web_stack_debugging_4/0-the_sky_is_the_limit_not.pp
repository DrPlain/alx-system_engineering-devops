# Manifest to fix nginx limit: increases max file descriptors for our server

exec { 'fix_limit':
    command => 'sed -i "s/ULIMIT.*/ULIMIT=\"-n 2000\"/" /etc/default/nginx',
    path    => '/bin',
}

service { 'nginx':
    ensure    => 'running',
    subscribe => Exec['fix_limit'],
}
