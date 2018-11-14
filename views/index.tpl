<!DOCTYPE html>
<html lang="is">
<head>
	<link rel="stylesheet" type="text/css" media="screen" href="/static/css2.css" />
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta http-equiv="X-UA-Compatible" content="ie=edge">
	<title>Verkefni 7.</title>
	
	<script src="main.js"></script>
</head>

<body>
	<h3>Nýskráningarform:</h3>
	<form method="POST" action="/donyskra" accept-charset="IOS-8859-1" id="ny">
		Notendanafn:<br>
		<input type="text" name="user" required><br>
		Lykilorð:<br>
		<input type="text" name="pass" required><br>
		Nafn:<br>
		<input type="text" name="nafn" required><br>
		<input type="submit" value="Nýskrá">
		<input type="reset" value="Hreinsa">
	</form>
	<hr>
	<h3>Innskráningarform:</h3>
	<form method="POST" action="/doinnskra" accept-charset="IOS-8859-1" id="inn">
		Notendanafn:<br>
		<input type="text" name="user" required><br>
		Lykilorð:<br>
		<input type="text" name="pass" required><br>
		<input type="submit" value="Innskrá">
	</form>
</body>
</html>

