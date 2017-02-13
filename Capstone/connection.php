<?php
/**
 * Created by PhpStorm.
 * User: Kieran
 * Date: 2/12/2017
 * Time: 11:02 PM
 */

$servername = "localhost";
$username = "Administrator";
$password = "MsuFcu24570";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

$sql = "SELECT * FROM msufcu.alexa";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}


$request = True;

if ($request){
    $sql = "SELECT intentName, jsonResponse FROM msufcu.alexa";
    $result = $conn->query($sql);
    if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            echo " Intent: " . $row["intentName"]. " - JSON: " . $row["jsonResponse"];
        }
    } else {
        echo "0 results";
    }
}

$ex_json = '{
  "session": {
    "sessionId": "SessionId.2395edf9-ffbb-4da0-b0b1-db3c330e6ce4",
    "application": {
      "applicationId": "amzn1.ask.skill.5ba5cf73-de24-41a3-942d-373af2db725a"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AFCR3OTEXT45SC7KAV6ZYKBEDRRD72WDPSBSGQIMEAAENZO7EZ4CNI3CPF4TLQK23CDYP6BFYA7SNN75EMUXCW65S6UXVUEQ7ZMWABA4N5UJNEKYCZBSGCJTB66F4H7FJ3GVE6WCD76K6ESZCECHW232GHOPSDHVZPT2NDZYPYFXXER6YFZEY52X7ST2CA53ICXBZ6GJLXH75CQ"
    },
    "new": true
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.19c2d7b2-9129-467e-9aea-f5d473a37200",
    "locale": "en-US",
    "timestamp": "2017-02-08T15:12:44Z",
    "intent": {
      "name": "HoursIntent",
      "slots": {}
    }
  },
  "version": "1.0"
}';

#echo var_dump(json_decode($ex_json, true));
$obj = json_decode($ex_json, true);
$key1 = "request";
$key2 = "intent";
$key3 = "name";

if (array_key_exists($key1, $obj)){
    #echo "ITS IN THERE";
}
#echo $obj[$key1][$key2][$key3];
#print var_dump($obj->{'session'});
#$obj = $obj{'request'};
#echo var_dump($obj{'request'});

$intent_name = $obj[$key1][$key2][$key3];

function alexa_intent ($intent_name){
    if ($intent_name == "HoursIntent"){
       return $intent_name;
    }
    else{
        echo "Intent not recognized";
    }
}

function get_sql($call_type){
    if($call_type == "HoursIntent"){
        $sql = "SELECT * FROM msufcu.users";
    }
    else{
        $sql = "";
    }
    return $sql;
}

$intent = alexa_intent($intent_name);
$sql = get_sql($intent);




$conn->close();



