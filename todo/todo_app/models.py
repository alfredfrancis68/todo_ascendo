from django.db import models

class TodoManager(models.Manager):
    pass

class Todo(models.Model):
    IMP = (
        ("Very high",0),
        ("high",1),
        ("Normal",2),
        ("Least ",3),

    )
    title = models.CharField(max_length=100)
    importance = models.SmallIntegerField(choices=IMP,default=0)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    objects = TodoManager()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'todo'
        ordering=['-pub_date']

