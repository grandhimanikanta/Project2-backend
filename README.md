# Recruit-a-thon-backend
Hackton
<br>
Live URL : https://recrtuit-a-thon.herokuapp.com/ <br>
<br>
====================================
<br>
/user/login/
POST
body

{
“username” : "manikanta@manikanta.com",
“password” : “manikanta”
}

/user/verify_login
POST
body

{
“token” : 12345678sdfghgfcvbn
}

/user/logout
POST
body

{
“token” : 12345678sdfghgfcvbn
}

Get particular role info with role id

/roleinfo/

POST

body
	{
	“role_id”: 1
	}

Get all Roles info

/roleinfo

GET

Create role and update role:

Update role needs “role_id” in body

/editrole/
POST
body

{
	“role_id”: 1,(optional)
	“role_name”: “HR”,
	"rounds: [
	<ROUND_NAME>,
	<ROUND_NAME>,
	<ROUND_NAME>,
	]
}
