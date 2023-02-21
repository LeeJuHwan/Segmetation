import pandas as pd
from sqlalchemy import create_engine
from django.core.management.base import BaseCommand
from api.models import DrugInfo

class Command(BaseCommand):
    def handle(self, *args, **options):
        columns = ["ITEM_NAME", "ITEM_NAME_SUB", "ENTP_NAME", "CHART", "PRINT_FRONT", "PRINT_BACK", "DRUG_SHAPE", "DRUG_SHAPE2",
                "COLOR_CLASS1", "COLOR_CLASS1-투명 제외", "COLOR_CLASS2", "COLOR_CLASS2-투명 제외", "LINE_FRONT","LINE_BACK", "LENG_LONG", 
                "LENG_SHORT", "THICK", "CLASS_NAME", "ETC_OTC_NAME", "FORM_CODE_NAME", "MARK_CODE_FRONT_ANAL", "MARK_CODE_BACK_ANAL", 
                "MARK_CODE_FRONT_IMG", "MARK_CODE_BACK_IMG", "MARK_CODE_FRONT",  "MARK_CODE_BACK"]
        
        df = pd.read_excel("/home/lab06/drug_total_수정본.xlsx")
        df = df[columns]
        df.rename(columns = {'COLOR_CLASS1-투명 제외' : 'COLOR_CLASS1_투명_제외',
                    "COLOR_CLASS2-투명 제외" : "COLOR_CLASS2_투명_제외"}, inplace = True)
        engine = create_engine("postgresql://postgres:1111@localhost:5432/project")
        df.to_sql(DrugInfo._meta.db_table, if_exists='append' ,con=engine, index=False)
