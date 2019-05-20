from django.shortcuts import render
import pymysql

from .models import UserMessage

# Create your views here.

def getform(request):
    # 查看数据
    # # all_messages = UserMessage.objects.all()     # 将数据里的数据全部拿到
    # all_messages = UserMessage.objects.filter(name="bobby", address="北京")    # 通过条件将数据拿出来
    # for message in all_messages:
    #     print(message.name)
    # return render(request, 'message_form.html')

    # 存数据
    # user_message = UserMessage()
    # user_message.name = 'bobby2'
    # user_message.message = 'helloword2'
    # user_message.address = '上海'
    # user_message.email = '2@2.com'
    # user_message.object_id = 'helloword2'
    # user_message.save()         # models.Model的save方法，将数据写入到数据表
    # return render(request, 'message_form.html')

    # 取数据
    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')

    # 完成表单存储数据
    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     message = request.POST.get('message', '')
    #     address = request.POST.get('address', '')
    #     email = request.POST.get('email', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = 'helloword3'
    #     user_message.save()
    # return render(request, 'message_form.html')

    # 删除表单数据
    # # all_messages = UserMessage.objects.all()
    # all_messages = UserMessage.objects.filter(name="bobby", address="北京")
    # # all_messages.delete()
    # for message in all_messages:
    #     message.delete()
    # return render(request, 'message_form.html')

    # 将数据显示到HTML页面中
    message = None
    all_messages = UserMessage.objects.filter(name='bobby2')
    if all_messages:
        message = all_messages[0]
        # message = all_messages[2:8]

    return render(request, 'message_form.html', {
        "my_message": message
    })

# def book_list(request):
#     db = pymysql.connect(user='root', db='testdjango', passwd='123456', host='loaclhost')
#     cursor = db.cursor()
#     cursor.execute("SELECT name FROM books ORDER BY name")
#     names = [row[0] for row in cursor.fetchall()]
#     db.close()