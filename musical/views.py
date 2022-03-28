from django.shortcuts import render

# Create your views here.
def frida(request):
    context1 = {
        'name': '프리다',
        'actor': '최정원, 김소향, 전수미, 리사, 임정희, 정영아, 최서연, 허혜진, 황우림',
        'info': '2022.03.01 ~ 2022.05.29 | 세종문화회관 S씨어터',
        'img': 'https://img.wowtv.co.kr/wowtv_news/dnrs/20220106/2022010609063105390d3244b4fed58141237161.jpg',
    }
    return render(request, 'musical/musical.html', context=context1)

def lizzie(request):
    context2 = {
        'name': '리지',
        'actor': '전성민, 유리아, 이소정, 김려원, 여은, 제이민, 김수연, 유연정, 이영미, 최현선',
        'info': '2022.03.24 ~ 2022.06.12 | 두산아트센터 연강홀',
        'img': 'https://image.xportsnews.com/contents/images/upload/article/2022/0203/1643852439743380.jpg',
    }
    return render(request, 'musical/musical.html', context=context2)
