from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    adminemail = models.EmailField(max_length=20, primary_key=True)
    adminpassword = models.CharField(max_length=20)


class ResgisterStudent(models.Model):
     first_name=models.CharField(max_length=40)
     last_name=models.CharField(max_length=40)
     email=models.EmailField(max_length=40)
     rollno=models.IntegerField()
     dob=models.CharField(max_length=10)
     course=models.CharField(max_length=30)
     mark1=models.IntegerField()
     mark2=models.IntegerField()
     mark3=models.IntegerField()
     percentage=models.IntegerField()
     address=models.CharField(max_length=40)
     state=models.CharField(max_length=30)
     city=models.CharField(max_length=20)
     pincode=models.IntegerField()

class CentreRegisterStudent(models.Model):
     student_name=models.CharField(max_length=20)
     mother_name=models.CharField(max_length=20)
     father_name=models.CharField(max_length=20)
     rollno=models.IntegerField()
     image=models.ImageField()
     Dob=models.CharField(max_length=10)
     centre_name=models.CharField(max_length=20)
     course_name=models.CharField(max_length=40)
     duration=models.CharField(max_length=10)
     examheldon=models.CharField(max_length=10)
     percent=models.IntegerField()
     grade=models.CharField(max_length=2)
     session=models.CharField(max_length=20)
     centre_code=models.IntegerField()
     dateofissue=models.CharField(max_length=10)
     remark=models.CharField(max_length=2)
     mark_s1=models.IntegerField()
     mark_s2=models.IntegerField()
     mark_s3=models.IntegerField()
     mark_s4=models.IntegerField()
     mark_s5=models.IntegerField()
     written_mark=models.IntegerField()
     practical_mark=models.IntegerField()
     assignment_mark=models.IntegerField()
     viva_mark=models.IntegerField()

class Status(models.Model):
    # You existing fields...
    status = models.CharField(max_length=30)
    student_id=models.IntegerField()
    student_rollno=models.IntegerField()     


# class StudentDetails(models.Model):
#      student_name=models.CharField(max_length=30)
#      mother_name=models.CharField(max_length=30)
#      father_name=models.CharField(max_length=30)
#      dob=models.CharField(max_length=10)
#      center_name=models.CharField(max_length=40)
#      course_name=models.CharField(max_length=30)
#      duration=models.CharField(max_length=30)
#      rollno=models.IntegerField()
#      student_photo=models.ImageField()
#      exam_held=models.CharField()
#      s1=models.IntegerField()
#      s2=models.IntegerField()
#      s3=models.IntegerField()
#      s4=models.IntegerField()
#      s5=models.IntegerField()
#      assignment_mark=models.IntegerField()
#      viva_mark=models.IntegerField()
#      percentage=models.IntegerField()
#      grade=models.CharField()
#      session=models.CharField()
#      center_code=models.IntegerField()
#      dateof_issue=models.CharField(max_length=12)



# class Centre_Registeration(models.Model):
#      centre_name=models.CharField(max_length=40)
#      email=models.EmailField(max_length=40)
#      password=models.CharField(max_length=30)
#      centerid=models.IntegerField()
#      address=models.CharField(max_length=40)
#      city=models.CharField(max_length=20)
#      state=models.CharField(max_length=30)     
#      pincode=models.IntegerField()
#      # def  __str__(self) :
#      #      return self.centre_name