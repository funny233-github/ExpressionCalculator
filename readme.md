#SUMMARY
- 通过读取字符串的算式来计算
- "(1+1)*4" -> 8

#EXAMPLE
```python
import calculate as cal
expression = "-(-.23+5-++1)+1+1+1/2"
test = cal.expressionCalculator(expression)
print(test.result)
```
