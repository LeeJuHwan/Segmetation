from rembg import remove
import cv2
import torch
from PIL import Image

class YOLO_model:
    
    def __init__(self):
        # Model
        self.model = torch.hub.load('YOLO/yolov5', 'custom', path='YOLO/best.pt', force_reload=True)
        
        
    def detect(self, pil_img):
        gray_img = pil_img.convert("L")
        result = self.model([gray_img], size=416)
        pos_list = result.pandas().xyxy[0]
        result_list = []
        
        for idx, pos in pos_list.iterrows():
            
            width = pos['xmax'] - pos['xmin']
            height = pos['ymax'] - pos['ymin']
            
            cropped_image = pil_img.crop((max(pos['xmin']-int(0.1*width), 0), max(pos['ymin']-int(0.1*height), 0), min(pos['xmax']+int(0.1*width), pil_img.width), min(pos['ymax']+int(0.1*height), pil_img.height)))
            result_list.append(cropped_image)
            
        return result_list
    
class color_model:
    
    def __init__(self):
        self.color_list = [
        "grey",
        "white",
        "red",
        "orange",
        "yellow",
        "light-green",
        "green" ,
        "blue-green",
        "blue",
        "indigo",
        "violet",
        "pink",
        "magenta" ]
    
    def get_color(self, opencv_img, include_near=False, is_pill=False):
        
        color_map = cv2.cvtColor(opencv_img, cv2.COLOR_BGR2HSV)
        color_dict = {color:0 for color in self.color_list}
        
        white_aspect = 0
        
        for color_row in color_map:
            for h, s, v in color_row:
                h_360 = h*2
                
                if(s<50 and v>120):
                    white_aspect += 1

                if(v<70):
                    continue
                elif(s<25):
                    if(v<150):
                        color_dict["grey"] += 1
                    else:
                        color_dict["white"] += 1
                    continue

                if(h_360<15 or h_360>=345):
                    color_dict["red"] += 1
                elif(15<=h_360<40):
                    color_dict["orange"] += 1
                elif(40<=h_360<65):
                    color_dict["yellow"] += 1
                elif(65<=h_360<85):
                    color_dict["light-green"] += 1
                elif(85<=h_360<140):
                    color_dict["green"] += 1
                elif(140<=h_360<165):
                    color_dict["blue-green"] += 1
                elif(165<=h_360<205):
                    color_dict["blue"] += 1
                elif(205<=h_360<245):
                    color_dict["indigo"] += 1
                elif(245<=h_360<295):
                    color_dict["violet"] += 1
                elif(295<=h_360<325):
                    color_dict["pink"] += 1
                elif(325<=h_360<345):
                    color_dict["magenta"] += 1
        
        result_list = []
        
        sum_nonblack = sum(color_dict.values())+1
        color_percent = {k : (v / sum_nonblack * 100) for k, v in color_dict.items()}
        sorted_percent = sorted(color_percent.items(), key=lambda x: x[1], reverse=True)
        white_percentage = white_aspect / sum_nonblack * 100
        
        if(sum_nonblack<10):
            result_list.append("black")
        else:
            result_list.append(sorted_percent[0][0])
            if(is_pill):
                if(sorted_percent[0][1]-sorted_percent[0][1]<30):
                    result_list.append(sorted_percent[0][1])
        
        if(include_near):
            additional_list = []
            for color in result_list:
                if(color=="black"):
                    additional_list.append("grey")
                    continue
                elif(color=="white"):
                    additional_list.append("grey")
                    continue
                elif(color=="grey"):
                    additional_list.append("white")
                    additional_list.append("black")
                    continue

                h_color_list = self.color_list[2:]
                color_idx = h_color_list.index(color)
                
                additional_list.append(h_color_list[(color_idx-1)%len(h_color_list)])
                additional_list.append(h_color_list[(color_idx+1)%len(h_color_list)])
                
            result_list += additional_list
            
            print(white_percentage)
            if("white" not in result_list and white_percentage>70):
                result_list.append("white")
            
        return result_list, color_percent
