from datetime import datetime

comment1 = {
    "Text" : "Lovely scenery!",
    "Name": "Barbara Middleton",
    "Username" : "@b123",
}
comment2 = {
    "Text" : " Dobar trek. Put sa jasnim markacijama izuzev nakon cetinarske sume gde je staza zarasla podosta.",
    "Name": "Ana Ulemek",
    "Username" : "@ulemequeen",
}
comment3 = {
    "Text" : "Da li je staza jasno markirana?",
    "Name": "Vlada Panic",
    "Username" : "@westserbiatrails",
}
comment4 = {
    "Text" : "Korab is one of my favorite peaks in the area!",
    "Name": "Sean Brown",
    "Username" : "@sean",
}


post1 ={
        "PostID": 1,
        "RouteName": "Grbaja – Prevoj Gurit – Žuta prla – vrh Trojan",
        "Distance": 15,
        "Time": 4,
        "TechnicalD": 7,
        "ConditionD": 6,
        "GPX": "gurit_zutaprla_trojan.gpx",
        "Username": "nevenam",
        "Description": "Postoje tri polazne staze od doma kojima se može izvršiti uspon na vrh Trojan (2190 m.n.v.). Jedna je makadamskim putem koji obilazi vrh Karaula sa desne strane do katuna Popadija i dalje preko Šupljih (Trojanskih) vrata. ",
        "AdditionalText":"Staza skreće prema njemu i strmo se uzdiže pored jaruge. Sledi niz serpentina do višeg livadskog platoa, na čijem kraju se nalazi prevoj iza koga je izvorišni tok reke Bistrice. Od ovog prevoja biramo stazu koja odvaja polulevo i prateći izohipse ispod grebena, nastavljamo dalje paralelno  sa granicom Crne Gore i Albanije. Ovaj deo staze se brzo prelazi i završava se strmijim usponom na prevoj (ćafa) Gurit (Gurikul) pred, za oči atraktivnim liticama Velikog vrha.",
        "Name": "Nevena Markovic",
        "Likes": ["westserbiatrails","nevenam"],
        "Image": "r.JPG",
        "MapImage": "map1.jpg",
        "Date": datetime(2021, 6, 29, 9, 30, 0),
        "Comments":[comment1,comment2]
    }
post2 ={
        "PostID": 2,
        "RouteName": "Kamp „Razvršje“ – Tri jezera (Crno, Zminje, Jablan)",
        "Distance": 25,
        "Time": 5,
        "TechnicalD": 5,
        "ConditionD": 8,
        "GPX": "durmitor.gpx",
        "Username": "westserbiatrails",
        "Description": "Trek počinje iz kampa „Razvršje“, odakle se stazom kroz šumu da brzo spustiti do Crnog jezera (brzo, pod uslovom da ne berete divlje jagode i maline kojih krajem leta ima u izobilju ). Na Crnom jezeru ostaviti sitnu mladunčad i ostatak familije neraspoložen za pešačenje da uživa.",
        "AdditionalText":"Dalje staza nastavlja oko jezera i potom dobro markiranom stazom uz Mlinski potok do Zminjeg jezera. Nakon toga potrebno je malo vratiti se istom stazom i skrenuti na makadamski put ka selu Bosača (kasnije na kratko se ide i asfaltom).  U selu skrenuti levo na prvoj raskrsnici u dolini, ka šumi. Iza poslednjih kuća nalazi se izvor sa pijačom vodom. Dalje dosta strmom stazom kroz šumu koja je nekada bila markirana, ali je dosta markacija izbledelo a i nešto drveća na kojima su bile je posečeno (držati se treka, u šumi postoji još nekih staza koje su meštani probijali). Taj deo kroz šumu je fizički najzahtevniji deo a i najružniji (subjektivan utisak, naravno).",
        "Name": "Vlada Panic",
        "Likes": [],
        "Image": "d.jpg",
        "MapImage": "map2.jpg",
        "Date": datetime(2021, 5, 17, 10, 30, 0),
        "Comments":[comment3]
    }
post3 ={
        "PostID": 3,
        "RouteName": "Korab : Adzina Reka Trail",
        "Distance": 50,
        "Time": 7,
        "TechnicalD": 6,
        "ConditionD": 9,
        "GPX": "korab.gpx",
        "Username": "ulemequeen",
        "Description": "Start sa Torbeskog Mosta, mesto 2 km dalje od mesta gde pocinje tradicionalni uspon na vrh Korab. Onda smo otrcali do karaule Pobeda, pa smo pratili dolinu Stirovice. Presli smo ledenu reku bosi, pa smo se popeli i pratili greben Projzabe, u pravcu velikih Korabskih vrhova. ",
        "AdditionalText":"Reka Radika izvire u reonu gde se spajaju dva velika masiva : Korab i Sar Planina. U stvari tri manje reke se spajaju u reku Radiku : Adzina Reka, Crn Kamen i Stirovica. Nas trail (planinsko trcanje) je pratio ove tri reke. Start sa Torbeskog Mosta, mesto 2 km dalje od mesta gde pocinje tradicionalni uspon na vrh Korab. Onda smo otrcali do karaule Pobeda, pa smo pratili dolinu Stirovice. Presli smo ledenu reku bosi, pa smo se popeli i pratili greben Projzabe, u pravcu velikih Korabskih vrhova. Onda spust do granice – reka Crn kamen, pratimo tok uzvodno opet do Torbeskog mosta, pa onda ulazimo u prelepu klisuru Adzine Reke. Pratimo Adzinu Reku sve do izvorisnog dela, popnemo se na vrh Lera (2197m), pa onda polako se spustamo u pravcu Gostivara – do sela Gorno i Dolno Jelovce.",
        "Name": "Ana Ulemek",
        "Likes": ["westserbiatrails"],
        "Image": "k.jpg",
        "MapImage": "map3.png",
        "Date": datetime(2021, 4, 10, 15, 25, 0),
        "Comments":[comment4]
    }
test = {
    1 : post1,
    2 : post2,
    3 : post3
}


nevena_posts={
    1: post1
}
vlada_posts={
    2: post2
}
ana_posts={
    3: post3
}

nevena = {
    "Name": "Nevena Markovic",
    "Username": "nevenam",
    "Posts": nevena_posts,
    "Image": "r.JPG",
    "Map": "nmap.png",
    "Distance": 44,
    "Time": 5,
    "Elevation": 345
}
vlada = {
    "Name": "Vlada Panic",
    "Username": "westserbiatrails",
    "Posts": vlada_posts,
    "Image": "vlada.JPG",
    "Map": "vmap.png",
    "Distance": 64,
    "Time": 5,
    "Elevation": 876
}
ana = {
    "Name": "Ana Ulemek",
    "Username": "ulemequeen",
    "Posts": ana_posts,
    "Image": "k.JPG",
    "Map": "amap.png",
    "Distance": 33,
    "Time": 4,
    "Elevation": 234
}

users={
    "nevenam" : nevena,
    "westserbiatrails": vlada,
    "ulemequeen": ana
}
