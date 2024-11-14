<?php
session_start();
?>
<!doctype html>
<html lang="es">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Vulnerable</title>
    <link href="bootstrap/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="d-flex vh-100">
<div class="m-auto text-center">
    <h1>Bienvenid@!</h1>
    <?php if (isset($_SESSION["logged_in"])) : ?>
        <div class="alert alert-success">FLAG</div>
    <?php endif; ?>
</div>
<script src="bootstrap/js/bootstrap.bundle.min.js"></script>
</body>
</html>
<?php
session_destroy();
?>
