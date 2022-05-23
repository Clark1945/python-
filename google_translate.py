from googletrans import Translator#匯入套件
from pprint import pprint
import googletrans

translator = translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])#如果不能使用，請參考下網站更新至最新版<https://exerror.com/googletrans-attributeerror-nonetype-object-has-no-attribute-group/>
#print(googletrans.LANGCODES)#查看可接受語系


print("-------------------------------------")
print("\n簡易翻譯系統！\n")
print("輸入1：中文翻譯英文")
print("輸入2：中文翻譯日文")
print("輸入3：中文翻譯義大利文")
print("輸入4：任意文翻譯中文")
print("輸入-1：關閉系統")
print("--------------------------------------")
selection=0
while (selection != -1):
  selection=int(input("輸入動作"))
  if selection==1:
    inputText=input("輸入原文：")
    translationEn = translator.translate(inputText, dest='en')
    print(translationEn.text)
  if selection==2:
    inputText=input("輸入原文：")
    translationJp = translator.translate(inputText, dest='ja')
    print(translationJp.text)
  if selection==3:
    inputText=input("輸入原文：")
    translationIt = translator.translate(inputText, dest='en')
    print(translationIt.text)
  if selection==4:
    inputText=input("輸入原文：")
    translationIt = translator.translate(inputText, dest='zh-tw')
    print(translationIt.text)

print("\n運作完成！")