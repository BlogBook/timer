import dns.resolver
import smtplib
import re
import time

from flask import Flask, request

app = Flask(__name__)


@app.route('/<addressToVerify>', methods=['GET'])
def email_verify(addressToVerify):

    start_time = time.time()
    # Simple Regex for syntax checking
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

    match = re.match(regex, addressToVerify)
    if match == None:
        # print('Bad Syntax')
        # raise ValueError('Bad Syntax')
        sec = (time.time() - start_time)
        return 'Invalid email' + str(sec)

    splitAddress = addressToVerify.split('@')
    domain = str(splitAddress[1])
    records = dns.resolver.query(domain, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)
    server = smtplib.SMTP()
    server.connect(mxRecord)
    server.mail(addressToVerify)
    code, message = server.rcpt(str(addressToVerify))
    server.quit()
    secs = (time.time() - start_time)
    return 'success'+str(secs)


if __name__ == '__main__':
    app.run(debug=True)
