from django.db import models


class User(models.Model) :
    data_result = models.CharField(blank=True, max_length = 5000, default="")
    label = models.CharField(blank=True, max_length = 500, default="")

class FileUpload(models.Model) :
    save_files = models.ImageField("file", upload_to='Uploaded Files/%y/%m/%d/', blank=True)
    predict_shape = models.CharField(blank=True, max_length = 500, default="", null = True)
    predict_color = models.CharField(blank=True, max_length = 500, default="", null = True)
    pub_date = models.DateField(auto_now = True)
    result = models.CharField(blank=True, max_length = 5000, default="", null = True)
    # 일치, 불일치 필드 추가

    class Meta() :
        db_table = "images"

class DrugInfo(models.Model):
    id = models.AutoField(primary_key=True)
    ITEM_SEQ = models.IntegerField(null=True)
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

class DrugInfoEfcy(models.Model):
    entpName = models.CharField(null=True, max_length=200, default="")
    itemName = models.CharField(null=True, max_length=200, default="")
    itemSeq = models.IntegerField(null=True)
    efcyQesitm = models.CharField(null=True, max_length=5000, default="")
    useMethodQesitm = models.CharField(null=True, max_length=5000, default="")
    atpnWarnQesitm = models.CharField(null=True, max_length=5000, default="")
    atpnQesitm = models.CharField(null=True, max_length=5000, default="")
    intrcQesitm = models.CharField(null=True, max_length=5000, default="")
    seQesitm = models.CharField(null=True, max_length=5000, default="")
    depositMethodQesitm = models.CharField(null=True, max_length=5000, default="")

    class Meta() :
        db_table = "use_method"

class DrugMaterial(models.Model) :
    ITEM_SEQ = models.CharField(max_length=100, null=True)
    ITEM_NAME = models.CharField(max_length=5000, blank=True, default="", null=True)
    ENTP_NAME = models.CharField(max_length=5000, blank=True, default="", null=True)
    ITEM_PERMIT_DATE = models.CharField(max_length=5000, blank=True, default="", null=True)
    ETC_OTC_CODE = models.CharField(max_length=5000, blank=True, default="", null=True)
    CLASS_NO = models.CharField(max_length=5000, blank=True, default="", null=True)
    CHART = models.CharField(max_length=5000, blank=True, default="", null=True)
    BAR_CODE = models.CharField(max_length=5000, blank=True, default="", null=True)
    MATERIAL_NAME = models.CharField(max_length=5000, blank=True, default="", null=True)
    EE_DOC_ID = models.CharField(max_length=5000, blank=True, default="", null=True)
    UD_DOC_ID = models.CharField(max_length=5000, blank=True, default="", null=True)
    NB_DOC_ID = models.CharField(max_length=5000, blank=True, default="", null=True)
    INSERT_FILE = models.CharField(max_length=5000, blank=True, default="", null=True)
    STORAGE_METHOD = models.CharField(max_length=5000, blank=True, default="", null=True)
    VALID_TERM = models.CharField(max_length=5000, blank=True, default="", null=True)
    REEXAM_TARGET = models.CharField(max_length=5000, blank=True, default="", null=True)
    REEXAM_DATE = models.CharField(max_length=5000, blank=True, default="", null=True)
    PACK_UNIT = models.CharField(max_length=5000, blank=True, default="", null=True)
    EDI_CODE = models.CharField(max_length=5000, blank=True, default="", null=True)
    CANCEL_DATE = models.CharField(max_length=5000, blank=True, default="", null=True)
    CANCEL_NAME = models.CharField(max_length=5000, blank=True, default="", null=True)
    TYPE_CODE = models.CharField(max_length=5000, blank=True, default="", null=True)
    TYPE_NAME = models.CharField(max_length=5000, blank=True, default="", null=True)
    CHANGE_DATE = models.CharField(max_length=5000, blank=True, default="", null=True)

    class Meta() :
        db_table = "material"