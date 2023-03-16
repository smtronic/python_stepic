#  переменной result хранился словарь,
#  в котором для каждого символа строки text будет подсчитано количество его вхождений.
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# result = {}
# for c in text:
#     result[c] = result.get(c, 0) + 1

result = {char: text.count(char) for char in set(text)}
