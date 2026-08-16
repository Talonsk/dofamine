screen images: 
    $ open_images.append('images');

    imagebutton:
        idle "images"
        xpos 670
        ypos 275 
        sensitive not dialogue_active
        action Jump('images')

screen paper:
    $ open_images.append('paper');

    imagebutton:
        idle "paper"
        xpos 480
        ypos 670 
        sensitive not dialogue_active
        action [Show('painting'), Jump('painting')]

screen painting:    
    imagebutton:
        idle im.Scale("images/ui/painting.png", 850, 500)
        xalign 0.5
        yalign 0.5 

screen hole:
    $ open_images.append('hole');

    imagebutton:
        idle "hole"
        xpos 207
        ypos 453
        sensitive not dialogue_active
        action Jump('hole')

screen hole:
    $ open_images.append('hole');

    imagebutton:
        idle "hole"
        xpos 207
        ypos 453
        sensitive not dialogue_active
        action Jump('hole')

screen hole:
    $ open_images.append('hole');

    imagebutton:
        idle "hole"
        xpos 207
        ypos 453
        sensitive not dialogue_active
        action Jump('hole')


label act1:

    jump walk

    show bg room

    u 'Я проснулась.{w=1} Потолок пустой, но не как обычно.{w=1} Конечно! Сегодня день особенный ведь. Я иду в гости{w=1}  Наконец-то я получила от нее письмо.{w=1} Вчера.{w=1} Или позавчера.{w=1} А может неделю назад.{w=1} Или месяц'

    u 'Ой, а где бумажка?'

    u 'Шарю рукой под подушкой.{w=1} Нащупываю.'

    u 'Ее адрес. И эта комната ее.{w=1} Была.{w=1} Здесь обои с цветочками, а мне больше нравятся звездочки. Но она любила цветочки.{w=1} Я поэтому тоже теперь люблю цветочки.'

    u 'Я встаю. Пол холодный.{w=0.5} Надо было носки надеть, но я забыла.{w=1} Мы с сестрой всегда ходили босиком, и мама ругалась.{w=1} А сестра смеялась и говорила: «Пол холодный, потому что он самостоятельный».'
    
    u 'Я не поняла тогда.{w=1} И сейчас не очень. Но я верю.'
    
    u 'Ладно. Сначала — умыться.{w=1} Потом — позавтракать.{w=1} Потом - спросить у мамы.{w=1} И потом — идти'
    
    u 'Я так рада. Прям бегать хочется.'
    
    jump room

    return


label images:
    
    u 'Это мои рисунки, они больше всего нравились сестре!'

    jump room

    return

label room:
    show bg room    

    show screen paper()
    show screen images()
    call screen arrows('bathroom', 'Ванная комната', 'hallway', 'Коридор')

    return


label painting:

    if not is_say_painting:
        u 'Это наша семья. Почти. Я, мама, сестра и..папа, но его больше нет. Мама сказала что он погиб потому что пил гадости.'

        u 'Но я тоже иногда пью гадости. Например газировку. Неужели я тоже скоро умру.....'

        hide screen painting
        $ is_say_painting = True

    else:
        u '...'
        hide screen painting

    jump room

    return

label bathroom:
    show bg bathroom

    u 'Зеркало высоко.{w=1} Я встаю на носочки.{w=1} Вижу только лоб и глаза.{w=1} Глаза сонные. И волосы торчат.{w=1} Я похожа на ёжика.'
    
    u 'Я люблю разговаривать сама с собой.{w=1} Когда сестра жила с нами, мы разговаривали вместе.{w=1} А теперь я одна.{w=1} Но ничего, сейчас я к ней приду, и мы будем болтать, болтать, болтать.'
    
    u 'Я умылась.{w=1} Вода холоднючая. Хорошо.'

    u 'На полотенце пятно.{w=1} Кажется, ржавое. Или красное.{w=1} Наверное, краска.{w=1} Папа что-то красил когда-то.{w=1} Или нет. Не помню.'

    call screen arrows(right_bg='room',  right_ph='Комната')

    return

label hallway:
    show bg hallway

    show screen hole()
    call screen arrows('kitchen', 'Кухня', 'room', 'Комната')

    return

label hole:
    
    u 'Это папа сделал. Когда сестра его разозлила.{w=1} Он часто бил ее.{w=0.5} А еще он иногда закрывался с ней в комнате, а она кричала.{w=1} Но не так, как когда бьёт.{w=0.5} По-другому.{w} Мама сказала мне не подходить к комнате в такие моменты, громко включала радио и мы сидели на кухне...{w=1} Однажды я спросила сестру почему она после этого долго моется и закрывается в комнате.{w=1} Она сказала: "Отстань, это игра".{w=1} Но я же слышала, что она плачет. Разве так играют?'

    jump hallway

    return

label kitchen:
    show bg kitchen_mom

    u 'Мама стоит около стола.{w=1} Готовит.{w=1} Она часто готовит.'

    u '— Мам, можно я к сестре схожу?{w}'

    u 'Мама поднимает глаза.{w=1} У неё лицо усталое.{w=1} И немного испуганное, но она улыбается.{w=1.5} Мама часто боится. Я не понимаю чего.'

    show bg kitchen

    show mom normal

    m smiling '— К какой сестре? - спрашивает мама.'

    u '— Ну, к старшей! Она же прислала адрес. Вот, смотри.'

    u 'Я показываю бумажку.{w=0.5} Мама смотрит, но не берёт.{w=0.5} Рукой не трогает. Будто боится обжечься.'

    m '— Ты уверена? - спрашивает мама.'

    u '— Конечно! Она меня ждёт! Она написала!'

    u 'Мама молчит долго-долго. Я уже начинаю бояться, что она скажет «нет».'

    m '— Будь осторожна, - говорит мама наконец. — И не гуляй долго. Вернись до темноты.'

    u '— Вернусь-вернусь! Спасибо, мамочка!'

    u 'Я чмокаю её в щёку и бегу к двери.{w=0.8} Мама холодная.{w=0.8} Странно.{w=0.8} Может, она простудилась?'

    u 'Но я уже думаю про сестру.'

    hide mom

    jump park

    return

label park:
    show bg park

    pause

    return