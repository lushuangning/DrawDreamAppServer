from django.db import models
# Create your models here.


class Account(models.Model):
    acco_id = models.AutoField(primary_key=True)
    acco_num = models.charField(max_length=32, unique=True)
    acco_pwd = models.charField(max_length=18)
    # 设置auto_now_add或者auto_now为True时会使editable置为False
    acco_create_date = models.DateField(auto_now_add=True)
    acco_modify_date = models.DateField(null=True)
    acco_login_date = models.DateField(null=True)
    acco_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    # ForeignKey默认地使用关联对象的主键。
    usin_id = models.ForeignKey(Account)
    usin_name = models.CharField(max_length=32, default="漫画小迷弟")
    usin_sex = models.BooleanField()
    usin_phone = models.CharField(max_length=20, unique=True, null=True)
    usin_email = models.EmailField()
    usin_sign = models.CharField(max_length=256, default="这个人很懒，什么也没留下")

    def __str__(self):
        return self.title


class NewsClassify(models.Model):
    necl_id = models.UUIDField(primary_key=True)
    necl_name = models.CharField(max_length=64, unique=True)
    necl_create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class NewsSummary(models.Model):
    nesu_id = models.UUIDField(primary_key=True)
    nesu_classify = models.ForeignKey(NewsClassify)
    nesu_create_date = models.DateField(auto_now_add=True)
    nesu_count = models.IntegerField(default=0)
    nesu_like = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class NewsDetial(models.Model):
    nede_id = models.ForeignKey(NewsSummary, primary_key=True)
    nede_title = models.CharField(max_length=128)
    nede_author = models.CharField(max_length=64, default="佚名")
    nede_time = models.DateField(null=True)
    nede_content = models.TextField()

    def __str__(self):
        return self.title


class UserCollect(models.Model):
    usco_acco_id = models.ForeignKey(Account, primary_key=True)
    usco_acco_id = models.ForeignKey(NewsSummary)
    usco_create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentReplay(models.Model):
    core_acco_id = models.ForeignKey(Account, primary_key=True)
    core_nede_id = models.ForeignKey(NewsSummary, primary_key=True)
    core_content = models.CharField(max_length=512)
    core_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
