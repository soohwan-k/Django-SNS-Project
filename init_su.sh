#!/bin/sh

echo "------ create default admin user ------"
echo "from user.models import User; User.objects.create_superuser('byemrkimseeu@naver.com','dbtn4314587', 'http://post-phinf.pstatic.net/MjAxOTA1MDdfNjkg/MDAxNTU3MjE4MDkwMDU5.XWQfwP-wq-ytF00HpdnBegHd2amDesWcEa-gjhyffEUg.PlAxpJMD4ZOuytjDqo6nFSOEJWv_2invnKUC7M4bAzEg.JPEG/%EC%9D%B4%EC%86%9C_%284%29.jpg?type=w1200')" | python manage.py shell
