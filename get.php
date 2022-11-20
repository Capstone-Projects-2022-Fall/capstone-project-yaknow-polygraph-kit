<?php

$email = $password = "";
$errors = array('email' => '', 'password' => '');

    if(isset($_POST['submit'])){
        if(empty($_POST['email'])){
            $errors['email'] =  "An Email Is Required <br />";
        } else {
            $email = $_POST['email'];
            if(!filter_var($email, FILTER_VALIDATE_EMAIL)){
                $errors['email'] = "Email Must Be a Valid Email-Address";
            }
        }
        if(empty($_POST['password'])){
            $errors['password'] = "A Password Is Required <br />";
        } else {
            $password = $_POST['password'];
        }
    }

    if(array_filter($errors)){
        //echo "There are Errors in the Form";
    } else {
        header('Location: index.php');
    }

?>

<!DOCTYPE html>
<html lang="en">
    <?php include('templates/header.php') ?>

    <section class="container grey-text">
        <h4 class="center">Provide User Information</h4>
        <form action="get.php" method="POST" class="white">
            <label for="">Your Email</label>
            <input type="text" name="email" value="<?php echo $email?>">
            <div class="red-text"><?php echo $errors['email']; ?></div>
            <label for="">Your Password</label>
            <input type="text" name="password" value="<?php echo $password?>">
            <div class="red-text"><?php echo $errors['password']; ?></div>
            <div class="center">
                <input type="submit" name="submit" value="submit" class="btn brand z-depth-0">
            </div>
        </form>
    </section>

    <?php include('templates/footer.php') ?>
</html>