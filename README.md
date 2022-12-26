## Overview

1. 인천데이터포털에서 군/구별 하루 평균 근로시간과 월평균 가구소득의 데이터를 가져왔습니다.

2. 데이터 분석에 용이하게 하기위해 jupyter notebook 을 사용하여 같은 컬럼인 군구로 merge하여 하나의 데이터 프레임으로 만들었습니다.

3. 하나로 만든 데이터 프레임을 csv 파일로 새로 저장하였습니다.

4. 하나로 합친 csv 파일을 jupyter notebook 에서 분석했습니다.

5. 분석한 자료를 visual studio code 에 코드를 작성하였습니다.

6. visual studio code 를 AWS의 EC2 서버에 연결시킨 후 streamlit 웹 대시보드를 생성하였습니다.

7. 터미널 접속을 끊어도 대시보드가 계속 유지되도록 백그라운드로 실행하였습니다.



## Repository File Structure

1. new_project.py: 앱 실행시 기초 베이스가 되는 파일
2. main.py: 가장 먼저 보여지는 메인화면
3. data_table.py: 데이터를 표 형태로 출력
4. data_chart.py: 데이터를 분석하여 차트 형태로 출력


## use library
streamlit
```
pip install streamlit
```

pandas
```
pip install pandas
```

matplotlib
```
pip install matplotlib
```

seaborn
```
pip install seaborn
```

plotly
```
pip install plotly
```


## Screenshots
![캡처3](https://user-images.githubusercontent.com/120348588/209498706-7b38aee9-af3b-453e-a8ea-1b55c0085a7f.PNG)

![캡처](https://user-images.githubusercontent.com/120348588/209498832-ce85394d-8f8f-4c3f-b097-4651942145ee.PNG)

![캡처11](https://user-images.githubusercontent.com/120348588/209498834-5a68afd3-7cc2-4d6a-a2bd-e28f550e87e2.PNG)

![캡처4](https://user-images.githubusercontent.com/120348588/209498835-4b70a543-9b0a-42cf-893b-b081ec40fe90.PNG)






## Dataset

인천광역시 인천데이터포털

https://www.incheon.go.kr/data/DATA010201/view?docId=15066303

https://www.incheon.go.kr/data/DATA010201/view?docId=15066292
