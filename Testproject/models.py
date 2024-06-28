from django.db import models

# Create your models here.

class TestProject(models.Model):
    """测试项目表"""
    name = models.CharField(max_length=50, help_text="项目名称", verbose_name="项目名称")
    leader = models.CharField(max_length=20, help_text="负责人", verbose_name="负责人")
    create_time = models.DateTimeField(auto_now_add=True, help_text="创建日期", verbose_name="创建日期")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "TestProject"
        verbose_name_plural = "测试项目表"

class TestEnv(models.Model):
    """项目测试环境表"""
    project = models.ForeignKey(TestProject, on_delete=models.CASCADE, help_text="所属项目", verbose_name="所属项目")
    global_variable = models.JSONField(help_text="全局变量", verbose_name="全局变量", default=dict, null=True, blank=True)
    debug_global_variable = models.JSONField(help_text="调试模式全局变量", verbose_name="调试模式全局变量", default=dict, null=True, blank=True)
    db = models.JSONField(help_text="数据库配置", verbose_name="数据库配置", default=dict, null=True, blank=True)
    headers = models.JSONField(help_text="全局请求头", verbose_name="全局请求头", default=dict, null=True, blank=True)
    global_func = models.TextField(help_text="全局工具函数", verbose_name="全局工具函数", default='', null=True, blank=True)
    name = models.CharField(max_length=50, help_text="测试环境名称", verbose_name="测试环境名称")
    host = models.CharField(max_length=50, help_text="测试环境的host地址", verbose_name="测试环境的host地址")

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "TestEnv"
        verbose_name_plural = "测试环境表"

class TestFile(models.Model):
    """测试文件表"""
    file = models.FileField(help_text="文件", verbose_name="文件")
    info = models.JSONField(help_text="文件信息", verbose_name="文件信息", default=list)

    def __str__(self):
        return self.info
    
    class Meta:
        db_table = "TestFile"
        verbose_name_plural = "测试文件表"
