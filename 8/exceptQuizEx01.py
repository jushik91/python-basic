
list_test=['One','Two','Three','Four']

index=0

try:
    path='D:\\pythonProject\\project\\day20190518\\imsi_new2.txt'
    f=open(path,'x')  # a, #w, #x(파일이 존재하면 에러가 발생함)

    # for i in list_test:
    #     index=index+1
    #     f.write('{}.{}\n'.format(index,i))

    for num,i in enumerate(list_test):
        f.write('{}.{}\n'.format(num+1,i))

        f.close()

except:

    print('This file is already exist')

else:
    pass

finally:
    pass

print('successs~~!!!')
