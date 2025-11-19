import random

d = {'Nanny':'유모', 'Offend':'기분을 상하게 하다', 'Offended':'기분이 상하다', 'Arrogant':'오만한', 'Distracted':'산만해진', 
     'Narrow':'좁은', 'anxious':'불안해하는', 'Fear':'두려움', 'to sleep through':'안깨고 자다', 'Nervous flier':'비행 공포증'
     , 'To stumble':'넘어지다, 넘어질뻔하다', 'Lavatory':'화장실', 'Eastbound':'동쪽으로 향하는', 'headed to':'향했다'}

d1 = {v:k for k,v in d.items()} # 한국어를 영어로



def test_de_mots(d):
    n = 0
    #m = len(d)/2
    l = []
    keys = list(d.keys())
    random.shuffle(keys)
    #k = keys[:int(m)]
    for mot in keys:
        mots = d[mot]
        guess = input('{} 단어를 번역하세요: '.format(mot))
        if guess == mots:
            n+=1
            print('단어의 번역이 맞습니다.') 
        else: 
            l.append(mot)
            print('단어의 번역이 틀립니다, 정답은 {} 입니다.'.format(mots))
    print('점수는 총 {}점중 {}점입니다.'.format(len(d), n))
    if len(l) != 0:
        str = '/'.join(l)
        print('틀린단어(들)은 {}입니다.'.format(str))
    elif len(l) == 0:
        print('축하합니다.')

# print(test_de_mots(d2))

def test_final(d, d1):
    n = 0
    l = []
    for k in d1:
        if k not in d:
            d[k] = d1[k]
    keys = list(d.keys())
    random.shuffle(keys)
    k = keys[:50] # 50 mots
    for mot in k:
        mots = d[mot]
        guess = input('{} 단어를 번역하세요: '.format(mot))
        if guess == mots:
            n+=1
            print('단어의 번역이 맞습니다.') 
        else: 
            l.append(mot)
            print('단어의 번역이 틀립니다, 정답은 {} 입니다.'.format(mots))
    print('점수는 총 {}점중 {}점입니다.'.format(len(d), n))
    if len(l) != 0:
        str = '/'.join(l)
        print('틀린단어(들)은 {}입니다.'.format(str))
    elif len(l) == 0:
        print('축하합니다.')

print(test_final(d, d1))

def cherche_mots(d, mot):
    return d[mot]

# print(cherche_mots(d2, 'la campagne'))

# print(len(d)

# é ê è