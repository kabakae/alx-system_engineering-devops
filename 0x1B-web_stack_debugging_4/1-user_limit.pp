#Enable the user holberton to login

# increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
# increases soft file limit for Holberton user.
exec {'increases-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
