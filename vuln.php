<?php
// Connexion à la base de données
$db = new mysqli('localhost', 'user', 'pass', 'database');

// Récupération directe des données POST sans filtrage
$username = $_POST['username'];
$password = $_POST['password'];

// Construction dangereuse de la requête
$sql = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = $db->query($sql);

if ($result->num_rows > 0) {
    echo "Connexion réussie !";
} else {
    echo "Identifiants invalides.";
}
?>
