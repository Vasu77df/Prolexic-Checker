import json 
import subprocess as sb 
from smtplib import SMTP
from email.mime.text import MIMEText

def checker(json_file):
    # len(ip_list['ip_list'])
    ip_list = json.load(json_file)
    not_routed = list()
    for i in range(0, 1):
        ip = ip_list['ip_list'][i]
        cmnd =  f"traceroute {ip}"
        net =  sb.run(cmnd, shell=True, stdout=sb.PIPE, stderr=sb.STDOUT)
        net_out = net.stdout
        net_out = net_out.decode('utf-8')
        net_out = net_out.strip('\n')
        print(net_out)
        if "akamai" in net_out or "prolexic" in net_out:
            print("It's there")
        else:
            print("not there")
            not_routed.append(ip)
    print(not_routed)
    with SMTP("cl-mont-1vms01.americaneagle.com") as ae_smtp:
        if not not_routed:
            msg  = """\
            From: noreply@americaneagle.com\r\n
            To: vasudevan.perumal@americaneagle.com\r\n
            Subject: Prolexic IP Checker Alert\r\n

            Checked all IP addresses and all are routed through AKAMAI or PROLEXIC"""
            FROM ='noreply@americaneagle.com'
            TO = ['vasudevan.perumal@americaneagle.com']
            ae_smtp.sendmail(FROM, TO, msg)
        else:
            msg = MIMEText("""The IP addresses not routed through PROLEXIC or AKAMAI are {not_routed}. Please Check Them!""".format(not_routed=not_routed))
            SUBJECT = "Prolexic IP Checker Alert"
            #TEXT = "The IP addresses not routed through PROLEXIC or AKAMAI are {not_routed}. Please Check Them!".format(not_routed=not_routed)
            FROM ='noreply@americaneagle.com'
            TO = ['vasudevan.perumal@americaneagle.com']
            msg['Subject'] = SUBJECT
            msg['From'] = FROM
            msg['To'] = TO[0]
            #msg = 'From: {}\n To: {}\nSubject: {}\n\n{}'.format(FROM, ','.join(TO), SUBJECT, TEXT)
            ae_smtp.sendmail(FROM, TO, msg)
        
if __name__ == "__main__":
    with open("parameters.json") as json_file:
        checker(json_file)
        

        'daniel.garczek@americaneagle.com'