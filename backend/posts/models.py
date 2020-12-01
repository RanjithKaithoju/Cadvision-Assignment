from django.db import models

# Create your models here.

#User model
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=255)

    def __str__(self):
        return self.first_name




#Posts model(OneToMany Relationship with User)
class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE)
    post_date = models.DateTimeField( auto_now_add=True,blank=True)
    post_title = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title
    

#Comments Model(OneToMany Relationship with Posts)
class Comments(models.Model):
    body = models.TextField(max_length=1024)
    date = models.DateTimeField( auto_now_add=True,blank=True)
    post_id = models.ForeignKey(Posts,related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'Comments'