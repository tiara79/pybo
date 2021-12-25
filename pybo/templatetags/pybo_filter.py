# [21-12-16] 마크다운 필터 등록하기
import markdown
from django.utils.safestring import mark_safe

# [21-12-13] 템플릿 필터함수 사용
from django import template
register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

# [21-12-16] 질문 상세 템플릿에 마크다운 적용해 보기
# markdown 모듈에 Hnl2br", "fenced_code" 확장 도구를 설정
# "nl2br"은 줄바꿈 문자를 <br> 태그로 바꿔 주므로 enter를 한 번만 눌러도
# 줄바꿈으로 인식한다. 만약 이 확장 도구를 사용하지 않으면 줄바꿈을 위해
# 줄 끝에 마크다운 문법인 스페이스를 2개를 연속으로 입력한다.
@register.filter()
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))

