# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
# Declare characters used by this game.
define f = Character(_("Fuyu"), color="#ae00ff")
define v = Character(_("Vieux"), color="#785212")
define q = Character(_("Queerel"), color="#dc07a6")
define m = Character(_("Moi"), color="#80b9fe")

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.
default book = False
default rizz = False
default tomber = False
default k_pop = False

# The game starts here.
label start:

    # Start by playing some music.
    play music "popo3.mp3"

    scene moone
    with fade

    "Vous vous réveillez dans un endroit sombre qui sent fort le salpètre et la mousse."

    m "Qu'est ce que je fous ici ?? Cet endroit me rappelle quelque chose, mais je ne saurais dire quoi exactement."

    m "Je ne me souviens de rien, du flou, un flash, je tombe, mais... "

    m "Je ne me souviens pas d'avoir touché le sol."

    m "... Bon.. Ignorons ça, je dois sortir d'ici au plus vite, ça pue et ça manque d'oxygène."

    scene allemagne
    with fade

    m "Ah, enfin de l'air ! "

    m "Mais qu'est ce que ?! On est en Allemagne ??"

    show fuyu_salut
    with dissolve

    f "Hallo ! Was machst du hier ? Du siehst verloren.."

    m "oh, un oiseau violet qui parle allemand. Quelle surprise."
    
    hide fuyu_salut

    show fuyu_normal

    f "Je peux parler français aussi ! T'as de la chance d'être tombé.e sur moi !"

    m "Sa voix est grave, languoureuse, même mystérieuse quand il parle allemand, mais en français, sa voix devient plus suave, toujours aussi gracieuse."

    menu:

        f "Donc je peux t'aider ?"

        "Lui demander son numéro":

            jump numéro

        "Lui demander où on est":

            jump position
        
        "Lui dire oui.":

            jump oui


label numéro:

    show fuyu_enerve

    f "Pour quoi faire ?"
 
    "Vous tentez de garder la tête froide, mais devant son regard appuyé sur vous, vous sentez la chaleur monter à vos joues, vous croisez vos bras sans même le vouloir."

    m "Pour qu'on puisse s'appeller.. "
    
    "Vous regardez ailleurs, il y a un blanc."

    show fuyu_ferme

    f "Je penses que tu te fais une fausse impression, on s'est rencontré.es il y a à peine une minute."

    menu:

        "Comment relancez vous la conversation ?"

        "Lui déclamer un poème improvisé pour lui expliquer vos sentiments":
            jump poème
        "Trébucher (tu as un plan secret)":
            jump tombé

    

label poème:

    $ poème = True

    m "Je ne connais même pas, ni ton nom ni quoi qu'ce soit,"

    show fuyu_normal

    m "Pourtant, mes sombres pensées s'envolent quand tu te tournes vers moi."

    m "Il n'a fallu qu'une minute, qu'un souffle, qu'une seconde même,"

    m "Tant de temps pour savoir, qu'impunément, je t'aime."

    
    f "..."


    f "Quand étais-ce maintenant ? Tout me semble éloigné"

    f "Tu me demandes mon nom, jeune étranger,"

    f "Tu me demandes mon coeur, jeune dérangé"

    f "Mais si tu le souhaitais, je te le donnerais."

    m "Je le souhaite, par pitié, donne-les moi sur le champ !"

    show fuyu_regardeailleurs

    f "C'est accordé mein Schatz, mon coeur je te le rends."

    jump marry

label marry:

    scene black
    with dissolve

    "Après ça, combien d'années se sont écoulées ? Des mois, des semaines, des décénies, nous ne saurons jamais."

    "Tout ce que l'on sait c'est que vous vous êtes marié.es"

    scene schloss
    with dissolve

    "Après des années de passion mélée à la création, vous avez réalisé vos rêves, et vivez, épanoui.es dans un château immense."

    if poème:

        "Vous avez publié des dizaines de receuils de poèmes, écrits par vous deux au coin du feu."

    "Vous vivez ensemble et êtes heureux."

    "{b}Fin Château{/b}."
    
    return

label tombé:

    $ tomber = True

    "Vous tombez à ses pieds."

    hide fuyu_regardeailleurs
    hide fuyu_normal
    hide fuyu_content
    hide fuyu_enerve
    hide fuyu_main
    hide fuyu_salut
    hide fuyu_ferme
    show fuyu_tombe

    f "Rien de cassé ??"

    m "Tout va bien !"

    show fuyu_main

    f ".."

    "Vous saisissez sa main, chaude et douce au toucher. Ce contact physique vous surprend, et vous retombez."

    hide fuyu_tombe
    hide fuyu_main
    show fuyu_ferme
    
    f "Mais, comment tu fais pour tomber comme ça, deux fois d'affliée ?? "

    f "Tiens, relève toi mieux cette fois ci."

    show fuyu_main
    hide fuyu_ferme

    "Cette fois, vous vous relevez, laissant votre dignité au sol."

    hide fuyu_main
    hide fuyu_ferme
    show fuyu_normal

    m "Mer-Merci."

    f "Ce n'est rien ! Comment puis-je t'aider ?"

    m "Tu m'as déjà aidé, je ne peux pas tout te demander .."

    f "Mais ce n'est rien ! "

    m "Tu pourrais m'aider à rentrer chez moi ?"

    jump position

label position:

    show fuyu_normal

    f "On est à côté de Francfort."
    
    f "Je peux te raccompagner si tu veux."

    m "Merci beaucoup !"

    scene rue
    
    "Vous marchez côte à côte, déambulez dans des petites rue pavées bordées de maisons à colombages, vous tournez après ce drôle d'oiseau, le suivez, imitez ses pas."

    scene campagne

    "Depuis combien de temps marchez vous ? Vous n'en savez rien. Vous êtes à présent en rase campagne allemande, suivant un oiseau violet dont vous ne connaissez rien et pourtant tout à la fois, puisque vous l'avez observé durant tout votre voyage. "

    m "Comment tu t'appelles ?"

    show fuyu_content

    f "Fuyu."

    f "Et toi ?"

    m "Je.. Je ne sais plus."

    show fuyu_normal

    f "Comment ça se fait ?"

    m "Je me suis réveillé.e là, je ne me souviens plus de rien.."

    show fuyu_ferme

    f "Ah.."

    show fuyu_regardeailleurs

    f "Mais.. Si tu ne sais plus rien, on va où ?"

    m "Je ne sais pas, on peut aller chez toi ?"  

    hide fuyu_regardeailleurs
    hide fuyu_normal
    hide fuyu_content
    hide fuyu_enerve
    hide fuyu_main
    hide fuyu_salut
    hide fuyu_ferme
    show fuyu_tombe

    f "!!..."

    show fuyu_ferme
    hide fuyu_tombe
    m "Ah pardon.. Je ne voulais pas-"

    show fuyu_content

    f "Pourquoi pas !! Suis-moi."

    m "Avec plaisir !"

    "Vous marchez envore longtemps dans ces paysages sublimes, sans pouvoir détacher vos regards."

    jump chez_lui

label oui :

    "Après cette réponse, trop courte vous laissez un malaise s'installer."

    m "Tu.. Tu vas bien ? Tu me regardes bizarrement..."

    show fuyu_kittycutter
    with dissolve

    show fuyu_kittycutteropen
    with dissolve

    show fuyu_kittycutteropensharp
    with dissolve

    "Tout comme Lantier, Fuyu a eu une petite, disons, absence.. "


    "{b}Fin Lantier{/b}."

    return


label chez_lui :

    "Vous arrivez dans la ville de Fuyu."

    scene eschwege1

    show fuyu_content

    f "On est arrivés dans ma ville !"

    m "C'est magnifique.."

    menu :
        f "Tu trouves ?"

        "Pas autant que toi." :

            jump rizz
        
        "C'est la plus belle ville je trouve.":

            jump eschwege_lover

    return

label rizz :

    show fuyu_regardeailleurs

    f "Ah~"

    f "Merci .."

    show fuyu_content

    m "T'aurais pas à boire ?"

    f "Si, j'ai du redbull tiens !"

    m "Ah elle est fraîche !"

    f "Pas autant que toi.."

    show fuyu_regardeailleurs

    m "..."

    "Vous sirotez lentement votre canette, ne sachant que dire."

    "Vous avez une idée de génie, vous commencez votre phrase avec assurance, mais oubliez la fin."

    menu:
        m "Ton père est un ..."

        "voleur":
            m "Ton père est un voleur, il a volé toutes les étoiles du ciel pour les mettre dans tes yeux."
        "boucher":
            m "Ton père est pas boucher ?"
            m "Parce que quand je te vois, je pleure sur le poulet."
        "développeur chez nintendo":
            m "Parce que t'as un corps de DS."
        "dresseur canin":
            m "Ton daron serait pas dresseur canin ?"
            m "Parce que t'es une chienne."
            show fuyu_enerve
            f "... "
            show fuyu_kittycutter
            with dissolve

            show fuyu_kittycutteropen
            with dissolve

            show fuyu_kittycutteropensharp
            with dissolve

            "{b}Fin Gros misogyne{/b}."
            return
        "arabe":
            m "Ton père il serait pas arabe ?" #crédits à Sarah pour la blague que je ne cautionne pas
            m "Parce que t'es une bombe."
            f "C'est bien gentil mais ta blague est.. Comment dire.."
            show fuyu_kittycutter
            with dissolve

            show fuyu_kittycutteropen
            with dissolve

            show fuyu_kittycutteropensharp
            with dissolve
            
            "{b}Fin Dérapage{/b}."
            return

    
    f "haha ! "

    show fuyu_normal

    f "Raté, son métier c'est livreur."

    m "Livreur de quoi ?"

    show fuyu_ferme

    f "De lait. Il n'a fait qu'une commande."

    m "Ah désolé.e.."

    hide fuyu_ferme
    show fuyu_content

    f "C'est rien t'excuse pas !"

    show fuyu_normal

    if tomber:
        "Vous vous regardez, géné.e.s, pendant un court moment qui vous semble une éternité, ne sachant comment enchaîner."

        "Vous vous préparez à dire quelque chose, mais iel vous devance."

        f "Tu es tombé.e tout à l'heure, tu te souviens ?"

        m "ou-oui ?"

        "Revenir sur ce sujet vous met un peu mal à l'aise."

        f "On peut dire que .."

        hide fuyu_normal
        show fuyu_regardeailleurs

        f "Tu es tombé.e sous mon charme. ?"

        m "!!..."

        m "*murmure* On peut dire ça..."

        hide fuyu_regardeailleurs
        show fuyu_content

        f "Tu as dit quelque chose ?"

        m "No-on ! non non rien du tout.."

        "{b}Fin Rizz{/b}."

        return

    else:
        menu:
            f "Et sinon, t'écoute comme genre de musique ?"

            "Rock":
                f "LOUISE M'A MIS UN GUN SUR LA TEMPE J'ADORE LE ROCK"
            "Electro":
                jump electro
            "Pop" :
                jump pop
            "Rap" :
                jump rap



label eschwege_lover :
    show fuyu_content

    f "Viens, on est pas loin de chez moi !"

    scene Chambre_de_fuyu
    show fuyu_normal

    f "Bienvenue !!"

    m "Merci !!"

    "J'ai plus d'idées là aidez moi (oups vous pouvez revenir en arrière pour l'autre choix 10x mieux)"

    "{b}Fin pas finie{/b}."

label pop :
    f "Alors c'est très bien, mais c'est pas précis.."
    menu :
        "Quelle pop ?"
        "K pop":
            f "Je vois je vois, et t'écoutes quoi comme chanson ? Je m'y connais un peu.."
            python :
                k_pop = renpy.input("Quel.le artiste de k pop ?")


            if k_pop == "Jimin":

                f "Mais oui, je connais Jimin, c'est celui qui a une voix bizarre là... Sans jugement bien sûr ^^"
                
            elif k_pop == "Jungkook" or k_pop == "JK" or k_pop == "jungkook" :
                f "Bien sûûr lui là.. Tu connais Seven Days a week donc ?"
                m "Bien sûr !!"
                f "Tu hum.. LES PAROLES MERDE !! C'est un harceleur et personne ne remarque j'ai l'impression.."
                m "Ah boon ??"
                f "Tu écouteras les paroles tu verras, c'est horrible."
            
            elif k_pop == "BTS" or k_pop == "Brevet de technicien supérieur" :

                f "Ah d'accord.. C'est pas mal, mais ça reste très basique. Je t'avoue que c'est pas mon groupe préféré."
                m "Ouais je comprends. Mais j'écoute pas que ça bien sûr !"
                f "J'espère bien !"
            
            elif k_pop == "BP" or k_pop == "blackpink" k_pop == "Blackpink" or k_pop == "BlackPink" :

                f "J'aime bien, c'est pas mal du tout ça !! Bombaya c'est ma pref je pense."

            elif k_pop == "Jisoo" or k_pop == "jisoo" :
                f "Ah mais oui, j'aime bien flower !"
            elif k_pop == "Jennie" or k_pop == "jennie" :

                f "C'est elle qui a fait solo non ? J'ai entendu du bien de la version jazz, mais j'aime pas le clip."

            else :
                f  "[k_pop]? Connais pas.. Bon mes connaissances sont peut-être un peu limitées.."
        "Pop américaine" :
            f "Taylor Swift tout ça ?"
            m "Oui en gros.."
        "Pop rock" :
            f "Je suis sans doute inculte, mais quelle différence avec le rock ?"
            m "Je chipote."

label electro :

    show fuyu_content
    f "J'AIME BIEEENG !!!!" #rajouter un skin pour ça, style fuyu beauf jsp
    f "Nan pardon je m'emporte .."

label rap :
    f "... Quel rap ? "
        
 







