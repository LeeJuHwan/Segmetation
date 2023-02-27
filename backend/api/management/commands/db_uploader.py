import pandas as pd
from sqlalchemy import create_engine
from django.core.management.base import BaseCommand
from api.models import DrugInfo, DrugInfoEfcy, DrugMaterial

class Command(BaseCommand):
    def handle(self, *args, **options):
        columns = ["ITEM_SEQ", "ITEM_NAME", "ITEM_NAME_SUB", "ENTP_NAME", "CHART", "PRINT_FRONT", "PRINT_BACK", "DRUG_SHAPE", "DRUG_SHAPE2",
                "COLOR_CLASS1", "COLOR_CLASS1-투명 제외", "COLOR_CLASS2", "COLOR_CLASS2-투명 제외", "LINE_FRONT","LINE_BACK", "LENG_LONG", 
                "LENG_SHORT", "THICK", "CLASS_NAME", "ETC_OTC_NAME", "FORM_CODE_NAME", "MARK_CODE_FRONT_ANAL", "MARK_CODE_BACK_ANAL", 
                "MARK_CODE_FRONT_IMG", "MARK_CODE_BACK_IMG", "MARK_CODE_FRONT",  "MARK_CODE_BACK"]
        
        df = pd.read_excel("/home/lab06/drug_total_수정본.xlsx")
        df = df[columns]
        df.rename(columns = {'COLOR_CLASS1-투명 제외' : 'COLOR_CLASS1_투명_제외',
                    "COLOR_CLASS2-투명 제외" : "COLOR_CLASS2_투명_제외"}, inplace = True)
        engine = create_engine("postgresql://postgres:1111@localhost:5432/project")
        df.to_sql(DrugInfo._meta.db_table, if_exists='append' ,con=engine, index=False)

        columns = ['entpName', 'itemName', 'itemSeq', 'efcyQesitm',
        'useMethodQesitm', 'atpnWarnQesitm', 'atpnQesitm', 'intrcQesitm',
        'seQesitm', 'depositMethodQesitm']
        
        df2 = pd.read_csv("/home/lab06/use_method.csv")
        df2 = df2[columns]
        engine2 = create_engine("postgresql://postgres:1111@localhost:5432/project")
        df2.to_sql(DrugInfoEfcy._meta.db_table, if_exists='append' ,con=engine2, index=False)


        mate_columns = ['ITEM_SEQ', 'ITEM_NAME', 'ENTP_NAME', 'ITEM_PERMIT_DATE', 'ETC_OTC_CODE', 'CLASS_NO', 
                        'CHART', 'BAR_CODE', 'MATERIAL_NAME', 'EE_DOC_ID', 'UD_DOC_ID', 'NB_DOC_ID', 'INSERT_FILE', 
                        'STORAGE_METHOD', 'VALID_TERM', 'REEXAM_TARGET', 'REEXAM_DATE', 'PACK_UNIT', 'EDI_CODE', 
                        'CANCEL_DATE', 'CANCEL_NAME', 'TYPE_CODE', 'TYPE_NAME', 'CHANGE_DATE']
        
        df3 = pd.read_csv("/home/lab06/material.csv")
        df3 = df3[mate_columns]
        engine3 = create_engine("postgresql://postgres:1111@localhost:5432/project")
        df3.to_sql(DrugMaterial._meta.db_table, if_exists='append' ,con=engine3, index=False)