import json 
import subprocess as sb 
from smtplib import SMTP

def checker(json_file):
    ip_list = json.load(json_file)
    not_routed = list()
    for i in range(0, len(ip_list['ip_list'])):
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
    with SMTP("mail.server.com") as ae_smtp:
        if not not_routed:
            SUBJECT = "Prolexic IP Checker Alert"
            TEXT = "Checked all IP addresses and all are routed through AKAMAI or PROLEXIC."
            FROM ='noreply@mail.com'
            TO = ['vasudevan.perumal@mail.com']
            msg = 'From: {}\n To: {}\nSubject: {}\n\n{}'.format(FROM, TO[0], SUBJECT, TEXT)
            ae_smtp.sendmail(FROM, TO, msg)
        else:
            SUBJECT = "Prolexic IP Checker Alert"
            TEXT = "The IP addresses not routed through PROLEXIC or AKAMAI are {not_routed}. Please Check Them!".format(not_routed=not_routed)
            FROM ='noreply@mail.com'
            TO = ['vasudevan.perumal@mail.com']
            msg = 'From: {}\n To: {}\nSubject: {}\n\n{}'.format(FROM, TO[0], SUBJECT, TEXT)
            ae_smtp.sendmail(FROM, TO, msg)
        
if __name__ == "__main__":
    with open("parameters.json") as json_file:
        checker(json_file)
        
