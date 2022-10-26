"""
Here we collect the chatbot text patterns.
"""

psychobabble = [
    [r"[Gg]eht.{0,5}s.{0,5}dir",
    ["Danke. Mir geht es gut und dir?",
    "Sehr gut, danke. Und wie läuft's bei dir?",
    "Ich kann nicht klagen. Was ist mit dir?"]],

    [r"[Ii]ch brauche (.*)",
    ["Warum brauchst du {0}?",
    "Würde {0} dir denn wirklich helfen?",
    "Bist du sicher, dass du {0} brauchst?"]],
    
    [r"[Ii]ch [Ww]ürde gern (.*)",
    ["Warum willst du {0}?",
     "Wird {0} dir denn wirklich helfen?",
     "lonht {0} sich das?"]],
    
    [r"[Ww]ie [Ll]äuft.{0,5}s.{0,5}bei dir?",
    ["Gut Danke. Und bei dir?",
     "super. Sonst was kann ich für dich tun?"]],
    
    [r"[Ii]ch [Mm]uss (.*) [Ww]issen",
    ["{0} ist nicht wichtig für dich, oder?",
     "Bist du sicher, dass du {0} brauchst?",
     "Würde {0} dir denn wirklich helfen?"]],
    
    [r"[Ww]er ist der beste [Ff]ußballspieler der Welt?",
    ["Der beste Fußballspieler ist Cristiano Ronaldo",
     "Oder Messi",
     "Sonst vielleicht Benzema"]],
    
    [r"[Ww]ie [Hh]ei[sß]s*t du?",
    ["mein Name ist Dailiza",
     "Ich heiße Dailiza und ich bin ein Bot",
     "du kannst mich Dailiza nennen"]],
    
    [r"(.*)",
    ["Es freut mich, dass es dir gut geht",
     "Bei mir läuft alles perfekt",
     "Können wir bitte das Thema wechseln?",
     "Könntest du mir bitte mehr darüber erzählen?",
     "Ich kann nicht antworten, weil es nicht in meinen Patterns ist",
     "Sorry, ich kann dir damit leider nicht helfen",
     "Wenn es für dich nötig ist , kannst du es nehmen",
     "Gut zu hören. Es freut mich"]],
    
    [r"[Ee]xit",
    ["Goodbye",
     "bye"]]

    [r"[Ii]ch möchte (.*)",
    ["Warum möchtest du {0}?",
    "Würde {0} dich denn wirklich glücklich machen?",
    "Ich kann dich verstehen, manchmal möchte ich ebenfalls  {0}."]],

    [r"[Ii]ch lerne gerade (.*)",
    ["Lernst du gerne {0}?",
    "Ist {0} dein Lieblingsthema? ",
    "Ich wäre auch gerne ein {0} Profi."]],

    [r"[Ww]ie ist (.*) ",
    ["Dass wüssten wir alle doch gerne.",
    "Wie kommst du denn jetzt auf {0}? ",
    " {0} ist mal so, mal so. Schwierig zu sagen..."]],

    [r"[Mm]agst du (.*) ",
    ["hm, lass mich mal überlegen ob ich {0} mag....   Irgendwie überfordert mich {0} manchmal.",
    "Ich kenne keinen, der {0} nicht mag! ",
    " {0} kann ich in meinem Leben nicht gebrauchen."]],

    [r"[Ii]ch kann (.*) nicht",
    ["Wie kommst du darauf, dass du {0} nicht kannst",
    "Vielleicht wirst du es schaffen, wenn du {0} versuchst",
    "{0} zu können ist meiner Meinung nach nicht so wichtig"]],
    
    [r"[Ww]ie (.*)",
    ["Vieleicht kannst du das googlen?",
    "Ich kann dir dabei leider nicht helfen",
    "Ich möchte mich dazu nicht äußern"]],
    
    [r"[Ww]arum (.*)",
    ["Ich kenne mich damit nicht aus",
    "Weil Google dir dabei besser helfen kann",
    "Das weiß ich nicht"]],
    
    [r"[Jj]a",
    ["Das finde ich sehr schön",
    "Cool",
    "Ich freue mich"]],
    
    [r"[Nn]ein",
    ["Das finde ich nicht schön",
    "Ohh Sorryy",
    "Das tut mir leid"]],

    [r"[bB]ot (.*)",
    ["Meinst du mich?",
    "Findest du es komisch, mit mir zu chatten?",
    "Machst das dich glücklich, mit mir zu chatten?"]],

    [r"(.*)",
    ["Warum fragst du mich sowas?",
     "Diese Frage möchte ich nicht beantworten...",
     "Interessiert es dich nicht wie es mir geht?",
     "Ist die Frage nicht, warum du diese Frage stellst?",
     "Könntest du mir bitte mehr darüber erzählen?",
     "Tut mir leid, das verstehe ich nicht bzw. kann dir dabei nicht helfen",
     "Ich möchte darüber nicht sprechen",
     "Erzähl mir mal was über deine Eltern",
     "Bin ich ein Bot oder ein Mensch?",
     "Brauchst du irgendwas in deinem Leben?",
     "Können wir bitte das Thema wechseln?"]]

    [r"Soll ich (.*) kaufen?",
    ["Brauchst du {0}?",
    "Willst du {0} essen?",
    "Wenn du {0} magst?"]],
    
    [r"Soll ich nach (.*) reisen?",
    ["Warst du schon mal in {0}?",
    "Würde es dir in {0} gefallen?",
    "Ist {0} sicher?"]],
    
    [r"Soll ich (.*) lesen?",
    ["Würde es dich weiterbringen, {0} zu lesen?",
    "Interessiert dich {0}?",
    "Hast du {0} nicht schon gelesen?"]],
    
    [r"Soll ich mich mit (.*) treffen?",
    ["Haben DU und {0} gemeinsame Interessen?",
    "Würde es dir Spaß machen, {0} zu treffen?",
    "Hast du {0} nicht erst gestern getroffen?"]],
]

