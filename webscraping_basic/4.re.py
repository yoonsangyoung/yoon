import re

p = re.compile("ca.e")   # ca#e  패턴을 가져옴   
# . (ca.e): 하나의 문자를 의미 case cafe care
# ^ (^de): 문자열의 시작 desk,destination
# $ (se$): 문자열의 끝 > case, base

p = re.compile("원하는 형태")
m = p.match("비교할 문자열") #  주어진 문자열의 처음부터 일치하는지 확인
m = p.search("비교할 문자열") # 주어진 문자열 중에 일치하는게 있는지 확인
m= p.findall("careless") # findall : 일치하는 모든 것을 리스트 형태로 반환

###
m=p.match("case")
print(m.group()) #매치 되지 않으면 에러 발생
if m:
    print(m.group())

m=p.group()("good care") #주어진 문자열의 일치하는게 있는지

m=p.string()("good care") # 입력받은 문자열
m=p.start()("good care") #일치하는 문자열의 시작 index
m=p.end()("good care")  #일치하는 문자열의 끝 index
m=p.span()("good care") #일치하는 문자열의 시작/끝 index

