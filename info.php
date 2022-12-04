<?php

    //$email = $_POST['email'];

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

//     $sql = "SELECT exmaID, tsStamp, pulse, skin_conductivity,
// respiration_belt, blood_pressure FROM Questions.SingularRecording where exmaID = 9";
    //$max = "SELECT MAX(exmaID) FROM Questions.SingularRecording";
    //$sql = "SELECT tsStamp, respiration_belt, blood_pressure, skin_conductivity, pulse FROM Questions.SingularRecording WHERE exmaID = 75";

    $sql = "SELECT tsStamp, respiration_belt, blood_pressure, skin_conductivity, pulse, exmaID FROM Questions.SingularRecording WHERE exmaID = (SELECT MAX(exmaID) FROM Questions.SingularRecording)";

    // $sql = "SELECT Questions.SingularRecording.exmaID,Questions.SingularRecording.tsStamp,Questions.SingularRecording.skin_conductivity,Questions.SingularRecording.respiration_belt,Questions.SingularRecording.blood_pressure,users.user.email
    // from Questions.SingularRecording Inner join users.user
    // ON Questions.SingularRecording.exmaID=users.user.id";

    $result = mysqli_query($conn, $sql);
    $users = mysqli_fetch_all($result, MYSQLI_ASSOC);

    $rowcount = mysqli_fetch_assoc($result);
    print_r($rowcount);

    if ( ! $result ) {
        echo mysql_error();
        die;
    }

    $data = array();
    $counter = 0;

    $data[0] = ["tsStamp", "respiration_belt", "blood_pressure", "skin_conductivity", "pulse", "exmaID"];

    for ($x = 1; $x < mysqli_num_rows($result); $x++) {
        $counter = $counter + 1;
        $data[] = $users[$x];
    }

    $fp = fopen('dataCSV.csv', 'w');

    foreach ($data as $fields) {
        fputcsv($fp, $fields);
    }

    fclose($fp);

    // $json = json_encode($data);

    // if (file_put_contents("data.json", $json))
    //     echo "JSON file created successfully...";
    // else 
    //     echo "Oops! Error creating json file...";

    //print_r($counter);

    //print_r($result);

    //print_r($users[0]);

    // require('get.php');
    // echo $email;

    //echo json_encode($data);

    //json_encode($data);
    
?>
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Graph Result</title>
        <link rel="stylesheet" type="text/css" href="style.css">
        <script type="text/javascript" src="https://d3js.org/d3.v4.js"></script>
    </head>
    <body>
        <script type="text/javascript" src="multipleGraphs.js"></script>
    </body>
</html>

