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

    "Après ça, combien d'années se sont écoulées ? Des mois, des semaines, des décénies, nous ne sauront jamais."

    "Tout ce que l'on sait c'est que vous vous êtes marié.es"

    scene schloss
    with dissolve

    "Après des années de passion mélée à la création, vous avez réalisé vos rêves, et vivez, épanoui.es dans un château immense."

    if poème:

        "Vous avez publié des dizaines de receuils de poèmes, écris par vous deux au coin du feu."

    "Vous vivez ensemble et êtes heureux."

    "{b}Fin Heureuse château{/b}."
    
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

    "Depuis combien de temps marchez vous ? Vous n'en savez rien. Vous êtes à présent en rase campagne allemande, suivant un oiseau violet dont vous ne connessez rien et pourtant tout à la fois, puisque vous l'avez observé durant tout votre voyage. "

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

    "Tout comme Lantier, Fuyu a eu une petite absence.. "


    "{b}Mauvaise fin{/b}."

label chez_lui :

    "Vous arrivez chez Fuyu."
    
    "{b}Fin heureuse campagne{/b}."

    return


