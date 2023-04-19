# Garbage-Classification-Project

MS AI Shcool을 진행하며 진행한 첫 번째 프로젝트입니다.


![이성규 포트폴리오-B (23 04 19)](https://user-images.githubusercontent.com/101550112/233021638-8dc4909b-2c96-4def-a652-c5cdfc47eb23.png)
![이성규 포트폴리오-B2 (23 04 19)](https://user-images.githubusercontent.com/101550112/233021648-7f05077c-d08e-4efb-9a1e-e6149c1649ee.png)

전체 프로그램 설명 URL :  https://youtu.be/FOzfgKr11-c


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

프로그램 실행시 기본적으로 나오는 화면입니다.


![실행 1](https://user-images.githubusercontent.com/101550112/233073018-1f528efd-afe2-4e58-9ad3-5752d92ef714.png)

<br>

<img src="https://user-images.githubusercontent.com/101550112/161672465-403e763d-3fd1-4276-befe-4b48137b7e84.png" width="80%" height="80%"/>


#### ① : 검색 기능. 원하는 카테고리와 코로나 위험도를 설정하여 검색.
#### ② : 코로나 기능. 코로나 확진자 발생지 기준 100m 원 표시.
#### ③ : 거리 측정 기능. 체크한 후 맵 좌클릭을 통해 거리 측정 가능. 우클릭으로 거리 측정 종료.
#### ④ : 카테고리 버튼. 토글 버튼 클릭시 맵상에 토글버튼 해당 카테고리 마크 표시.
#### ⑤ : 맵 이동 버튼. 전북대 근처 자취집이 많은 네 장소 선정, 클릭시 맵 변겅.

<br>

카테고리 버튼에서, 집카테고리를 활성화 시킨후 클릭하게 되면 다음과 같은 창이 뜨게됩니다.

![창](https://user-images.githubusercontent.com/101550112/161676213-1e096d4d-b59a-46d6-974e-eb29127a07ec.png)


이 창에선 탭을 통해 정보 및 인테리어를 해볼수 있습니다.

![창2](https://user-images.githubusercontent.com/101550112/161676563-f2df7259-35c8-48f3-a82d-30bf77d5b024.png)

<br>

## 프로그램 구조

![apdls](https://user-images.githubusercontent.com/101550112/161677083-d89679dc-8bd8-4d39-add2-0581c497d409.png)


프로그램은 크게 다음과같이 세 부분으로 나누어 생각할 수있습니다.

1. 프로그램을 실행할때 띄워지는 Map window 창

2. Map Window 창 안에 선언되어있는 WebBrowser 컨트롤

3. WebBrowser 컨트롤을 통해 띄워지는 집 정보 창.

이 세 부분은 WPF 부분과 Web 부분으로 구분됩니다.

MapWindow에서 버튼을 누르는 등 특정 이벤트를 발생시키면 WPF에서 Web으로 신호가 보내지게 되고 이에 Web에서는 신호에 맞는 동작을 합니다.
반대로 웹 브라우저인 맵 위의 있는 집을 클릭하게 되면 그 클릭한 집에 해당하는 집 API 정보를 WPF에 전달하여 집 정보창을 열게됩니다.

## 구현 첼린지

프로그램을 만들며 여러 첼린지들이 존재하였습니다.

### 1. HTML
프로그램 상에서 카카오 지도 API를 사용하여 지도를 표현하고자 하였습니다. 그러나 카카오 지도 API는 HTML형식으로 사용해야했고, XAML 상에서 Web Browser 컨트롤을 통해 사용하게 되었습니다. 문제는 저를 포함하여 팀원 모두 HTML을 다룰줄 아는사람이 없었습니다. 저는 이를 해결하기 위해 완벽하게는 작성하지 못하더라도 비슷하게 모양만이라도 따라 구현할수 있도록 인터넷을 통해 카카오 API관련 HTML을 독학을 하였습니다.  프로그램을 제작하며 시간에 쫓겨 혼자 독학을 했기때문에 제대로 배우지 못하여 하드코딩부분이 매우 많았지만, 여러 인터넷의 예제 코드들을 복합적으로 결합하여 나름 제가 원하는 모양대로 HTML 제작을 해낼수 있었습니다. 

### 2. 서버
1번에서 언급하였듯, 카카오 지도 API를 사용하려면 HTML을 사용해야했습니다. HTML을 작성한 후 이를 표현해줄 서버가 필요했고, 저는 경험이없어서 살짝 애를 먹었습니다. 결국 서버 지원 사이트를 이용하여 임시적으로 몇일간 서버를 여는식으로 해결해 냈습니다. 

도움을 받은 사이트 : https://tiiny.host/manage

### 3. MVVM 패턴
MVVM 패턴적용 관련하여 어려움이 있었습니다. 저희는 프로그램에 앞서 이야기한 지도 API를 활용하여 Web Browser를 띄웠습니다. 그리고 특정 신호를 보내어 Web Browser가 그 신호에 맞게 변화하게 하고싶었습니다. 이는 Invoke Script라는 메소드를 통해 할 수 있었는데, XAML에서는 호출이 안되는 메소드였습니다. 

이는 Exception from HRESULT: 0x80020006 (DISP_E_UNKNOWNNAME) 가 발생하게 되는데
http://msdn.microsoft.com/en-us/library/cc491132.aspx 에 따르면 'InvokeScript (String)를 구현하는 문서가로드를 완료하기 전에 호출해서는 안됩니다. LoadCompleted 이벤트가 발생하여 문서로드가 완료되면 감지 할 수 있습니다. ' 라는 조건이 있었기 때문입니다. 

( = 메인 윈도우가 생성되는 InitializeComponent(); 메인 윈도우 생성이후 그 컨트롤 자체에 직접 접근해야함. )

즉 View 인 디자인 코드에서는 호출이 안되므로 ViewModel에서 직접 Web Browser 컨트롤에 접근하여 Invoke Script메소드를 호출할 방법이 필요했던 것입니다. 사실상 View의 코드 비하인드에서 직접 메소드를 호출한다면 매우 쉽게 Invoke Script를 호출할 수 있었겠으나, MVVM 패턴을 고려하기때문에 생긴 기술적 어려움 이였습니다. 이에 대한 해결 방안으로는 ViewModel에서 Web Browser 컨트롤을 하나 갖도록 구현하고, View에서 그 Web Browser 컨트롤을 바인딩 하도록 구현하여 해결하였습니다.


![바인딩](https://user-images.githubusercontent.com/101550112/161678358-7762583c-a148-4630-bdd4-4a15693f9c8f.png)

<br>

### 4. 같은 윈도우 폼, 다른 datacontext ( MVVM 패턴 )

프로그램의 맵 상에서 집을 클릭할 때 새로운 윈도우가 열립니다. 이때 윈도우는 생성할 때마다 같은 XAML파일, 즉 같은 윈도우 폼이지만 서로 다른 데이터를 가진 객체를 datacontext로써 갖도록 구현하고 싶었습니다. 정확히 말하면, WebBrowser로부터 API를 요청하는데 쓰이는 특정 정보를 받고 그 정보에 따라 다른 방 정보를 가진 객체를 DataCotext로 갖도록 구현하고싶었습니다.

![첼린41](https://user-images.githubusercontent.com/101550112/161681625-33fc446e-7daa-4fb1-be8d-dfaf65c71db7.png)

이는 윈도우 창이 열릴때 Web에서 받은 정보를 통해 DataContext를 생성해야하는데, XAML상에서 리소스로써 선언 해줄 때 인자를 받으며 생성하도록 하는 방법을 찾지 못했습니다. ( MVVM 패턴으로 비하인드 코드에는 작성을 하지 않기위해 XAML에서 DataContext를 해결하고자함. )

![첼린42](https://user-images.githubusercontent.com/101550112/161681695-40691488-46b5-418a-ab43-8c1de3dafe9d.png)

그렇다면 생성할때 인자를 받지 않고 VM(DataContext)를 생성한 이후 Web에서 정보를 받아 VM이 가진 정보를 변경해야 했는데, Web에서 WPF로의 정보 전달은 따로 Web으로부터 정보를 받을 수 있도록 클래스에서 정의가 추가적으로 필요했습니다. 이 정의가 추가된 클래스들은 Web에서 정보 받을때 호출될 함수를 갖고있는 클래스입니다.

그러면 VM을 이 웹과 정보를 받는 클래스로 정의하여 새로운 윈도우 마다 생성해 Datacontext로 설정하고, 정보를 받으면 될거란 생각을 했습니다.
그러나 그렇게 하게된다면 모든 VM 클래스가 Web과 반응하는 클래스로 되어있고 호출 함수의 이름이 모두 동일하기 때문에 Web으로부터 정보 전달을 받을때 모든 존재하는 VM의 함수가 호출되어 오류가 생길수 있으며(결론적으로 모두 정보가 동일하게 변경될 수 있음.), 겨우 생성할때 한번 Web으로 부터 정보를 받기 위해 모든 VM을 Web과 소통 가능한 클래스로 만드는게 비효율적이고 소모적이였습니다.

![첼린43](https://user-images.githubusercontent.com/101550112/161681834-0f99456c-a813-413e-8375-c7a9aaf8ea7c.png)

그렇다면 VM로 쓰일 클래스는 웹에서 정보를 받는 클래스가 아니며, 생성할때 각자 다른 정보를 갖도록 구현해 줘야했습니다.

MVVM 패턴을 유지하기 위해 XAML에서 인자를 안받고, 비하인드 코드에서도 작성하지 않는 조건으로 구현할 방법이 이처럼 잘 떠오르지 않아 구현에 큰 첼린지가 있었습니다.


#### 해결 
Web 전달을 받을 클래스를 정의한 후 클릭하면 Web으로부터 날라온 정보를 인자로 받아 VM과 View 창 둘다 생성하고 XAML이 아닌, 그 클래스 코드 상에서 View.Context = VM으로 명시를 통해 DataContext를 할당 해주어 해결하였습니다.

단, 이로인해 XAML에서는 윈도우를 생성하기전에는 VM이 없으므로 XAML 코드적으로 VM으로 접근하기가 불가능하여 구현할때 신경쓸게 많아졌습니다.

<br>

ex ) 
ItemsSource="{Binding Source={StaticResource vm}, Path=Cities}" 

이런식으로 직접적으로 vm을 명시할수 없음. 


Text="{Binding Path=Main.Temp,Converter={StaticResource KtoCConverter}}" 

VM.속성 이런식으로 VM안의 속성에 접근이 불가능해짐. 


![첼린44](https://user-images.githubusercontent.com/101550112/161682823-9c55ad5d-64ee-48a4-8b1c-b3e9a02c56e1.png)

## 한계점

### 1. 코로나 원

원래는 코로나 확진자의 동선이 자세하게 모두 공개가 되어었고, 누구나 열람이 가능했습니다.

그러나 법안 변경으로 인해 14일간만 일부 장소 목록 형태로만 공개되도록 변경되었습니다.

더욱이, 마침 프로그램을 제작할때 전주에는 14일 안에 발생한 코로나 확진자가 없었습니다.

이로인해 프로그램 지도에 표시된 코로나 원은 저희가 임의로 설정한 좌표를 사용할 수 밖에 없었습니다.

![한계1](https://user-images.githubusercontent.com/101550112/161683291-aab17cf4-2b2a-45d1-b6fb-0247f288f576.png)

### 2. 인테리어 탭 드래그 구현

원래는 인테리어탭에서 가구를 옮길때 현재 프로그램처럼 버튼으로 이동하도록 구현할 생각이 아니였습니다. 

마우스로 가구를 드래그하여 위치를 변경하도록 구현하고싶었으나, 비하인드 코드 없이 MVVM패턴으로 구현하기가 너무 어려웠고, 시간이 많이 부족했기에 차선택으로 버튼을 통해 이동하고록 구현하게 되었습니다.

### 3. 인테리어 실용성 관련

먼저, 인테리어 탭이 실용성 면에서 부족한 면이 매우 많습니다.

실질적으로 쓰이기에는 집 매물의 사진마다 모두 비율이 동일하게 적용될 수 없으며, 두번째 인테리어 탭은 사진마다 공용적으로 활용 가능한 기능이 아닙니다.
사실상 실용성은 거의 없다 봐도 무방합니다.

이는 AR관련하여 공부를 함으로써 보충이 필요할 것 같습니다.


### 4. HTML 코드와 API 활용의 하드코딩

HTML과 API를 다루는데 너무나도 부족했던 저 였기에, 코드가 매우 하드코딩 및 비효율적 입니다.

특히 검색 기능의 코드를 보면 정보를 필터링 해서 찾아내는 것이아닌, 순수 노가다성 코드로 일일이 직접 구현이 되어있습니다.

API활용 또한, 매번 새로운 매물이 올라올때마다 갱신되는 것이 아닌 현재 (제작할 때 당시) 집 매물만 존재하도록 구현이 되어있습니다.

이는 시간과 실력이 부족했기에 나타난 프로그램의 완성도 문제라 생각합니다.

### 5.서버가 없을시 작동하지 않는 프로그램

4번과 동일한 원인으로 볼 수 있습니다. 

HTML을 이용하여 서버를 만드는 것에 매우 미숙하였고, 영구적으로 서버를 만들지 못했습니다. 

이는 프로그램을 실행할때, 서버가 개설되 있지 않을경우 Web Browser가 작동하지않아 프로그램 기능 자체가 활용 되지 못하는 것을 볼 수 있습니다.


<br>

#### 전체적으로 볼때, 시간과 실력에 비해 맞지않는 무모한 프로그램을 계획했다고 생각합니다. 
#### 프로그램의 코딩은 대부분 하드코딩으로 실용성이 매우 낮습니다. 스스로의 부족함을 더욱이 상기하게된 프로젝트였다고 생각합니다.

<br>

## 프로그램 실행

한계점에서도 언급 되어있듯, 실행하기전 서버 갱신이 필요합니다.

Program 폴더에서 자세히 설명하겠습니다. 

실행을 원하시는 분은 Program 폴더로 들어가 주십시오.

<br>
