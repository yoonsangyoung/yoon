#원하는 데이터 찾기

from openpyxl import workbook
wb = workbook("sample.xlxs")
ws = wb.acitve

for row in ws.iter_rows(min_row=2):
    if row[1].value > 80:
        print(row[0].value) 
        
for row in ws.iter_rows(min_row=1):
    for cell in row:
        if cell.value == "영어":
            cell.value == "컴퓨터"   # 엑셀의 파일 변경
            
ws.insert_rows(8) # row 8번째 줄 삽입
ws.insert_rows(8,5) # row 8번째 줄 위치에 5줄을 추가 

ws.insert_cols(2) # B번째 열이 비워짐 (새로운 빈 열이 추가)
ws.insert_cols(2,3) # B번째 열부터 3열 추가 (새로운 빈 열이 추가)

ws.delete_rows(8) # 8번째 줄에 데이터 삭제
ws.delete_rows(8,3) # 8번째 줄부터 세줄 데이터 삭제

ws.delete_cols(2) # 2번째 열에 데이터 삭제
ws.delete_rows(2,2) # 2번째부터 2줄 데이터 삭제

ws.move_range("B1:C11",row=0,cols=1)  # 이동하려는 범위를 cols 1칸 만큼 이동

#차트 생성
from openpyxl.chart import BarChart,Reference
#B2:C11 까지의 데이터를 차트로 생성
bar_value = Reference(ws, min_row=2, max_row=11, min_col=2, max_col=3)
bar_chart = BarChart() # 차트의 종류 설정 (bar,line,pie)
bar_chart.add_data(bar_value) # 차트 데이터 추가

#그후 bar_chart를 ws에 넣어주면 됨
ws.add_chart(bar_chart, "E1") # 차트 넣은 위치 정의

