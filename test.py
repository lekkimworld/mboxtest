import mailbox

mbox = mailbox.mbox('test.mbox')
for msg in mbox:
	msgsubject = msg['subject']
	msgfrom = msg['from']
	msgbody = '';

	# see if message is MIME multipart - if yes only get plain text parts
	if msg.is_multipart():
		for payload in msg.get_payload():
			if payload['Content-Type'] == 'text/plain':
				msgbody += payload.get_payload()
	else:
		# it's not -- great - just get contents
		msgbody = msg.get_payload()

	# ignore if no plain text body
	if len(msgbody) == 0: continue

	# output body length
	print msgsubject + ', body is <' + str(len(msgbody)) + '> chars...'

    