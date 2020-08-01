
<?php
	$rawData = $_POST['imgBase64'];
	$filteredData = explode(',', $rawData);
	$unencoded = base64_decode($filteredData[1]);
	$fp = fopen('picture.png', 'w+');
	fwrite($fp, $unencoded);
	fclose($fp);
	$command = escapeshellcmd('python3 projet.py');
	$output = exec($command);
	echo $output;
?>