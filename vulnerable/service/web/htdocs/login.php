<?php
session_start();

$usuario = "";
if (isset($_POST['email']))
    $usuario = $_POST['email'];

$password = "";
if (isset($_POST['password']))
    $password = $_POST['password'];

$conexion = mysqli_connect("db", "vulnerable", "12345Abcde", "vulnerable");
$query = "select * from users where username='" . $usuario . "' and password=sha1('" . $password . "')";
$resultset = mysqli_query($conexion, $query) or die(mysqli_error($conexion));
$total = mysqli_num_rows($resultset);
mysqli_close($conexion);

if ($total > 0) {
    $_SESSION["logged_in"] = true;
    header("Location: welcome.php");
    die();
} else {
    $errors = [
        'email' => 'Usuario o contraseña incorrectos',
    ];
    $_SESSION["errors"] = $errors;
    header("Location: index.php");
    exit();
}
