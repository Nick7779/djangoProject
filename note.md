### Admin：
在Django自带的admin中创建超级用户：`python manage.py createsuperuser`

###APP:
创建APP：`python manage.py startapp [Name]`

### Model：
models.CharField：必须指定长度max_length=20

Model生成迁徙文件：`python manage.py makemigrations`

执行迁徙文件：`python manage.py migrate`