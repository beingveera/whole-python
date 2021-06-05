import smtplib as s

obj=s.SMTP('smtp.gmail.com',587)

obj.starttls()

obj.login("smart.iv.user@gmail.com",'9829237552')

subject="Smart IV Team "
body="Hello Shubham,\nWel come to our Community of smart iv. we have done a lot of work in our project and as soon as possible we will complete our project. it`s just a testing mail for alert configration and server data testing .\n\n From:\n Smart IV Team."

message="Subject:{}\n\n{}".format(subject,body)

obj.sendmail("smart.iv.user@gmail.com","shubhamvagrecha2000@gmail.com",message)
print("Send main successfully...")
obj.quit()



