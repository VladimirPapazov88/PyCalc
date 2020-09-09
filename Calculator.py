import ui, clipboard, dialogs, sound, math
shows_result = False
def buttontapped(sender):
	n = sender.title
	global shows_result
	label = sender.superview['label1']
	label2 = sender.superview['label2']
	shows_result = '0'
	if sender.name in '0123456789':
			sound.play_effect('ui:switch9')
			if label.text == '0':
				label.text = n 
			else:
				label.text += n
	if n == '-x':
		sound.play_effect('ui:switch9')
		label.text = '-'
	elif n in '+-÷×**':
		sound.play_effect('ui:switch9')
		if label.text[-1] in '+-÷×':
			label.text = label.text[:-1] + n
		else:
			label.text += n
	elif n == 'x!':
		sound.play_effect('ui:switch9')
		label2.text = label.text + '! ='
		label.text = str(math.factorial(int(label.text)))
	elif n == '.' and label.text[-1] != '.':
		sound.play_effect('ui:switch9')
		label.text += n
	elif n == 'AC':
		sound.play_effect('ui:switch9')
		label.text = '0'
		label2.text = ''
	elif n == 'C':
		sound.play_effect('ui:switch9')
		label.text = label.text[:-1]
		if len(label.text) == 0:
			label.text = '0'
	elif n == '=':
		sound.play_effect('ui:switch9')
		try:
			label2.text = label.text + ' ='
			expr = label.text.replace('÷', '/').replace('×', '*')
			label.text = str(eval(expr))
		except (SyntaxError, ZeroDivisionError):
			label.text = 'ERROR'
		shows_result = True
	elif n != '=':
		shows_result = False
		label2.text = ''
def copyresult(sender):
	t1 = sender.superview['label1'].text
	t2 = sender.superview['label2'].text
	if t2:
		text = t2 + ' ' + t1
	else:
		text = t1
	clipboard.set(text)
	sound.play_effect('arcade:Coin_3')
	dialogs.hud_alert('Copied!')
v = ui.load_view('Calculator')
v.present('sheet')
