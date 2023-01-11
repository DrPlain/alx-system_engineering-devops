exec {'Terminated killmenow':
    command  => 'pkill killmenow',
    provider => 'shell',
}
