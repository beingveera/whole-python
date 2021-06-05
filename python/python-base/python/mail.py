import smtplib as s
obj=s.SMTP('smtp.gmail.com',587)
obj.starttls()
obj.login("veerasharma9895@gmail.com",'9829237552')
sub="Sending a s mail using python"
body="its me veera"
message="Subject:{}\n\n{}".format(sub,body)
list_address=["veerasharma0000@gmail.com"]
obj.sendmail('veerasharma9895@gmail.com',list_address,message)
print("Mail Send Succesfuly...")
obj.quit()
