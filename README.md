# DRFreact_final_pjt
DRF, react 기반 게시판 구현 파이널 프로젝트 레파지토리
- 같은 작업을 serializer, view, 심지어 model에도 구현할 수 있다. 동일하게 동작하는데는 문제 없으나, 되도록 각 부분의 역할에 맞게 분리하는 것이 좋다.
- 이것은 협업과 유지보수의 용이함을 위한 노력이다. 

# 세션 & 쿠키
  - 세션: 서버 쪽에서 저장하는 정보
  - 쿠키: 클라이언트의 자체적인 저장소 (그 자체로 데이터라기보다 데이터를 저장해놓는 임시 저장소의 개념)
  <img width="590" alt="세션쿠키" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/1f459a9c-64de-4455-87d0-327417f70ef3">

# 토큰 & JWT
  - 회원가입 시 유저에 매칭되는 토큰을 생성하여 저장
  - 로그인 요청이 들어오면 해당 토큰을 응답으로 보내주고, 클라이언트는 이 토큰을 잘 가지고 있다가 요청을 보낼 때 헤더에 토큰을 넣어 송신
  - 서버는 요청으로 들어온 토큰이 있는지 확인하여 인증
  - 토큰은 기본적으로 암호화 방식을 채택하여 사용
  - 각 토큰/세션에 대해 유효기간 설정을 통해 보안성 강화
  <img width="590" alt="토큰JWT" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/d20c7a0a-67db-4390-8460-bd19b0e8ac54">

# related_name 에러
  - 서로를 참조하는 관계, 즉 ForeignKey나 OneToOneField, ManyToManyField와 같은 관계에서 발생하는 에러
  - 같은 모델을 참조하는 인스턴스가 있을 경우, 반드시 related_name=''을 지정해줘야 한다. (writer, likes)
  <img width="612" alt="post 모델" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/38a933c6-13dd-4701-b332-542df3844955">
  - 위와 같은 Post 모델을 기반으로 할 떄, Post 모델 내에서는 author 필드를 통해 연결된 User 데이터를 불러올 수가 있다. (Post.author.username)
  - 그러나 그 역은 성립되지 않는다. 만약 User.post.title과 같은 방식으로 데이터에 접근하려하면 에러가 발생한다. 일방적으로 참조된 User 입장에서는 Post라는 이름을 모르기 때문이다.
  - 이를 해결할 수 있는 방법이 있는데,
      - 1번째,
        ```
        user = User.objects.get(pk=1)
        posts = user.post_set.all()
        ```
      - 2번째,
        ```
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts') - 모델 내 이름 정해준 뒤
        user = User.objects.get(pk=1)
        posts = user.posts.all()
        ```
        이렇게 해주면 유저가 작성한 글들을 확인할 수가 있습니다.





        
