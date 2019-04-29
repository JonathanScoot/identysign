from aip import AipOcr

def Prepare():

    APP_ID = '16116533'
    API_KEY = 'xDzBG3xsbz9ZgeoSb6kTC4M1'
    SECRET_KEY = 'nxBj36bQfIRLgh7U3aIxgoaEYCVtqLQF'
    image_path = '/Users/jonathan/Desktop/sign9.jpeg'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    image = get_file_content(image_path)

    options = {}
    options["language_type"] = "ENG"
    options["detect_direction"] = "false"
    options["detect_language"] = "false"
    options["probability"] = "false"


    recresult = client.basicGeneral(image, options)
    recresult2 = recresult['words_result'][0]['words']
    recresult3 = []

    formula = ''

    for i in recresult2:
        if i != (' ' or  '\n'):
            recresult3.append(i)
            formula += i

    sign = recresult3[1]
    print("识别结果为：\n")
    print(formula)

    if sign == '*' and (int(recresult3[0]) * int(recresult3[2])) == int(recresult3[4]):
        print('the result {} is correct √ '.format(recresult3[4]))

    elif sign == '+' and (int(recresult3[0]) + int(recresult3[2])) == int(recresult3[4]):
        print('the result {} is correct √ '.format(recresult3[4]))

    elif sign == '-' and (int(recresult3[0]) - int(recresult3[2])) == int(recresult3[4]):
        print('the result {} is correct √ '.format(recresult3[4]))

    elif sign == '/' and (int(recresult3[0]) / int(recresult3[2])) == int(recresult3[4]):
        print('the result {} is correct √ '.format(recresult3[4]))

    else:
        print('the result {} is error × '.format(recresult3[4]))

Prepare()
