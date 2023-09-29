# 별도 브랜치 'dev'에 구현 코드가 업로드되어 있습니다.

# DRF 기반 게시판 구현 프로젝트 레파지토리
  - Django REST Framework를 기반으로, 게시판 백엔드 API 개발을 진행한 프로젝트입니다.
  - 백엔드 개발의 핵심이라 할 수 있는 항목별 C.R.U.D 구현 및 부가적 기능들을 구현하였습니다.
  - 유저 인증 관련하여, 기본적인 토큰 방식을 적용하여 authenticated 검증이 된 경우에만 기능수행이 가능하도록 구현하였습니다.(전체 게시글 보기/게시글 작성/게시슬 수정/댓글 보기/댓글 수정/좋아요 등) 
  - 모델 > 시리얼라이저 > 뷰 > url 플로우를 따른 개발 및 heroku를 활용한 배포까지 진행하고자 하였습니다.
  - 배포 url: https://sensuous-myboard.herokuapp.com

# 기술스택
  <table>
    <thead align="center">
        <tr>
            <th><span>BE</span></th>
            <th><span>FE</span></th>
            <th><span>DB</span></th>
            <th><span>DEPLOYMENT</span></th>
            <th><span>MANAGEMENT</span></th>
        </tr>
    </thead>
    <tbody>
          <td align="center">
              <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
              <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
              <img src="https://img.shields.io/badge/insomnia-4000BF?style=for-the-badge&logo=insomnia&logoColor=white">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/react-61DAFB?style=for-the-badge&logo=react&logoColor=black"> 
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/postgresql-4169E1?style=for-the-badge&logo=postgresql&logoColor=white">
          </td>
          <td align="center">
              <img src="https://img.shields.io/badge/heroku-430098?style=for-the-badge&logo=heroku&logoColor=white">
          </td>
          <td align="center">
            <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
          </td>
    </tbody>
</table>

# 기능구현(App 별)
  - 회원 관련 기능(User)
      - 회원 Profile 관리(nickname, subjects(관심사), image(프로필 사진) 등)
      - 회원가입 기능
      - 로그인 기능
      - Profile 수정하기 기능

  # 유저 인증 관련 접근방법
  - 세션 & 쿠키
    - 세션: 서버 쪽에서 저장하는 정보
    - 쿠키: 클라이언트의 자체적인 저장소 (그 자체로 데이터라기보다 데이터를 저장해놓는 임시 저장소의 개념)
      <img width="590" alt="세션쿠키" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/1f459a9c-64de-4455-87d0-327417f70ef3">
  
  - 토큰 & JWT
    - 회원가입 시 유저에 매칭되는 토큰을 생성하여 저장
    - 로그인 요청이 들어오면 해당 토큰을 응답으로 보내주고, 클라이언트는 이 토큰을 잘 가지고 있다가 요청을 보낼 때 헤더에 토큰을 넣어 송신
    - 서버는 요청으로 들어온 토큰이 있는지 확인하여 인증
    - 토큰은 기본적으로 암호화 방식을 채택하여 사용
    - 각 토큰/세션에 대해 유효기간 설정을 통해 보안성 강화
      <img width="590" alt="토큰JWT" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/d20c7a0a-67db-4390-8460-bd19b0e8ac54">

  - 게시글 관련 기능(Post C.R.U.D)
      - 게시글 생성
      - 특정 게시글 1개 보기 / 게시글 전체 목록 보기(가져오는 갯수 제한-페이지네이션)
      - 게시글 수정하기
      - 게시글 삭제하기
      - 게시글 좋아요 기능
      - 게시글 필터링(작성자 / 좋아요)
      - 게시글 관련 API 수행 시, 기능 별 권한 설정
   
  - 댓글 관련 기능(Comment C.R.U.D)
      - 댓글 생성
      - 특정 댓글 1개 보기 / 댓글 전체 목록 보기
      - 댓글 수정하기
      - 댓글 삭제하기
      - 게시글 볼 때 댓글도 함께 가져오기

# 주요 폴더별 파일트리
<table>
    <thead align="center">
        <tr>
            <th><span>myboard</span></th>
            <th><span>posts</span></th>
            <th><span>users</span></th>
        </tr>
    </thead>
    <tbody>
          <td align="center">
              <img width="254" alt="스크린샷 2023-09-29 오후 6 05 40" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/4c5e3d13-1a0e-46dd-9101-e8f1f23a02ec">
          </td>
          <td align="center">
              <img width="415" alt="스크린샷 2023-09-29 오후 6 05 54" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/737c764e-33fd-4a9d-87df-606d65569390">
          </td>
          <td align="center">
              <img width="305" alt="스크린샷 2023-09-29 오후 6 06 05" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/ee5208f6-15e5-4a21-8105-aa4639dbef34">
          </td>
    </tbody>
</table>

# 예외처리 커스텀
  <img width="957" alt="예외처리 커스텀" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/67fc0394-992a-439a-ad14-d9cbfdb4b1de">
  - 예외처리 커스터마이징 예시 이미지 (insomnia.rest 사용 API 테스트)
  
  - exception_handler 변경을 통해 기존 단순 표기법에서 좀 더 디테일한 내용을 담아 클라이언트에 JSON 형태로 response 될 수 있도록 커스터마이징
  - 상기 이미지에는 재입력 비밀번호가 일치하지 않을 때 예외처리 상황을 보여주고 있고, 이외에도 unique field(이메일 중복검증) 충돌 등의 상황에서 예외처리가 될 수 있도록 하였습니다.
  
  - 기존
  ```python
  {
    "detail": " ... "
  }
  ```
  - 커스터마이징 후
  ```python
  {
    "message": " ... ",
    "results": " ... ",
    "status": " T or F ",
    "status_code": " HTTP_xxx ... "
  }
  ```
  
# 진행 간 발생 에러 및 대응방안
## 1. related_name 에러
  - 서로를 참조하는 관계, 즉 ForeignKey나 OneToOneField, ManyToManyField와 같은 관계에서 발생하는 에러
  - 같은 모델을 참조하는 인스턴스가 있을 경우, 반드시 related_name=''을 지정해줘야 한다. (writer, likes)
    <img width="612" alt="post 모델" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/38a933c6-13dd-4701-b332-542df3844955">
  - 위와 같은 Post 모델을 기반으로 할 떄, Post 모델 내에서는 author 필드를 통해 연결된 User 데이터를 불러올 수가 있다. (Post.author.username)
  - 그러나 그 역은 성립되지 않는다. 만약 User.post.title과 같은 방식으로 데이터에 접근하려하면 에러가 발생한다. 일방적으로 참조된 User 입장에서는 Post라는 이름을 모르기 때문이다.
## 대응방안
  - 1번째,
      ```python
      user = User.objects.get(pk=1)
      posts = user.post_set.all()
      ```
  - 2번째,
    ```python
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') - 모델 내 이름 정해준 뒤
    user = User.objects.get(pk=1)
    posts = user.posts.all()
    ```
    이렇게 해주면 유저가 작성한 글들을 확인할 수가 있습니다.

## 2. heroku 배포 시 발생 에러
  <img width="1022" alt="스크린샷 2023-09-29 오후 5 48 12" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/6dc9c079-226c-4b02-8ffc-3b805ce2b33b">

## 원인 및 대응방안
  - 원인: 마이그레이션 파일에 대한 의존성이 해결되지 않아 발생하는 문제. 의존성이 설정되지 않거나 잘못 설정된 경우, migrate 명령 실행 중에 오류가 발생할 수 있음.
  - 대응방안: 

# 프로젝트 회고
  - 코드 내 동일 작업을 serializer, view, 심지어 model에도 구현할 수 있음은 물론입니다. 어떤 방식이든 동일하게 동작하기에 문제 없으나, 되도록 각 부분의 역할에 맞게 분리하는 것이 좋습니다.
  - 이것은 협업과 유지보수의 용이함을 위해 반드시 필요한 부분이라는 것을 느낄 수 있었습니다.
  - 현재 사용중인 IDE의 버전, 프레임워크의 버전 등 버전 호환성이 맞지 않아 발생하는 오류가 생각보다 굉장히 빈번하다는 것을 느꼈습니다. 개발 시 이용하고자하는 툴의 버전과 상호 호환성에 대한 명확한 이해가
    반드시 선행되어야 함을 많이 느낄 수 있었습니다. 이는 향후 개발 시에도 유념해야 하는 부분일 것으로 생각됩니다.
  - 배포의 경우 pythonanywhere aws 등과 함께 어떤 방식을 택할지에 대해 고민하였습니다. heroku의 경우 pythonanywhere보다 난이도는 높지만, 더 좋은 성능과 실행 경험을 가지기에 선택하게 되었습니다.
  - 배포의 과정에서 여러 에러들을 만나게 되었지만, 이를 하나씩 해결해나가면서 배운 지식을 향후 서비스 배포 시 적극 활용할 수 있을 것으로 기대하고 있습니다.
  - 또한, 앞으로 상황에 따라 최적합한 방식을 스스로 찾아낼 수 있도록 좀 더 다양한 프로젝트 수행을 통해 역량을 키우고자 합니다.

