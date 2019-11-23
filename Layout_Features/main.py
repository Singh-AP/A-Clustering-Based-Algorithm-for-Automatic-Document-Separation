import pytesseract
from pytesseract import Output
import cv2

def LayoutFeatures(dirs):
    """
    input: dirs= List of strings of relaative path of images
    output: layoutData= Dict(
                                { imageNumber:{
                                                AvgWordheight=float,
                                                AvgCharWidth=float,
                                                AvgWordSpacing=float,
                                                AvgLineSpacing=float
                                            }
                                }
                            )
    What this does?
    -Reads image files from  given folder
        -for every image, gets the
                    avg word height
                    avg char width
                    word spacing
                    avg line spacing
    """
    DictLayoutFeatures={}
    imageIndex=0
    for dir in dirs:
        img = cv2.imread(dir)
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        # TextFull=pytesseract.image_to_string(img)
        # TextSent=[x for x in TextFull.split('\n')]
        n_boxes = len(d['level'])
        n_paras=len(d['par_num'])
        n_lines=len(d['line_num'])
        print(n_boxes,n_paras,n_lines)
        # print(len(TextSent),n_boxes)
        # print(d.keys())
        AvgWordHeight=0
        AvgCharWidth=0
        TotalChars=0
        AvgWordSpacing=0
        AvgLineSpacing=0
        PrevWordCoordinateX=0
        PrevWordCoordinateY=0
        SentenceCount=0
        for i in range(n_boxes):
            (x, y, w, h,txt) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i],d['text'][i])
            """
                Among the data returned by pytesseract.image_to_data():

                    -left is the distance from the upper-left corner of the bounding box, to the left border of the image.
                    -top is the distance from the upper-left corner of the bounding box, to the top border of the image.
                    -width and height are the width and height of the bounding box.
                    -conf is the model's confidence for the prediction for the word within that bounding box. If conf is -1, that means that the corresponding bounding box contains a block of text, rather than just a single word.
            """

            AvgWordHeight+=h
            lentxt=max(1,len(txt))
            AvgWordSpacing += abs(x-PrevWordCoordinateX)
            if (abs(PrevWordCoordinateY-y)>(0.1*y)):
                SentenceCount+=1
                AvgLineSpacing+=abs(PrevWordCoordinateY-y)
            
            PrevWordCoordinateY=y
            PrevWordCoordinateX=x
            AvgCharWidth += (w/lentxt)
            TotalChars += lentxt
            # mx=max(mx,len(txt.split()))
            # if i==6:
            #     print(txt,len(txt))
            # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        AvgWordHeight/=n_boxes
        AvgCharWidth/=TotalChars
        AvgWordSpacing/=n_boxes
        AvgLineSpacing/=SentenceCount
        DictLayoutFeatures[imageIndex]=dict({"AvgCharWidth ": AvgCharWidth,"AvgWordHeight ":AvgWordHeight,"AvgLineSpacing ":AvgLineSpacing," AvgWordSpacing ":AvgWordSpacing})
        # print("AvgCharWidth ",AvgCharWidth,"AvgWordHeight ",AvgWordHeight,"AvgLineSpacing ",AvgLineSpacing," AvgWordSpacing ",AvgWordSpacing)
        imageIndex+=1
        # cv2.imshow('img', img)
        # cv2.waitKey(0)
    return DictLayoutFeatures

print(LayoutFeatures(["novel.png"]))
