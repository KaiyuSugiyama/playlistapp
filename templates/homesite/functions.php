<?php

$username = $_POST['username'];
$password = $_POST['password'];
if (!empty($username) || !empty($password){
$dir = 'homesite/Users.db';
$dataToStore = "INSERT INTO users (username, password) VALUES ('$username', '$password');"
file_put_contents($dir, $dataToStore);
}