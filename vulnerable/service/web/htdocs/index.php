<?php
session_start();
if (isset($_SESSION['errors'])) {
    $errors = $_SESSION['errors'];
}
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
<div class="m-auto">
    <div class="card">
        <div class="card-header">Iniciar sesión</div>

        <div class="card-body">
            <form method="POST" action="login.php">
                <div class="row mb-3">
                    <label for="email" class="col-md-4 col-form-label text-md-end">Email</label>
                    <div class="col-md-8">
                        <input id="email" type="email"
                               class="form-control <?php echo isset($errors['email']) ? 'invalid' : '' ?>" name="email"
                               required autocomplete="email"
                               autofocus>
                        <?php if (isset($errors['email'])) : ?>
                            <span class="invalid-feedback d-inline" role="alert">
                                <strong><?php echo $errors['email'] ?></strong>
                            </span>
                        <?php endif; ?>
                    </div>
                </div>
                <div class="row mb-3">
                    <label for="password" class="col-md-4 col-form-label text-md-end">Contraseña</label>
                    <div class="col-md-8">
                        <input id="password" type="password"
                               class="form-control" name="password" required autocomplete="current-password">
                        <?php if (isset($errors['password'])) : ?>
                            <span class="invalid-feedback d-inline" role="alert">
                                <strong><?php echo $errors['password'] ?></strong>
                            </span>
                        <?php endif; ?>
                    </div>
                </div>
                <div class="row mb-0">
                    <div class="col-md-8 offset-md-4">
                        <button type="submit" class="btn btn-primary">Iniciar sesión</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
<script src="bootstrap/js/bootstrap.bundle.min.js"></script>
</body>
</html>
<?php
session_destroy();
?>
