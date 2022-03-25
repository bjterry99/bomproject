from django.db import models

class scripture(models.Model) :
    scripture_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=2000, default="text", verbose_name="Words")
    scripture = models.CharField(max_length=50, default="scripture", verbose_name="Scripture")
    tip = models.CharField(max_length=100, default="When your...", verbose_name="Tip")
    encouragement = models.BooleanField(default=False)
    testimony = models.BooleanField(default=False)
    low = models.BooleanField(default=False)

    class Meta:
        db_table = 'scripture'

    def __str__(self) :
        return (self.scripture)

class user(models.Model) :
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, default="admin", verbose_name="Username")
    password = models.CharField(max_length=50, default="1234", verbose_name="Password")

    class Meta:
        db_table = 'user'

    def __str__(self) :
        return (self.username)

class favorite(models.Model) :
    fav_id = models.AutoField(primary_key=True)
    scriptureid = models.ForeignKey(scripture, models.DO_NOTHING, default="default", verbose_name="Scripture")
    userid = models.ForeignKey(user, models.DO_NOTHING, default="default", verbose_name="User")

    class Meta:
        db_table = 'favorite'

    def __str__(self) :
        return (str(self.scriptureid) + ' - ' + str(self.userid))