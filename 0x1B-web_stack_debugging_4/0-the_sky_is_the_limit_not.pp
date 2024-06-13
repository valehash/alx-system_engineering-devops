#fixing nginx requests with puppet

file { '/etc/default/nginx':
  ensure => present,
}

exec { 'update_connection_limit':
  command => '/bin/sed -i \'s/ULIMIT="-n [0-9]*"/ULIMIT="-n 10000"/g\' /etc/default/nginx',
  onlyif  => '/bin/grep "24: Too many open files" /var/log/nginx/error.log',
  require => File['/etc/default/nginx'],
}

exec { 'reload_nginx':
  command => '/etc/init.d/nginx restart',
}
