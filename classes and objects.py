class user:
      def __init__(self ,email,nam,passw,currentjob):
         self.email=email
         self.name=nam
         self.password=passw
         self.current_job_title=currentjob
      def changepassword(self,newpass):
         self.password=newpass
      def changejobtitle(self,newjob):
         self.current_job_title=newjob
      def getuserinfo(self):
          print(f"user{self.name} currently work as{self.current_job_title} email of user {self.email } password of user{self.password}")
          appuser=user("manjunadha949@gmail.com","M.Manjunadha","121212Manju","Student")
          h=input("Hey user enter newpassword")
          appuser.changepassword(str(h))
          p=input("Hey user enter new job")
          appuser.changejobtitle(str(p))
          appuser.getuserinfo()
