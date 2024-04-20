#script to install flask using pip3

package{'python3-pip':
  ensure => installed,
}

package {'Flask':
  ensure   =>  '2.1.0',
  provider =>  'pip3',
  require  =>  Package['python3-pip'],
}
