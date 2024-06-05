# fixing php with puppet

file { '/var/www/html/wp-settings.php':
  ensure => present,
}

exec { 'replace_phpp_with_php':
  command => 'sed -i \'s/\.phpp/\.php/g\' /var/www/html/wp-settings.php',
  onlyif  => 'grep \.phpp /var/www/html/wp-settings.php',
  require => File['/var/www/html/wp-settings.php'],
}

