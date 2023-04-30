# Language is Japanese
test_data_A_1 = ('JA', u'情報を入手')

# Language is Korean
test_data_A_2 = ('KO', 'Get info')
test_data_A_2_correct = ('KO', u'정보를 얻다')

# Language is Russian
test_data_A_3 = ('RU', u'Получить информацию')

# Language is Chinese
test_data_A_4 = ('ZH', u'获取信息')

# Language is English
test_data_A_5 = ('EN', 'Get info')

# Valid series number
test_data_B_1 = ('1863552437',
                 ['Warranty results for 1863552437',
                  'Description', 'CLICKSHARE CX-50 SET EU',
                  'Part number', 'R9861522EU',
                  'Installation date', '10 Feburary 2021',
                  'Warranty end date', '08 Feburary 2022'])

# Blank input
test_data_B_2_1 = ('','Please specify a serial number.')

# length is less than 6 digital
test_data_B_2_2 = ('aaa','A minimum of 6 characters is required.')

# invalid seriel number
test_data_B_2_3 = ('186355aa', "We couldn't find a product with this serial number. Please double-check the serial number and try again.")

