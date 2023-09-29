# DRF 기반 게시판 구현 프로젝트 레파지토리
  - Django REST Framework를 기반으로, 게시판 백엔드 API 개발을 진행한 프로젝트입니다.
  - 백엔드 개발의 핵심이라 할 수 있는 항목별 C.R.U.D 구현 및 부가적 기능들을 구현하였습니다.
  - 모델 > 시리얼라이저 > 뷰 > url 플로우를 따른 개발 및 heroku를 활용한 배포까지 진행하고자 하였습니다.

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

# 유저 인증 관련 접근방법
## 세션 & 쿠키
  - 세션: 서버 쪽에서 저장하는 정보
  - 쿠키: 클라이언트의 자체적인 저장소 (그 자체로 데이터라기보다 데이터를 저장해놓는 임시 저장소의 개념)
  <img width="590" alt="세션쿠키" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/1f459a9c-64de-4455-87d0-327417f70ef3">

## 토큰 & JWT
  - 회원가입 시 유저에 매칭되는 토큰을 생성하여 저장
  - 로그인 요청이 들어오면 해당 토큰을 응답으로 보내주고, 클라이언트는 이 토큰을 잘 가지고 있다가 요청을 보낼 때 헤더에 토큰을 넣어 송신
  - 서버는 요청으로 들어온 토큰이 있는지 확인하여 인증
  - 토큰은 기본적으로 암호화 방식을 채택하여 사용
  - 각 토큰/세션에 대해 유효기간 설정을 통해 보안성 강화
  <img width="590" alt="토큰JWT" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/d20c7a0a-67db-4390-8460-bd19b0e8ac54">

# 진행 간 발생 에러 및 대응방안
##  related_name 에러
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

# 프로젝트 회고
  - 같은 작업을 serializer, view, 심지어 model에도 구현할 수 있다. 동일하게 동작하는데는 문제 없으나, 되도록 각 부분의 역할에 맞게 분리하는 것이 좋다.
  - 이것은 협업과 유지보수의 용이함을 위한 노력이다.






        
