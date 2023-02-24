import requests

headers = \
{'User-Agent':'Mozilla/5.0 (windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

url = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest' # 오늘의 유머 베스트오브베스트 링크 입력
site = requests.get(url, headers=headers)  # 내용 가져오기
source_data1 = site.text  # 인터넷소스코드를 source_data변수에 저장

count1 = source_data1.count('"subject"><a href="')  #  베스트오브베스트 글제목 링크  개수 가져오기

for i in range(count1):  # 해당 개수만큼 반복
      pos1 = source_data1.find('"subject"><a href="')+ len('"subject"><a href="')  # 글링크  앞 부분위치 지정
      source_data1 = source_data1[pos1:]  # 해당 위치로 이동

      pos2 = source_data1.find('" target="_top">')  # 글링크  뒷부분 위치 지정
      a_data = source_data1[:pos2]  # 앞부분 부터 뒷부분까지 내용추출후 저장

      pos3 = source_data1.find('=1" target="_top">')+ len('=1" target="_top">')  # 글제목 앞부분 위치 저장
      source_data1 = source_data1[pos3:]  # 해당위치로 이동

      pos4 = source_data1.find('</a><span class=')  # 글제목 뒷부분 위치 지정
      b_data = source_data1[:pos4]  # 앞부분부터 뒷부분까지 내용추출후 저장

      url = 'https://www.todayhumor.co.kr'+a_data  # 베스트오브베스트 메인화면이 아닌 글내부의 링크 입력
      site = requests.get(url, headers=headers)  # 내용 가져오기
      source_data2 = site.text  # 인터넷 소스코드를 source_data변수에 저장
       
      count2 = source_data2.count('<p>    <img src=')  # 이미지 링크  제목 개수 가져오기

      for i in range(count2):  # 해당 개수만큼 반복
            pos5 = source_data2.find('<p>    <img src=')+ len('<p>    <img src=')  # 이미지링크 앞 부분위치 지정
            source_data2 = source_data2[pos5:]  # 해당위치로 이동

            pos6 = source_data2.find('alt="')  # 이미지링크  뒷부분 위치지정
            c_data = source_data2[:pos6]  # 앞부분부터 뒷부분까지 내용추출후 저장
            
            source_data2 = source_data2[pos6+1:]  # 다음 링크를 찾기위해 뒷부분이동시키기
            print(i+1, a_data, b_data, c_data)  # a_data, b_data, c_data를 화면에 출력하기
 
