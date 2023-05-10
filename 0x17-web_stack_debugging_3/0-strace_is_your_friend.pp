# pp manifests that automates the fixing Apache returning a 500 error

exec { 'fixed php error on Apache':
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  provider => shell,
}
