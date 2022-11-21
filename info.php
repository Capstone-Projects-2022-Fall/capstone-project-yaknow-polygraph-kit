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

    $sql = "SELECT exmaID, tsStamp, pulse, skin_conductivity,
respiration_belt, blood_pressure FROM Questions.SingularRecording where exmaID = 9";
    $result = mysqli_query($conn, $sql);
    $users = mysqli_fetch_all($result, MYSQLI_ASSOC);

    $rowcount = mysqli_fetch_assoc($result);
    print_r($rowcount);

    if ( ! $result ) {
        echo mysql_error();
        die;
    }

    $data = array();

    for ($x = 0; $x < mysqli_num_rows($result); $x++) {
        $data[] = mysqli_fetch_assoc($result);
    }

    //print_r($result);

    //print_r($users);

    echo json_encode($data);

    mysqli_free_result($result);

    mysqli_close($conn);
    
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1> Exam 9 Graphs <h1>
    This is exam 9
</body>
</html>