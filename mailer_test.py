import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import io
import os
import commands
import gzip
#from formatstring import format
from email.MIMEBase import MIMEBase
from email import Encoders

###########################################################
#    Name: send_mail()
#    Args: send_from : mail send from 
#          send_to : mail sent TO receipeints
#          subject : Subject for the mail
#          text    : contain for the mail
#          cc=[]   : client carbon copy list
#          bcc=[]  : blind carbon copy list
#          files   : List of files default None
#          tar_path: tar path for the zip files tobe attached by mail default None
#          server  : local server for sending the mail
# Returns: None
#  Raises: n/a
#    Desc: This functions invokes for sending the mail status for the processing either sucsess/fail
##########################################################

output=commands.getstatusoutput("cat tmpx")[1]

def send_mail(send_from, send_to, subject, text, cc=[], bcc=[], files=None, tar_path=None, server=""):
    try:
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = send_from
        msg['To'] = ', '.join(send_to)
        msg.attach(MIMEText(text,'html'))
        if files:
            multiple_attach = files.split(",")
            if len(multiple_attach) > 1:
                for files in multiple_attach:
                    if not files.endswith("pdf"):
                        with open(files, 'rb') as listOfFiles, io.BytesIO() as buf:
                            gz_file = gzip.GzipFile(mode='wb', fileobj=buf)
                            gz_file.writelines(listOfFiles)
                            gz_file.close()
                            attachment = MIMEApplication(buf.getvalue(), 'x-gzip')
                            attachment['Content-Disposition'] = 'attachment; filename='+basename(files)+'.gz'
                            msg.attach(attachment)
                    else:
                        part = MIMEBase('application', "octet-stream")
                        part.set_payload(open(tar_path+files,"rb").read() )
                        Encoders.encode_base64(part)
                        part.add_header('Content-Disposition', 'attachment; filename="%s"' % (files))
                        msg.attach(part)
            else:
                with open(files, 'rb') as listOfFiles, io.BytesIO() as buf:
                    gz_file = gzip.GzipFile(mode='wb', fileobj=buf)
                    gz_file.writelines(listOfFiles)
                    gz_file.close()
                    attachment = MIMEApplication(buf.getvalue(), 'x-gzip')
                    attachment['Content-Disposition'] = 'attachment; filename='+basename(files)+'.gz'
                    msg.attach(attachment)

        smtp = smtplib.SMTP(server)
        smtp.sendmail(send_from, send_to+cc+bcc, msg.as_string())
        smtp.close()
        print "Mail Send successfully"
    except Exception as inst:
        raise inst



html = """\
<html>
<body>
Hello, </br>
This is the test email.
</body>
</html>
""".format(output=output)

send_from = "abhijeetmote@gmail.com"
send_to =  ["abhijeetmote@gmail.com"]
subject = "test"
text = html
cc=[]
bcc=[]
files="finalValid.py"
tar_path=None
server="localhost"

send_mail(send_from, send_to, subject, text, cc, bcc, files, tar_path, server)
