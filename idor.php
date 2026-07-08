<?php
// vulnerable.php
// Educational IDOR example — DO NOT DEPLOY IN PRODUCTION.
// Usage (lab only): /vulnerable.php?user_id=123

session_start();

// $pdo must be a valid PDO connection to your database (e.g., MySQL / SQLite)
// Here we assume a PDO connection is already initialized.
$pdo = new PDO('mysql:host=localhost;dbname=lab','user','pass', [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION
]);

// Value supplied by the user (URL/query)
$userId = isset($_GET['user_id']) ? intval($_GET['user_id']) : 0;

// No authorization check: the provided ID is used directly
$stmt = $pdo->prepare('SELECT id, username, email FROM users WHERE id = ?');
$stmt->execute([$userId]);
$user = $stmt->fetch(PDO::FETCH_ASSOC);

if (!$user) {
    http_response_code(404);
    echo "Utilisateur introuvable";
    exit;
}

// Expose sensitive data without access verification
header('Content-Type: application/json');
echo json_encode($user);
