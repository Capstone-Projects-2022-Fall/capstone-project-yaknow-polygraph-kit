<?php
    error_reporting(0);
    $email = $password = "";
    $errors = array('email' => '', 'password' => '');

    $dbServerName = "173.255.232.150";
    $dbUsername = "cis4398";
    $dbPassword = "dNC=IK~9)7";
    $dbName = "Questions";

    $conn = new mysqli($dbServerName, $dbUsername, $dbPassword, $dbName);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    if(isset($_POST['submit'])){
        if(empty($_POST['email'])){
            $errors['email'] =  "An Email Is Required <br />";
        } else {
            $email = $_POST['email'];
            if(!filter_var($email, FILTER_VALIDATE_EMAIL)){
                $errors['email'] = "Email Must Be a Valid Email-Address";
            }
            else {
                $email_query = "SELECT email, password FROM users.user WHERE email = '".$email."'";
                $result = mysqli_query($conn, $email_query);
                $data = mysqli_fetch_all($result, MYSQLI_ASSOC);
                if (empty($data)) {
                    $errors['email'] = "Email Not Found. Try Another Maybe?";
                }
            }
        }
        if(empty($_POST['password'])){
            $errors['password'] = "A Password Is Required <br />";
        } else {
            $email = $_POST['email'];
            $password = $_POST['password'];

            //$fp = fopen('file.csv', 'w');
            //fputcsv($fp, $email);
            //fclose($fp);
            
            $sql = "SELECT email, password FROM users.user WHERE email = '".$email."'";
            $result = mysqli_query($conn, $sql);
            $data = mysqli_fetch_all($result, MYSQLI_ASSOC);

            if ($data[0]['password'] != $password){
                $errors['password'] = "Wrong Password Entered. Try Again.";
            }
            else {
                header('Location: info.php');
            }
            
        }
        
    }
    
?>

<!DOCTYPE html>
<html lang="en">
    <?php include('templates/header.php') ?>

    <section class="container grey-text">
        <h4 class="center">Provide User Information</h4>
        <form action="get.php" method="POST" class="white">
            <label for="">Your Email</label>
            <input type="text" name="email" value="">
            <div class="red-text"><?php echo $errors['email']; ?></div>
            <label for="">Your Password</label>
            <input type="password" name="password" value="">
            <div class="red-text"><?php echo $errors['password']; ?></div>
            <div class="center">
                <input type="submit" name="submit" value="submit" class="btn brand z-depth-0">
            </div>
        </form>
    </section>

    <?php include('templates/footer.php') ?>
</html>