# Changes the OS config for eay login

exec { 'set better config':
  command => 'sudo sed -i "s/nofile 5/nofile 50000/; s/nofile 4/nofile 40000/" /etc/security/limits.conf && sudo sysctl -w fs.file-max=100000 && sudo sysctl -p',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
}

