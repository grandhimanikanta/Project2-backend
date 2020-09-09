# Recruit-a-thon-backend
Hackton
<br>
Live URL : https://recrtuit-a-thon.herokuapp.com/ <br>
<br>

<h2 id="userlogin">/user/login/</h2>
<h3 id="post">POST</h3>
<p><strong>body</strong></p>
<blockquote>
<p>{<br>
“username” : <a href="mailto:%22manikanta@manikanta.com">"manikanta@manikanta.com</a>",<br>
“password” : “manikanta”<br>
}`</p>
</blockquote>
<h2 id="userverify_login">/user/verify_login</h2>
<h3 id="post-1">POST</h3>
<p><strong>body</strong></p>
<blockquote>
<p>{<br>
“token” : 12345678sdfghgfcvbn<br>
}</p>
</blockquote>
<h2 id="userlogout">/user/logout</h2>
<h3 id="post-2">POST</h3>
<p><strong>body</strong></p>
<blockquote>
<p>{<br>
“token” : 12345678sdfghgfcvbn<br>
}</p>
</blockquote>
<h4 id="get-particular-role-info-with-role-id">Get particular role info with role id</h4>
<h2 id="roleinfo">/roleinfo/</h2>
<h3 id="post-3">POST</h3>
<p><strong>body</strong></p>
<blockquote>
<p>{<br>
“role_id”: 1<br>
}</p>
</blockquote>
<h4 id="get-all-roles-info">Get all Roles info</h4>
<h2 id="roleinfo-1">/roleinfo</h2>
<h3 id="get">GET</h3>
<h4 id="create-role-and-update-role">Create role and update role:</h4>
<h5 id="update-role-needs-role_id-in-body">Update role needs “role_id” in body</h5>
<h2 id="editrole">/editrole/</h2>
<h3 id="post-4">POST</h3>
<p><strong>body</strong></p>
<blockquote>
<p>{<br>
“role_id”: 1,(optional)<br>
“role_name”: “HR”,<br>
"rounds: [<br>
&lt;ROUND_NAME&gt;,<br>
&lt;ROUND_NAME&gt;,<br>
&lt;ROUND_NAME&gt;,<br>
]<br>
}</p>
</blockquote>

