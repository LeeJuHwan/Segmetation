import requests
from bs4 import BeautifulSoup

def call_by_url():

    #DB에서 가져온 ITEM_SEQ정보
    item_seq = "200808876"

    #template에 전달할 딕셔너리
    info_dict = {}

    # 식별자_URL
    identify_url = r"https://apis.data.go.kr/1471000/MdcinGrnIdntfcInfoService01/getMdcinGrnIdntfcInfoList01?serviceKey=SgmrRsA%2Bn%2B%2F81ytbTTkOeya48YDYcqlTX%2FcxX%2Fy7Bh1WSJ9t4cPUUNMqaGvIjO%2Bq28Ix9qe%2BMO0Z7KB%2FIGUBfg%3D%3D&item_seq="

    # 성분_URL
    material_url = r"https://apis.data.go.kr/1471000/DURPrdlstInfoService02/getDurPrdlstInfoList2?serviceKey=SgmrRsA%2Bn%2B%2F81ytbTTkOeya48YDYcqlTX%2FcxX%2Fy7Bh1WSJ9t4cPUUNMqaGvIjO%2Bq28Ix9qe%2BMO0Z7KB%2FIGUBfg%3D%3D&itemSeq="

    # 용법 URL
    usage_url = r"https://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList?serviceKey=SgmrRsA%2Bn%2B%2F81ytbTTkOeya48YDYcqlTX%2FcxX%2Fy7Bh1WSJ9t4cPUUNMqaGvIjO%2Bq28Ix9qe%2BMO0Z7KB%2FIGUBfg%3D%3D&itemSeq="

    # 식별자 URL에서 정보 가져오기
    identify_request = requests.get(identify_url+item_seq)
    identify_xml = BeautifulSoup(identify_request.text, "xml")

    identify_item = identify_xml.find("item")

    info_dict["name"] = identify_item.find("ITEM_NAME")
    info_dict["seq"] = identify_item.find("ITEM_SEQ")
    info_dict["comp"] = identify_item.find("ENTP_NAME")
    info_dict["pirnt_front"] = identify_item.find("PRINT_FRONT")
    info_dict["pirnt_back"] = identify_item.find("PRINT_BACK")
    info_dict["color"] = identify_item.find("COLOR_CLASS1") + " " + identify_item.find("COLOR_CLASS2")
    info_dict["shape"] = identify_item.find("DRUG_SHAPE")

    # 성분 URL에서 정보 가져오기
    material_request = requests.get(material_url+item_seq)
    material_xml = BeautifulSoup(material_request.text, "xml")

    material_item = material_xml.find("item")

    info_dict["material"] = material_item.find("MATERIAL_NAME")


    # 용법 URL에서 정보 가져오기
    usage_request = requests.get(usage_url+item_seq)
    usage_xml = BeautifulSoup(usage_request.text, "xml")

    usage_item = usage_xml.find("item")

    info_dict["usage"] = usage_item.find("efcyQesitm")
    info_dict["method"] = usage_item.find("useMethodQesitm")
    info_dict["attention"] = usage_item.find("atpnQesitm")
    info_dict["deposit"] = usage_item.find("depositMethodQesitm")

    ## 템플릿으로 info_dict 전달
    # return template
        

