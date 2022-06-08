from googletrans import Translator

a = Translator()
print(a.translate("Мобильная робототехника", dest='ru').text)
