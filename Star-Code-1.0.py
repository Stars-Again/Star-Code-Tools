# 添加模块
import os , base64 , binascii , hashlib , platform , binascii
from urllib.parse import quote , unquote

# 判断操作系统
if(platform.system()=='Windows'):
    Clear_screen = ('cls')
elif(platform.system()=='Linux'):
    Clear_screen = ('clear')
else:
    Clear_screen = ('clear')

# 清屏
os.system(Clear_screen) 

while True:

    # 定义要转换的字符串
    Conversio_content = input('[请输入要转换的内容]:')

    while True:

        # 清屏
        os.system(Clear_screen) 
        print('[输入内容为]',Conversio_content,'\n')

        # 列出功能
        function = ('[1.编码]','[2.解码]','[3.进制]','[4.重输]','[5.退出]','')
        for i in function:
            print (i)

        # 选择功能
        Conversio_mode = input ('[请输入你的选择1-5]:')

        # 编码
        if Conversio_mode == '1':

            # 清屏
            os.system(Clear_screen)
            print('[输入内容为]',Conversio_content,'\n')

            # URL编码
            transformation = quote(Conversio_content,'utf-8')
            print('[Url 编码]',transformation)

            # Hex编码
            transformation = Conversio_content.encode('utf-8')
            print('[Hex 编码]',binascii.hexlify(transformation).decode('utf-8'))

            # ASCII编码
            transformation_front = []
            transformation = []
            num = 0
            for i in Conversio_content:
                transformation.append(ord(Conversio_content[num]))
                num += 1
            print('[Ascii 编码]',' '.join(map(str,transformation)))  

            # MD5-32加密
            transformation = hashlib.md5()
            transformation.update(Conversio_content.encode('utf-8'))
            print('[MD5-32 加密]',(transformation.hexdigest()).upper())

            # MD5-16加密
            transformation = hashlib.md5()
            transformation.update(Conversio_content.encode('utf-8'))
            print('[MD5-16 加密]',(transformation.hexdigest())[8:-8].upper())

            # Base-64编码
            transformation_Bytes = bytes(Conversio_content,'utf-8')
            transformation = base64.b64encode(transformation_Bytes)
            transformation = str(transformation,'utf-8')
            print('[Base-64 编码]',transformation)

            # Base-32编码
            transformation = Conversio_content.encode('utf-8')
            transformation = base64.b32encode(transformation)
            transformation = str(transformation,'utf-8')
            print('[Base-32 编码]',transformation)

            # Base-16编码
            transformation = Conversio_content.encode('utf-8')
            transformation = base64.b16encode(transformation)
            transformation = str(transformation,'utf-8')
            print('[Base-16 编码]',transformation)

            # Unicode编码
            transformation_unicode = Conversio_content.encode('unicode_escape')
            transformation_unicode = str(transformation_unicode,'utf-8')
            print('[Unicode 编码]',transformation_unicode)

            # Sha-1加密
            transformation_sha1 = hashlib.sha1(Conversio_content.encode('utf-8'))
            transformation = transformation_sha1.hexdigest()
            print('[Sha-1 加密]',transformation)

            # Sha-224加密
            transformation_sha1 = hashlib.sha224(Conversio_content.encode('utf-8'))
            transformation = transformation_sha1.hexdigest()
            print('[Sha-224 加密]',transformation)

            # Sha-256加密
            transformation_sha1 = hashlib.sha256(Conversio_content.encode('utf-8'))
            transformation = transformation_sha1.hexdigest()
            print('[Sha-256 加密]',transformation)

            # Sha-384加密
            transformation_sha1 = hashlib.sha384(Conversio_content.encode('utf-8'))
            transformation = transformation_sha1.hexdigest()
            print('[Sha-384 加密]',transformation,'\n')

            # 返回
            input('[按回车键返回]')

        # 解码
        elif Conversio_mode == '2':

            # 清屏
            os.system(Clear_screen)
            print('[输入内容为]',Conversio_content,'\n')

            # Url还原
            transformation = unquote(Conversio_content,'utf-8')
            print ('[Url还原]',transformation)

            # Hex还原
            while True:
                try:
                    transformation = Conversio_content.encode('utf-8')
                    transformation = binascii.unhexlify(transformation)
                    print ('[Hex还原]',transformation.decode('utf-8'))
                    break
                except ValueError:
                    print ('[Hex还原] 输入的内容不可被还原')
                    break

            # Ascii还原
            while True:
                #正常
                try:
                    transformation_ascii_list = Conversio_content
                    (f'transformation_ascii_list={transformation_ascii_list.split()}')
                    transformation_ascii_list += ' '
                    transformation_ascii_splicing = ' '
                    transformation = ''

                    for i in transformation_ascii_list:
                        transformation_ascii_splicing = transformation_ascii_splicing + i
                        x = (i.isdigit())
                        if x == True:
                            pass
                        else:
                            transformation_ascii_splicing = int(transformation_ascii_splicing)
                            transformation += chr(transformation_ascii_splicing)
                            transformation_ascii_splicing = ''
                    print ('[Ascii还原]',transformation)
                    break
                # 报错
                except ValueError:
                    print('[Ascii还原] 输入的内容不可被还原')
                    break

            # Base64还原
            while True:
                # 正常
                try:
                    transformation_Base64_decrypt = bytes(Conversio_content,'utf-8')
                    transformation = base64.b64decode(transformation_Base64_decrypt)
                    transformation = str(transformation,'utf-8')
                    print('[Base64还原]',transformation)
                    break
                # 报错
                except ValueError:
                    print('[Base64还原] 输入的内容不可被还原')
                    break

            # Base32还原
            while True:
                # 正常
                try:
                    transformation_Base64_decrypt = bytes(Conversio_content,'utf-8')
                    transformation = base64.b32decode(transformation_Base64_decrypt)
                    transformation = str(transformation,'utf-8')
                    print('[Base64还原]',transformation)
                    break
                # 报错
                except ValueError:
                    print('[Base32还原] 输入的内容不可被还原')
                    break

            # Base16还原
            while True:
                # 正常
                try:
                    transformation_Base64_decrypt = bytes(Conversio_content,'utf-8')
                    transformation = base64.b16decode(transformation_Base64_decrypt)
                    transformation = str(transformation,'utf-8')
                    print('[Base64还原]',transformation)
                    break
                # 报错
                except ValueError:
                    print('[Base16还原] 输入的内容不可被还原')
                    break

            # Unicode还原
            while True:
                # 正常
                try:
                    transformation_unicode = Conversio_content
                    transformation_unicode = bytes(transformation_unicode,encoding='utf-8')
                    transformation_unicode = transformation_unicode.decode('unicode_escape')
                    print('[Unicode还原]',transformation_unicode)
                    break
                # 报错
                except:
                    print('[Unicode还原] 输入的内容不可被还原')
                    break

            # 返回
            print('')
            input('[按回车键返回]')

        # 进制
        elif Conversio_mode == '3':
            # 清屏
            os.system(Clear_screen)
            print('[输入内容为]',Conversio_content,'\n')
            transformation_Base_system = Conversio_content
            judge = transformation_Base_system.isalnum()

            if judge == True:
                while True:
                    # 清屏
                    os.system(Clear_screen)
                    print('[输入内容为]',Conversio_content,'\n')
                    function = ('[1.二进制]','[2.八进制]','[3.十进制]','[4.十六进制]','','[按回车键返回]')
                    for i in function:
                        print (i)

                    # 选择功能
                    function = input ('[请输入当前进制1-4]:')
                    print('')
                    
                    transformation_2_Base_system = Conversio_content

                    # 当前为二进制
                    if function == '1':
                        
                        # 开始死循环
                        while True:
                            # 正常
                            try:
                                # 清屏
                                os.system(Clear_screen)
                                print('[输入内容为]',Conversio_content,'\n')

                                # 转换为八进制
                                print('[八进制]',oct(int(transformation_2_Base_system,2)))

                                # 转换为十进制
                                print('[十进制]',(int(transformation_2_Base_system,2)))

                                # 转换为十六进制
                                print('[十六进制]',hex(int(transformation_2_Base_system,2)))

                                # 返回
                                print('')
                                input('[按回车键返回]')
                                break
                            # 报错
                            except:
                                # 清屏
                                os.system(Clear_screen)
                                print('[输入内容为]',Conversio_content,'\n')
                                print('[进制] 输入的内容不是二进制')

                                # 返回
                                print('')
                                input('[按回车键返回]')
                                break

                    # 当前为八进制
                    elif function == '2':

                        # 开始死循环
                        while True:
                            # 正常
                            try:
                                # 清屏
                                os.system(Clear_screen)
                                print('[输入内容为]',Conversio_content,'\n')

                                # 转换为二进制
                                print('[二进制]',bin(int(transformation_2_Base_system,8)))

                                # 转换为十进制
                                print('[十进制]',(int(transformation_2_Base_system,8)))

                                # 转换为十六进制
                                print('[十六进制]',hex(int(transformation_2_Base_system,8)))

                                # 返回
                                print('')
                                input('[按回车键返回]')
                                break
                            # 报错
                            except:
                                # 清屏
                                os.system(Clear_screen)
                                print('[输入内容为]',Conversio_content,'\n')
                                print('[进制] 输入的内容不是八进制')

                                # 返回
                                print('')
                                input('[按回车键返回]')
                                break

                    # 当前为十进制
                    elif function == '3':
                        # 开始死循环
                        while True:
                            # 正常
                            try:
                                # 清屏
                                os.system(Clear_screen)
                                print('[输入内容为]',Conversio_content,'\n')

                                # 转换为二进制
                                print('[二进制]',bin(int(transformation_2_Base_system)))

                                # 转换为八进制
                                print('[八进制]',(oct(int(transformation_2_Base_system))))

                                # 转换为十六进制
                                print('[十六进制]',hex(int(transformation_2_Base_system)))

                                # 返回
                                print('')
                                input('[按回车键返回]')
                                break
                            # 报错
                            except:
                                # 清屏
                                os.system(Clear_screen)
                                print('[输入内容为]',Conversio_content,'\n')
                                print('[进制] 输入的内容不是十进制')

                                # 返回
                                print('')
                                input('[按回车键返回]')
                                break

                    # 当前为十六进制
                    elif function == '4':

                        # 开始死循环
                        while True:
                            # 正常
                            try:
                                # 清屏
                                os.system(Clear_screen)
                                print('[输入内容为]',Conversio_content,'\n')

                                # 转换为二进制
                                print('[二进制]',bin(int(transformation_2_Base_system,16)))

                                # 转换为八进制
                                print('[八进制]',oct(int(transformation_2_Base_system,16)))

                                # 转换为十进制
                                print('[十进制]',(int(transformation_2_Base_system,16)))

                                # 返回
                                print('')
                                input('[按回车键返回]')
                                break
                            # 报错
                            except:
                                # 清屏
                                os.system(Clear_screen)
                                print('[输入内容为]',Conversio_content,'\n')
                                print('[进制] 输入的内容不是十六进制')

                                # 返回
                                print('')
                                input('[按回车键返回]')
                                break
                    else:
                        break
            else:
                # 返回
                print('')
                input('[按回车键返回]')
                break

        # 重输
        elif Conversio_mode == '4':
            # 清屏
            os.system(Clear_screen)
            break 

        # 退出
        elif Conversio_mode == '5':
            # 清屏
            os.system(Clear_screen) 
            print('[退出程序]')
            exit()