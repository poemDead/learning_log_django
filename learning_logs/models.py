from django.db import models

# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """关于某主题的具体知识的一个条目"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 多个条目显示为Entries 而不是默认的Entrys
        verbose_name_plural = 'Entries'
    
    def __str__(self):
        return f"{self.text[:50]}..."

    