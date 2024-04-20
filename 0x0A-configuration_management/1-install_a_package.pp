"script to install flask using pip3"
$base_packages = {'python-pip', 'python-devel', 'openssl-devel', 'libffi-devel'}

$package_dependencies = concatenate($base_packages, 'pip3')


package{$base_packages:
  ensure    =>  'installed'
}

package{'pip3':
  ensure   =>  latest,
  require  =>  Package[$base_packages],
  provider =>  'pip3',
}

package {'flask':
  ensure   =>  installed,
  require  =>  Package[$package_dependencies],
  name     =>  'flask~=2.1.0',
  provider =>  'pip3',
}
