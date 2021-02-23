# 密碼重試
password = 'a123456'
x = 3

while x > 0:
	ans = input('請輸入密碼： ')
	if ans == password:
		print('登入成功！')
		break
	elif ans != password and x > 1:
		print('密碼錯誤！ 還有', x - 1, '次機會')
		x = x - 1
	else:
		print('你已錯3次了')
		break