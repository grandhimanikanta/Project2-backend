from django.db import models

class canditates(models.Model):
    date=models.DateTimeField()
    canditate_name=models.CharField(max_length=20,null=True,blank=True,default=None)
    phone_number=models.IntegerField(null=True,blank=True,default=None)
    email_address=models.EmailField(primary_key=True)
    experience=models.CharField(max_length=20,null=True,blank=True,default=None)
    domain=models.CharField(max_length=20,null=True,blank=True,default=None)
    current_ctc=models.CharField(max_length=10,null=True,blank=True,default=None)
    expected_ctc=models.CharField(max_length=10,null=True,blank=True,default=None)
    notice_period=models.CharField(max_length=10,null=True,blank=True,default=None)
    role_id = models.IntegerField()

class role_table(models.Model):
    role_id=models.AutoField(primary_key=True,blank=True,default=None)
    role_name=models.CharField(max_length=20,null=True,blank=True,default=None)
    rounds=models.IntegerField(null=True,blank=True,default=None)
    round_details=models.CharField(max_length=50,null=True,blank=True,default=None)
    # def __str__(self):
    #     return self.role_id,self.role_name,self.rounds

class rounds_table(models.Model):
    role_id=models.ForeignKey(role_table,on_delete=models.CASCADE)
    email_address=models.ForeignKey(canditates,on_delete=models.CASCADE)
    present_round=models.IntegerField(blank=True,default=None)
    status_application=models.CharField(max_length=20,blank=True,default=None)
    feedback=models.CharField(max_length=20,blank=True,default=None)

