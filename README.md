# Recruit-a-thon-backend
Hackton
<br>
Live URL : https://recrtuit-a-thon.herokuapp.com/ <br>
<br>
====================================
<br>
/user/login/  <br>
POST <br>
  body:<br>
  {<br>
	"username" : "manikanta@manikanta.com",<br>
	"password" : "manikanta"<br>
  }<br>
 
 ==============================<br>
  /user/verify_login<br>
  POST<br>
    body:<br>
  {<br>
	"token" : 12345678sdfghgfcvbn <br>
  }
 <br><br>
=======================================<br>
    
  /user/logout<br>
  POST<br>
    body:<br>
  {<br>
	"token" : 12345678sdfghgfcvbn <br>
  }<br>

=======================================<br>

  /roleinfo/<br>
  POST<br>
    body:<br>
  {<br>
	"role_id": <NUMBER> <br>
  }<br>

==============================================<br>

  /roleinfo<br>
  GET<br>

==============================================<br>
  /editrole/<br>
  POST<br>
    body:<br>
  {<br>
	"role_id": <NUMBER>, <br>
	"role_name": <NAME>, <br>
	"rounds: [<br>
	<ROUND_NAME>,<br>
	<ROUND_NAME>,<br>
	<ROUND_NAME>,<br>
	] <br>
  }<br>

==============================================<br>
