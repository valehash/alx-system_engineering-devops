# fixing  the phpp in wp-settings

file { 'var/www/html/wp-settings.php'
  ensure  => present
}

file_line {'replace_phpp_with_php':
  path    => '/var/www/html/wp-settings.php',
  line    => '.phpp',
  replace => '.php',
}
