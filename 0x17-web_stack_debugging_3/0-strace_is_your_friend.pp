# This manifest fixes permissions, disables .htaccess if not needed, and ensures PHP is installed

# Fix permissions
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

# Remove .htaccess if not needed
file { '/var/www/html/.htaccess':
  ensure  => absent,
}

# Ensure PHP is installed
package { 'php5':
  ensure => installed,
}

# Create PHP configuration directory
file { '/etc/php5/apache2':
  ensure  => directory,
  owner   => 'root',
  group   => 'root',
  mode    => '0755',
  require => Package['php5'],
}

# Configure PHP settings
file { '/etc/php5/apache2/php.ini':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => "
    ; Basic PHP settings for error reporting
    display_errors = On
    log_errors = On
    error_log = /var/log/php_errors.log
  ",
}

# Ensure Apache is running and configured to listen on port 80
$apache_package_name = $::operatingsystem ? {
  'Ubuntu' => 'apache2',
  default  => 'httpd',
}

$apache_service_name = $::operatingsystem ? {
  'Ubuntu' => 'apache2',
  default  => 'httpd',
}

package { $apache_package_name:
  ensure => installed,
}

service { $apache_service_name:
  ensure     => running,
  enable     => true,
  subscribe  => [File['/var/www/html'], Package['php5'], File['/etc/php5/apache2/php.ini']],
  hasrestart => true,
  require    => Package[$apache_package_name],
}
