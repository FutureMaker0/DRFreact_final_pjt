# DRFreact_final_pjt
DRF, react 기반 게시판 구현 파이널 프로젝트 레파지토리

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
  <img width="594" alt="토큰JWT" src="https://github.com/FutureMaker0/DRFreact_final_pjt/assets/120623320/d20c7a0a-67db-4390-8460-bd19b0e8ac54">
