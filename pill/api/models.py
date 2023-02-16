from django.db import models


class FileUpload(models.Model) :
    save_files = models.ImageField("file", upload_to='Uploaded Files/%y/%m/%d/', blank=True)
    predict_shape = models.CharField(blank=True, max_length = 20)
    predict_color = models.CharField(blank=True, max_length = 20)
    pub_date = models.DateField(auto_now = True)
    # 일치, 불일치 필드 추가

    class Meta() :
        db_table = "images"

class DrugInfo(models.Model):
    id = models.AutoField(primary_key=True)
    ITEM_NAME = models.CharField(null=True, max_length=200, default="")
    ITEM_NAME_SUB = models.TextField(null=True, blank=True, default="")
    ENTP_NAME = models.CharField(null=True, blank=True, max_length=200, default="")
    CHART = models.CharField(null=True, blank=True, max_length=1000, default="")
    PRINT_FRONT = models.CharField(null=True, blank=True, max_length=200, default="")
    PRINT_BACK = models.CharField(null=True, blank=True, max_length=200, default="")
    DRUG_SHAPE = models.CharField(null=True, blank=True, max_length=200, default="")
    DRUG_SHAPE2 = models.CharField(null=True, blank=True, max_length=200, default="")
    COLOR_CLASS1 = models.CharField(null=True, blank=True, max_length=200, default="")
    COLOR_CLASS1_투명_제외 = models.CharField(null=True, blank=True, max_length=200, default="")
    COLOR_CLASS2 = models.CharField(null=True, blank=True, max_length=200, default="")
    COLOR_CLASS2_투명_제외 = models.CharField(null=True, blank=True, max_length=200, default="")
    LINE_FRONT = models.CharField(null=True, blank=True, max_length=200, default="")
    LINE_BACK = models.CharField(null=True, blank=True, max_length=200, default="")
    LENG_LONG = models.CharField(null=True, blank=True, max_length=200, default="")
    LENG_SHORT = models.CharField(null=True, blank=True, max_length=200, default="")
    THICK = models.CharField(null=True, default="", max_length=50)
    CLASS_NAME = models.CharField(null=True, blank=True, max_length=200, default="")
    ETC_OTC_NAME = models.CharField(null=True, blank=True, max_length=200, default="")    
    FORM_CODE_NAME = models.CharField(null=True, blank=True, max_length=200, default="")
    MARK_CODE_FRONT_ANAL = models.CharField(null=True, blank=True, max_length=200, default="")
    MARK_CODE_BACK_ANAL = models.CharField(null=True, blank=True, max_length=200, default="")
    MARK_CODE_FRONT_IMG = models.TextField(null=True, blank=True, default="")
    MARK_CODE_BACK_IMG = models.TextField(null=True, blank=True, default="")
    MARK_CODE_FRONT = models.CharField(null=True, blank=True, max_length=200, default="")
    MARK_CODE_BACK = models.CharField(null=True, blank=True, max_length=200, default="")
    # IMG_PATH = models.CharField(null=True, blank=True, max_length=200, default="")
    
    class Meta() :
        db_table = "drug_info"