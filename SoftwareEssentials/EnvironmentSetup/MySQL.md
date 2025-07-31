# MYSQL 
```bash 
  sudo apt install mysql-server -y
  sudo systemctl status mysql
  # if not enabled
  sudo systemctl enable mysql
  # disable 
  sudo systemctl disable mysql 
  # starting mysql service 
  sudo systemctl start mysql 
  # stop ...
  sudo systemctl stop mysql
  # setting root password 
  sudo mysql_secure_installation 
  # for passwords
  ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '..';
  FLUSH PRIVILEGES;
## to switch to faster login 
ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket;
FLUSH PRIVILEGES;
## creating user 
  CREATE USER 'srkamdev'@'localhost' IDENTIFIED BY ..'';
GRANT ALL PRIVILEGES ON *.* TO '...'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
## accessing users 
mysql -u 'name of 'user' -p
## grant priv
GRANT ALL PRIVILEGES ON *.* TO '...'@'localhost' WITH GRANT OPTION;
## revoke
REVOKE ALL PRIVILEGES, GRANT OPTION FROM '...'@'localhost';
## restrict
GRANT ALL PRIVILEGES ON myproject_db.* TO '...'@'localhost';
## show grants
SHOW GRANTS FOR '...'@'localhost';
## check plugin for user 
SELECT user, host, plugin FROM mysql.user;
