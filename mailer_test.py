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
#    Desc: This functions invokes for sending the mail status for the processing either sucess/fail
##########################################################
execute=commands.getstatusoutput("ls -ld -h /mnt/demo_data/20150826/AMS/* | egrep 1a | awk '{print $9}'")
output=commands.getstatusoutput("cat tmpx")[1]

#print a[1]
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
<head>
<style>
table, th, td
table, th, td
{{border: 1px solid black;}}
</style>

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

</head>
<body>

Hi Team,

<br/> <br/>

Folder created for $today at the following path $download_directory/$today and its size is $fullsize
<br/> <br/>
Below is the list of Files received Today
<br/> <br/>


#Table definition starts here
<table>
<tr>
<td><b> Folder Name </b></td>
<td><b> File Name  </b></td>
<td><b> Size </b></td>
</tr>
<tr>
<td>%fcs1 AMS %fce1</td>
<td>
%s
</td>

<td>

<br><br><h1>{output}</h1><br>

</td>

</tr>

</table>
<br/> <br/> <br/> <br/> 
$nct<br/>$nct1
<br/> <br/>

Regards
<br/>
System Team

</body>
</html>

""".format(output=output)

send_mail("abhijeetmote@gmail.com", ["abhijeetmote@gmail.com"], "test", html , cc=[], bcc=[], files="/home/abhijeet/testing/mail.py,/home/abhijeet/testing/finalValid.py", tar_path=None, server="localhost")
##send_mail(send_from, send_to, subject, text, cc=[], bcc=[], files=None, tar_path=None, server="localhost")

