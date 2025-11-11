import random

d = {'l\'affirmation(n.f.)':'주장', 'la conquête':'정복', 'l\'enquête(n.f.)':'조사', 'deviner':'추측하다', 'effectuer':'실행하다', 'saisir':'붙잡다', 'l\'infraction(n.f.)':'위법'
     , 'engager':'저당잡히다', 'le cursus':'학업과정', 'l\'indifférence(n.f.)':'무관심', 'affronter':'과감히맞서다', 'privilégier':'우선하다', 'le blouson':'잠바'
     , 'le recto verso':'양면', 'le recto':'앞면', 'le verso':'뒷면', 'pendre':'매달리다', 'l\'hirondelle(n.f.)':'제비', 'rabattre':'방향을바꾸다', 'anticiper':'예상하다'
     , 'immense':'거대한', 'la foule':'군중', 'la facture':'청구서', 'apporter':'가져오다', 'la cesse':'중지', 'le miellat':'단물', 'le nombre réel':'실수(수학)', 'entreprendre':'착수하다'
     , 'le conflit':'분쟁', 'la portée':'사거리', 'stimuler':'자극하다', 'l\'injonction(n.f.)':'명령', 'l\'exécutif(n.m.)':'행정부', 'la torpeur':'무기력함', 'désormais':'이제부터'
     , 'se mobiliser':'(군대가)총동원되다', 'sanctionner':'벌하다', 'le colon':'식민자', 'la violation des droits de l\'homme':'인권침해', 'imposé':'과세된, 의무적인', 'la sanction':'승인'
     , 'encontre':'~에 반대하여', 'l\'extrémiste':'극단주의자', 'opérant':'효과적인', 'le Conseil de l\'Union européenne':'유럽연합이사회', 'magistral(e)':'훌륭한', 'perturber':'혼란케하다'
     , 'explorer':'탐구하다', 'le brio':'탁월함', 'la nuance':'뉘앙스', 'le traumatisme':'트라우마', 'intime':'내면의', 'dont':'그중', 'troubler':'흐리게하다', 'tant':'그처럼', 'la complexité':'복잡성'
     , 'ce qui n\'est que':'이는 단지', 'la certitude':'확신', 'tricolore':'삼색의', 'porter':'들다, 입다', 'la tunique':'허리밑까지 내려오는 여성용 의복', 'la tunique merengue':'레알유니폼'
     , 'galactique':'은하의', 'l\'allure(n.f.)':'속력, 거동, 외모', 'véritable':'실제로, 진정한', 'le raz':'급류', 'la marée':'조류', 'le raz de marée':'해일', 'médiatique':'미디어의'
     , 'd\'un point de vue':'한 관점에서', 'juridique':'법적인', 'l\'accueil(n.m.)':'대접', 'le retrait':'철수', 'la retraite':'은퇴', 'le Premier ministre':'총리', 'le ministre':'장관'
     , 'socialiste':'사회주의(자)의', 'l\'époux(se)':'배우자(남편, 아내)', 'la visée':'겨냥, 목표', 'la corruption':'부패, 비리', 'l\'observateur(rice)':'관찰자, 참관인', 'méditer':'심사숙고하다'
     , 's\'interroger':'묻다, 의문을가지다', 'la démarche':'전개', 'sincère': '진실된, 솔직한', 'le discours':'연설', 'le catastrophisme':'극단적 비관론', 'le mendat':'임기, 위임', 'célèbre':'유명한'
     , 'trahir':'배신하다', 'l\'inquiétude(n.f.)':'우려', 'propre':'(명사앞에)자신의, (명사뒤에)고유한, 청결, 특성', 'la postérité':'후손', 'aggraver': '악화시키다, 악화되다', 'le clivage':'분열'
     , 'la mobilisation':'동원', 'le soutien':'지지자', 'soutenir':'지탱하다', 'poursuivre':'뒤쫓다, 계속되다', 'alors que':'~하는동안', 'contribuer':'~에 기여하다', 'attiser':'(화를)돋우다'
     , 'le blocage':'봉쇄', 'le conservateur':'보수주의자', 'le journal':'일기, 신문', 'le courrier':'우편'}

d1 = {v:k for k,v in d.items()} # 한국어를 불어로

d2 = {'irrépressible':'억제할수없는', 'se ruer':'(말따위가)뒷발질하다, 내던지다', 'soulever':'(문제따위를)제기하다','l\'interrogation(n.f.)':'질문, 의문문', 'la condition':'신분, 컨디션, 조건'
      , 's\'appuyer':'기대어놓다', 'le chef(fe)':'우두머리, 책임자', 'la rubrique':'(신문의)란, 항목', 'le média':'미디어', 'quotidien(ne)':'나날의, 일간신문', 'affirmer':'주장하다, 단언하다'
      , 'menacer':'위협하다', 'l\'organe(n.m.)':'기관, (기계의)장치', 'la propagande':'선전', 'le diffuseur':'배급원, 방송사', 'intervenir':'개입하다, 중재하다', 'tenir':'잡다, 고정시키다'
      , 'la trêve':'휴전', 'la négociation':'협상', 'l\'enjeu(n.m.)':'내기, 문제점', 'l\'hexagone(n.m.)':'육각형, 프랑스본토', 'presser':'압박하다', 'user':'사용하다, 행사하다'
      , 'basculer':'기울다, 위아래로움직이다, 동요하다', 'le levier':'레버', 'disposer':'배열하다, 마음대로하다', 'le passage':'통행, 통과', 'le point de passage':'교차점'
      , 'la bande':'밴드, 무리, (배의)경사', 'mise en place':'설정, 배치, 확립, 구성', 'l\'opération(n.f.)':'수술, 작업, 작용, 작전', 'le renseignement':'정보, 첩보', 'le terminal':'터미널', 'lequel':'어느'
      , 'terroriste':'테러리스트', 'humanitaire':'인도주의적인, 인도주의자', 'la centaine':'100개', 'le millier':'1000', 'la centaine des milliers':'수십만', 'la dizaine des milliers':'수만'
      , 'le million':'백만', 'le dix million':'천만', 'le cent million':'억', 'forcé':'강요된, 어쩔수없는', 'fuir':'도망치다, 회피하다', 'le refuge':'피난처', 'repris':'반복된'
      , 'reprendre':'다시시작하다, 회복하다', 'réellement':'실제로, 현실적으로', 'craindre':'두려워하다', 'l\'organisation(n.f.)':'조직, 단체', 'revendiquer':'(당연한권리로써)요구하다'
      , 'l\'évacué':'피난민', 'évacuer':'(생리현상)배출하다, 피난시키다', 'près':'근처', 'l\'offensif(ve)':'공격', 'percer':'구멍을뚫다, 돌파하다', 'la première information':'초기정보'
      , 'la prise':'잡기, 점령', 'russe':'러시아의, 러시아인', 'intensifier':'강화시키다, 강화되다', 'la presse':'보도, 언론', 'spécialiste':'전문가', 'l\'amateur(n.m.)':'수집가, 애호가, 아마추어의'
      , 'rassurer':'안심시키다, 안심하다', 'rassurant':'안심이되는', 'estimer':'평가하다, 추정하다', 'le moyen':'수단, 방법, 능력(복수), 재력(복수)', 's\'emparer':'점령하다'
      , 'le fiasco':'(남성의)성적불능, (계획따위의)완전한실패', 'envisager':'고찰하다, 고려하다', 'le camp':'진지, 수용소, 캠프장', 'le prélude':'전주곡, 서막', 'l\'assaut(n.m.)':'공격(1)'
      , 'l\'ampleur(n.f.)':'(규모,모양따위가)큼, 폭넓음', 'la diversion':'교란작전, 기분전환', 'rasé':'짧게깎은, 면도한', 'raser':'짧게깎다, 면도하다', 'des rues rasés':'파괴된거리', 'la troupe':'집단'
      , 'poursuivre':'계속하다, 뒤쫓다, 추구하다', 'le procès':'소송, 재판', 'incriminer':'비난하다, 책임을지우다', 'le courant':'흐름, 흐르는', 'étouffer':'질식시키다, 질식하다, 덮어씌우다'
      , 'le scandale':'스캔들, 파렴치한행위, 소동', 'accuser':'비난하다, 참회하다', 'la campagne':'농촌, 캠페인, 군사적인', 'le paiement':'지불, 보수', 'le frimeur(se)':'허풍쟁이'
      , 'acharné':'~에 열중한, ~에 대해 가차없는', 'acharner':'(사냥개무리를)부추기다, 열중하다', 'l\'hebdomadaire(n.m.)':'주간지, 주간의', 'terrestre':'지상의, 지구의', 'l\'intérêt(n.m.)':'이익, 이자, 수익'
      , 'raconter':'이야기하다' , 'la diplomatie':'외교', 'le grandiose':'웅장함, 웅장한', 'courtiser':'비위를맞추다, (여자의)마음에 들려 애쓰다', 'l\'investiture(n.f.)':'수여, 공천, 임명'
      , 'la délégation':'대표단', 'l\'homme d\'affaire':'사업가', 'l\'apothéose(n.f.)':'신격화', 'le partenariat':'제휴', 'conclure':'(계약,조약을)맺다, 종결하다'}

d3 = {v:k for k,v in d2.items()} # 한국어를 불어로

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
    print('점수는 총 50점중 {}점입니다.'.format(n))
    if len(l) != 0:
        str = '/'.join(l)
        print('틀린단어(들)은 {}입니다.'.format(str))
    elif len(l) == 0:
        print('축하합니다.')

print(test_final(d, d2))

def cherche_mots(d, mot):
    return d[mot]

# print(cherche_mots(d2, 'la campagne'))

# print(len(d)

# é ê è