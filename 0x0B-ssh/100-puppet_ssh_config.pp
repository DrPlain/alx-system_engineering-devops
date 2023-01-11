# Make changes in ~/.ssh/config file using puppet
include stdlib

file_line {'no_password':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
}

file_line {'IdentityFile':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school',
}
