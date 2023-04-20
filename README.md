# Garbage-Classification-Project

MS AI Shcool을 진행하며 진행한 첫 번째 프로젝트입니다.


![이성규 포트폴리오-B (23 04 19)](https://user-images.githubusercontent.com/101550112/233021638-8dc4909b-2c96-4def-a652-c5cdfc47eb23.png)
![이성규 포트폴리오-B2 (23 04 19)](https://user-images.githubusercontent.com/101550112/233021648-7f05077c-d08e-4efb-9a1e-e6149c1649ee.png)

전체 프로그램 설명 URL :  https://youtu.be/FOzfgKr11-c
<br>
<br>
<br>

Classification 문제 해결 폴더 - 과제로 나온 문제해결 관련 자료

쓰레기 분리수거 폴더 - 전처리 및 실행 코드 존재

프로젝트발표 - 전체 프로그램 설명 URL의 발표 내용 제작에 사용된 코드 및 자료


## 개요
Classification모델을 활용한 쓰레기 분류 프로그램입니다.

사진을 입력 받아 어떤 종류의 쓰레기인지 분류하는 기능


해당 사진이 어떤 쓰레기인지 따라 분리수거 방법 및 재활용 용도 제공


해당 쓰레기에 대한 정보 알아볼 수 있는 검색 기능


쓰레기 이미지 생성 기능

<br>

## 기술
구현 도구 : Visual Studio Code

구현 코드 : Python

<br>

## 실행 화면

### ※ 자세한 작동기전은 영상을 참고해주세요. ( https://youtu.be/FOzfgKr11-c )

<br>

프로그램 실행시 다음과 같이 3개의 탭이 있습니다.


![image](https://user-images.githubusercontent.com/101550112/233297295-89ab3b2d-2568-4aa8-9467-4fccebda1e37.png)

1번 탭 Image Upload : 직접 이미지 파일을 올려서 쓰레기를 분류해 봅니다.

![image](https://user-images.githubusercontent.com/101550112/233296961-479fd597-ecfe-4112-b651-56a4dee99a1b.png)

2번 탭 Using WebCam : 내장되어있는 캠을 통해 이미지를 생성하고 쓰레기를 분류합니다.

![image](https://user-images.githubusercontent.com/101550112/233304292-7bfe2f15-8593-461c-b9ce-e0bbee21ea77.png)

3번 탭 Making Image : 원하는 쓰레기 이미지를 생성하여 해당 이미지를 갖고 해당 프로그램을 테스트 해봅니다.

![image](https://user-images.githubusercontent.com/101550112/233321363-f3b6eca3-1f10-4920-aa0e-e67a46f6a158.png)

<br>

각 탭마다 아래에는 다음과 같이 3개의 라디오 버튼이 있는데, 넣은 이미지의 쓰레기 종류를 파악하여 정보를 제공해 줍니다.

![image](https://user-images.githubusercontent.com/101550112/233424128-5581c757-c248-4cb8-b6d9-adafb255df20.png)


#### ① : 검색 기능. 원하는 카테고리와 코로나 위험도를 설정하여 검색.
#### ② : 코로나 기능. 코로나 확진자 발생지 기준 100m 원 표시.
#### ③ : 거리 측정 기능. 체크한 후 맵 좌클릭을 통해 거리 측정 가능. 우클릭으로 거리 측정 종료.
#### ④ : 카테고리 버튼. 토글 버튼 클릭시 맵상에 토글버튼 해당 카테고리 마크 표시.
#### ⑤ : 맵 이동 버튼. 전북대 근처 자취집이 많은 네 장소 선정, 클릭시 맵 변겅.

<br>

카테고리 버튼에서, 집카테고리를 활성화 시킨후 클릭하게 되면 다음과 같은 창이 뜨게됩니다.

![창](https://user-images.githubusercontent.com/101550112/161676213-1e096d4d-b59a-46d6-974e-eb29127a07ec.png)

![image](https://user-images.githubusercontent.com/101550112/233424513-59de4535-2ee8-4174-974f-431e3e5fd31b.png)
<br>
