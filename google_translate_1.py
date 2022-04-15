from googletrans import Translator#匯入套件
from pprint import pprint
import googletrans

translator = translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])#如果不能使用，請參考下網站更新至最新版<https://exerror.com/googletrans-attributeerror-nonetype-object-has-no-attribute-group/>
print(googletrans.LANGCODES)#查看可接受語系
translation1 = translator.translate("Hola como estas ?", dest='ja')
print(translation1.text)#翻譯成日文
translation3 = translator.translate('不應該懶惰', src='zh-tw',dest="en")
print(translation3.text)#輸入要翻譯的字詞,src來表來源語系,dest是輸出語系
translation4 = translator.detect('不應該懶惰')#偵測語言
print(translation4)
