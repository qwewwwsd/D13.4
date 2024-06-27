from django import template


register = template.Library()

censor_list = ["андердог", "бэкграунд", "голеадор", "коуч", "лайкать", "лузер", "ноунейм", "окей", "перформанс", "плей-аут", "скиллы", "сим-билдинг", "тренинг", "чемпионшип"]
# Слова взяты из статьи https://lenta.ru/news/2021/01/13/ne_like/

@register.filter()
def currency(value):
   value = str(value)
   for i in value.split():
      for a in censor_list:
         if i == a:
            value = value.replace(f"{i}", ("*" * len(i)))
   return f"{value}"