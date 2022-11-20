<?php
    //error_reporting(0);
    $dbServerName = "173.255.232.150";
    $dbUsername = "cis4398";
    $dbPassword = "dNC=IK~9)7";
    $dbName = "Questions";

    // create connection
    $conn = new mysqli($dbServerName, $dbUsername, $dbPassword, $dbName);

    // check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } else {
        //echo "Connected successfully";
    }

    $sql = "SELECT * FROM users.user";
    $result = mysqli_query($conn, $sql);
    $users = mysqli_fetch_all($result, MYSQLI_ASSOC);
    //print_r($user);

    mysqli_free_result($result);
    mysqli_close($conn);
    
?>
<!DOCTYPE html>
<html lang="en">
    <?php include('templates/header.php') ?>
    <h4 class="center grey-text">Users</h4>
    <div class="container">
        <div class="row">
            <?php foreach($users as $user) { ?>
                <div class="col s6 md3">
                    <div class="card z-depth-0">
                        <div class="card-content center">
                            <h6><?php echo htmlspecialchars($user['name']); ?></h6>
                            <div><?php echo htmlspecialchars($user['email']); ?></div>
                        </div>
                        <div class="card-action right-align">
                            <a class="brand-text" href="info.php">More Information</a>
                        </div>
                    </div>
                </div>
            <?php } ?>
        </div>
    </div>
    <?php include('templates/footer.php') ?>
</html>
