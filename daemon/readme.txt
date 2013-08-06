
# me2py 소개
me2py는 me2day(http://me2day.net)의 OpenAPI를 python에서 쉽게 이용할 수 있는 
모듈을 제공하고 이를 시험할 수 있는 명령어 기반의 프로그램과 단위시험 기능을 
함께 제공합니다.


# me2day 소개
me2day는 한줄 블로그 서비스입니다. 글을 쓸 수 있는 양이
150자로 제한되어 있으며, 한번 쓰고 나면 수정/삭제가 되지 않습니다.

기존 블로그 보다 가볍게 자신의 생각이나 느낌을 주변에 알릴 수 있습니다. 휴대폰 문자로도
글을 남길 수 있어서 언제 어디서나 떠오르는 생각을 여러 사람과 나눌 수 있습니다.

http://me2day.net

# me2day Open API 
다른 애플리케이션이나 웹서비스에서 http를 이용하여 me2day서비스를 이용할 수 있는 
웹기반 인터페이스입니다. 현재 다음과 같은 API를 제공합니다.

 * create_post : 지정한 회원의 미투데이 페이지에 글을 작성합니다.   
 * get_latests : 지정한 회원의 최근글을 가져옵니다.
 * get_posts: 지정한 회원의 글을 가져옵니다.
 * create_comment : 지정한 글에 댓글을 작성합니다.
 * get_comments : 지정한 글의 댓글을 가져옵니다.
 * get_person : 지정한 회원 정보를 가져옵니다.
 * get_friends : 지정한 회원의 친구목록을 가져옵니다.
 * get_settings : 개인 설정 사항을 가져옵니다.
 * noop : 사용자인증 테스트를 하거나 서버 동작상태를 검사합니다.

자세한 정보는 다음 URL을 확인하세요.
 http://codian.springnote.com/pages/86001

# me2py 요구사양
 * 운영체제
   python이 설치된 대부분의 OS를 지원합니다.
 * python 2.5.1 이상
 * 한글 입력을 위한 UTF-8지원 터미널 프로그램

# 사용방법
 * 사용자 정보 입력 
압축을 풀은 디렉토리에서 python me2day.py를 입력한 후, 사용자 정보를 입력합니다.
질문에 맞게 me2day ID, me2day User Key를 입력합니다.
me2day User Key는 me2day접속후, 관리페이지에서 확인할 수 있습니다. 

 * 명령어 사용방법
명령어는 괄호안의 단축 이름을 지원합니다.

createpost(cp) "글 본문" "태그1 태그2" 아이콘 번호
예) cp "안녕하세요... " "인사말 인사" 1

getlatests(gl) userID 
예) gl joone 

getposts (아직 지원하지 않습니다)

createcomment(cc) post_id "댓글본문"
예) cc http://me2day.net/joone/2007/08/15#12:03:09 "댓글 테스트"

getcomments(gc) post_id
예) gc http://me2day.net/joone/2007/08/15#12:03:09 

getperson(gp) userID 
예) gp joone

getfriends(gf) userID 범위(all, close, family)
예) gf joone all

getsettings(gs) 
예) gs

# 단위테스트 실행
python me2day_test.py


# 개발자 연락처
블로그 http://joone.net/blog
이메일 joone@kldp.org


2007.8.18 마지막 변경
