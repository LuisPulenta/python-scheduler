import pandas
import datetime as dt
import random
import smtplib
from email.message import EmailMessage

# data = pandas.read_csv("d:/0Cursos/AngelaYu/Dia032-Mails de cumpleaños/cumples.csv")
data = pandas.read_csv("cumples.csv")
cumples=data.to_dict(orient="records")

birthdays_dict={(data_row["month"],data_row["day"]): data_row for (index,data_row) in data.iterrows()}

my_email = "luisnu23061965@gmail.com"
my_password="pftl pyfs byux fjju"

current_date = dt.datetime.now()

month =current_date.month
day =current_date.day

connection=smtplib.SMTP("smtp.gmail.com", 587)

for cumple in cumples:
    if cumple['month'] == month and cumple['day'] == day:
        name=cumple['name']
        mail=cumple['email']
        
        # with open(f"d:/0Cursos/AngelaYu/Dia032-Mails de cumpleaños/letter{random.randint(1,3)}.txt", encoding="utf-8") as lines:
        with open(f"letter{random.randint(1,3)}.txt", encoding="utf-8") as lines:
            content=lines.read()
            content=content.replace("[NAME]",name)

            with connection:
                connection.starttls()
                connection.login(user=my_email , password=my_password)
                msg = EmailMessage()
                msg["Subject"] = "Feliz cumple!!"
                msg["From"] = my_email
                msg["To"] = mail
                msg.set_content(content, charset="utf-8")
                with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                    connection.starttls()
                    connection.login(my_email, my_password)
                    connection.send_message(msg)
        