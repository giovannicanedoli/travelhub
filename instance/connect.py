import sqlite3

conn = sqlite3.connect("db.sqlite")
c = conn.cursor()

#per eseguire comandi sql
#c.execute("SELECT * FROM STOCAZZO")

#c.execute("SELECT * FROM cities")
'''
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Roma', 'Italia', 'https://images.pexels.com/photos/19132522/pexels-photo-19132522/free-photo-of-italia-edifici-arquitectura-viatjar.jpeg?auto=compress&cs=tinysrgb&w=600', 'Roma, la città eterna, è famosa per la sua ricca storia, i suoi monumenti antichi e la sua vivace atmosfera.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Venezia', 'Italia', 'https://images.pexels.com/photos/2748019/pexels-photo-2748019.jpeg?auto=compress&cs=tinysrgb&w=600', 'Venezia, la città dei canali, incanta i visitatori con i suoi romantici ponti, i palazzi storici e le gondole che navigano lungo i canali.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Firenze', 'Italia', 'https://images.pexels.com/photos/21279856/pexels-photo-21279856/free-photo-of-ciutat-fita-edificis-italia.jpeg?auto=compress&cs=tinysrgb&w=600', 'Firenze, culla del Rinascimento, vanta capolavori artistici, una magnifica architettura e una deliziosa cucina toscana.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcellona', 'Spagna', 'https://images.pexels.com/photos/819764/pexels-photo-819764.jpeg?auto=compress&cs=tinysrgb&w=600', 'Barcellona, una città cosmopolita e vibrante, affascina con le sue opere di Gaudí, le spiagge vivaci e la sua ricca cultura.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Madrid', 'Spagna', 'https://images.pexels.com/photos/3757144/pexels-photo-3757144.jpeg?auto=compress&cs=tinysrgb&w=600', 'Madrid, la capitale spagnola, è famosa per i suoi musei di fama mondiale, la sua movimentata vita notturna e le sue deliziose tapas.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Siviglia', 'Spagna', 'https://images.pexels.com/photos/16778460/pexels-photo-16778460/free-photo-of-fita-pont-riu-viatjar.jpeg?auto=compress&cs=tinysrgb&w=600', 'Siviglia, con la sua affascinante architettura moresca, il flamenco appassionato e il caldo sole andaluso, incanta i visitatori di tutto il mondo.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Parigi', 'Francia', 'https://images.pexels.com/photos/699466/pexels-photo-699466.jpeg?auto=compress&cs=tinysrgb&w=600', 'Parigi, la città dell''amore, è famosa per la sua eleganza, i suoi monumenti iconici e la sua rinomata cucina francese.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Nizza', 'Francia', 'https://th.bing.com/th/id/R.2abc086422f4cf184c9f8c3195b80e82?rik=bOBj4seixxpxNw&pid=ImgRaw&r=0', 'Nizza, situata sulla splendida Costa Azzurra, è conosciuta per le sue spiagge incantevoli, il suo clima mediterraneo e la sua eleganza raffinata.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Lione', 'Francia', 'https://images.pexels.com/photos/12204581/pexels-photo-12204581.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'Lione, con la sua ricca storia, la sua deliziosa gastronomia e la sua atmosfera vivace, è una delle città più affascinanti della Francia.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Londra', 'Regno Unito', 'https://th.bing.com/th/id/R.989003cdea6fb3dba534e689c9d35292?rik=2eELKBSQmDup4w&pid=ImgRaw&r=0', 'Londra, una metropoli cosmopolita, offre una miscela affascinante di storia antica, cultura contemporanea e vibrante vita urbana.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Manchester', 'Regno Unito', 'https://th.bing.com/th/id/R.6c9fcb614ed6ca19f4cd0881c47a67a2?rik=%2bg7e3yXt77aDTQ&pid=ImgRaw&r=0', 'Manchester, una città dinamica e creativa, è rinomata per la sua vivace scena musicale, i suoi club di calcio e la sua architettura industriale.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Liverpool', 'Regno Unito', 'https://wallpaperaccess.com/full/2047388.jpg', 'Liverpool, città natale dei Beatles, vanta una ricca storia musicale, un''iconica waterfront e una vivace cultura.' , 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Vienna', 'Austria', 'https://s29745.pcdn.co/wp-content/uploads/2019/08/2-Days-in-Vienna-Itinerary-1-1.jpeg', 'Vienna, la città della musica classica, è celebre per i suoi sontuosi palazzi imperiali, i suoi caffè storici e la sua scena culturale vibrante.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Salisburgo', 'Austria', 'https://th.bing.com/th/id/R.435a58beaf08556e930ee146ae5a13ff?rik=GTITcvTUZaEFxw&pid=ImgRaw&r=0', 'Salisburgo, città natale di Mozart, è rinomata per la sua architettura barocca, i suoi paesaggi alpini e il suo patrimonio musicale.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Lisbona', 'Portogallo', 'https://th.bing.com/th/id/R.398ec897817e8d6760fda64b186b060e?rik=DKblE%2fvtNcYW6g&pid=ImgRaw&r=0', 'Lisbona, la capitale portoghese, affascina con le sue strade tortuose, le sue affascinanti colline e il suo affascinante mix di antico e moderno.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Porto', 'Portogallo', 'https://th.bing.com/th/id/R.cf19928187bdeb9e1e2c8e35d7b19abe?rik=PKqqDJPzthYzUg&pid=ImgRaw&r=0', 'Porto, famosa per il suo vino porto, i suoi pittoreschi vicoli e i suoi imponenti ponti, è una delle città più affascinanti del Portogallo.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Amsterdam', 'Paesi Bassi', 'https://th.bing.com/th/id/R.93a410a3f0667172e3966681b86dce0f?rik=I97bC62dt6NBPg&pid=ImgRaw&r=0', 'Amsterdam, con i suoi pittoreschi canali, i suoi musei eclettici e la sua vivace vita notturna, è una delle città più affascinanti d''Europa.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rotterdam', 'Paesi Bassi', 'https://th.bing.com/th/id/R.8c0c6edd968b76637995d5d5c853bce8?rik=jEHC1Peod36fKw&pid=ImgRaw&r=0', 'Rotterdam, città portuale dinamica, è famosa per la sua architettura innovativa, i suoi vivaci mercati e la sua scena artistica.' , 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Atene', 'Grecia', 'https://images.pexels.com/photos/3224227/pexels-photo-3224227.jpeg', 'Atene, la culla della civiltà occidentale, vanta un ricco patrimonio archeologico, una vivace vita notturna e una deliziosa cucina mediterranea.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Santorini', 'Grecia', 'https://lp-cms-production.imgix.net/2021-05/shutterstockRF_1563449509.jpg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850&q=35&dpr=3', 'Santorini, con i suoi caratteristici edifici bianchi e blu, i tramonti mozzafiato e le spiagge di sabbia nera, è una delle isole più affascinanti della Grecia.', 'a');")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Mykonos', 'Grecia', 'https://lp-cms-production.imgix.net/2021-08/shutterstockRF_1541944991.jpg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850&q=20&dpr=5', 'Mykonos, con le sue spiagge di sabbia dorata, i suoi famosi mulini a vento e la sua vivace vita notturna, è una delle isole più glamour della Grecia.', 'a');")
'''

# Inserimento dei dati per Roma - Colosseo
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Roma', 'Italia', 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1996&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Il Colosseo è un''icona della Roma antica e una delle sette meraviglie del mondo.', 'FCO')")

# Inserimento dei dati per Roma - Fontana di Trevi
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rome', 'Italia', 'https://images.unsplash.com/photo-1525874684015-58379d421a52?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'La Fontana di Trevi è una delle fontane più famose del mondo, nota per la sua bellezza e la tradizione di lanciare una moneta per garantirsi il ritorno a Rome.', 'FCO')")

# Inserimento dei dati per Rome - Piazza San Pietro
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rome', 'Italia', 'https://images.unsplash.com/photo-1531572753322-ad063cecc140?q=80&w=2076&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Piazza San Pietro è il centro della Città del Vaticano e uno dei luoghi più importanti per i fedeli cattolici.', 'FCO')")

# Inserimento dei dati per Paris - Torre Eiffel
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Paris', 'Francia', 'https://images.unsplash.com/photo-1439393161192-32360eb753f1?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'La Torre Eiffel è uno dei simboli più iconici al mondo e offre una vista spettacolare sulla città di Paris.', 'CDG')")

# Inserimento dei dati per Paris - Louvre
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Paris', 'Francia', 'https://images.unsplash.com/photo-1587648415693-4a5362b2ce41?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Il Louvre è il più grande museo d''arte e di storia del mondo, con opere famose come la Gioconda di Leonardo da Vinci.', 'CDG')")

# Inserimento dei dati per Madrid - Puerta del Sol
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Madrid', 'Spagna', 'https://images.unsplash.com/photo-1570698473651-b2de99bae12f?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Puerta del Sol è una delle piazze più vivaci di Madrid, circondata da negozi, ristoranti e monumenti.', 'MAD')")

# Inserimento dei dati per Madrid - Parco del Retiro
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Madrid', 'Spagna', 'https://images.unsplash.com/photo-1578305698944-874fa44d04c9?q=80&w=1976&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Il Parco del Retiro è un''oasi verde nel cuore di Madrid, perfetta per una passeggiata o una pausa rilassante.', 'MAD')")

# Inserimento dei dati per Barcelona - Parco Güell
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcelona', 'Spagna', 'https://images.unsplash.com/photo-1593368858664-a7fe556ab936?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Il Parco Güell è un capolavoro di Gaudí e offre una vista spettacolare sulla città di Barcelona.', 'BCN')")

# Inserimento dei dati per Barcelona - Sagrada Familia
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcelona', 'Spagna', 'https://hips.hearstapps.com/gioit.h-cdn.co/assets/17/41/980x980/square-1507700367-sagradafamilia.jpg?resize=1200:*', 'La Sagrada Familia è una delle opere più famose e iconiche di Gaudí, ancora in fase di costruzione.', 'BCN')")

# Inserimento dei dati per Barcelona - La Pedrera
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcelona', 'Spagna', 'https://images.unsplash.com/photo-1568232094870-03e2b312ae4b?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'La Pedrera è un altro capolavoro architettonico di Gaudí, con un design unico e innovativo.', 'BCN')")

# Inserimento dei dati per Bangkok
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Bangkok', 'Thailand', 'https://www.happyviaggithailandia.com/app/public/upload/THAILANDIA/bangkok/033.jpg', 'Bangkok is the capital and most populous city of Thailand. It is known for its vibrant street life and cultural landmarks.', 'BKK')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Bangkok', 'Thailand', 'https://images.placesonline.com/photos/424011407170352_Bangkok_531675985.jpg', 'Bangkok is the capital and most populous city of Thailand. It is known for its vibrant street life and cultural landmarks.', 'BKK')")

# Inserimento dei dati per Terni - Cascate delle Marmore
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Terni', 'Italy', 'https://st3.idealista.it/news/archivie/styles/fullwidth_xl/public/2023-08/images/1280px-terni_cascate_delle_marmore_02_-_copia.jpg?VersionId=IWU5LV0ifRnGApBTr9klRzsZOFj6ZZbc&itok=A0554KAu', 'Terni is a city in the southern portion of the region of Umbria in central Italy.', 'QSR')")

# Inserimento dei dati per Terni - Piediluco e Rocca
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Terni', 'Italy', 'https://www.laportadellavalnerina.com/wp-content/uploads/2020/03/piediluco-e-rocca.jpg', 'Terni is also known for the picturesque Lake Piediluco and its historic Rocca Albornoziana.', 'QSR')")

# Inserimento dei dati per Terni - Altro esempio per Terni
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Terni', 'Italy', 'https://d5rzfs5ck83rq.cloudfront.net/_processed_/1/d/csm_foto_Terni_titolo_929bf688fb.jpg', 'Terni is a city with rich industrial history and beautiful natural surroundings.', 'QSR')")

# Inserimento dei dati per Santorini - Esempio 1
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Santorini', 'Greece', 'https://www.hachettebookgroup.com/wp-content/uploads/2020/03/Santorini.png?w=1024', 'Santorini is a volcanic island in the Cyclades group of the Greek islands.', 'JTR')")

# Inserimento dei dati per Santorini - Esempio 2
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Santorini', 'Greece', 'https://static2-viaggi.corriereobjects.it/wp-content/uploads/2022/08/iStock-166471469-1080x720.jpg?v=1659884245', 'Santorini is famous for its stunning sunsets and beautiful white-washed buildings overlooking the Aegean Sea.', 'JTR')")

# Inserimento dei dati per New York - Esempio 1
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'New York', 'United States', 'https://media.tacdn.com/media/attractions-splice-spp-674x446/07/bd/6f/17.jpg', 'New York City is known for its iconic skyline, Broadway shows, and diverse cultural attractions.', 'JFK')")

# Inserimento dei dati per New York - Esempio 2
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'New York', 'United States', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/1200px-New_york_times_square-terabass.jpg', 'Times Square is a major commercial and entertainment hub in New York City.', 'JFK')")

# Inserimento dei dati per New York - Esempio 3
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'New York', 'United States', 'https://mywowo.net/media/images/cache/new_york_central_park_02_parte_sett_centrale_jpg_1200_630_cover_85.jpg', 'Central Park is an urban park in New York City, offering a peaceful escape from the hustle and bustle of the city.', 'JFK')")

# Inserimento dei dati per Los Angeles - Esempio 1
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Los Angeles', 'United States', 'https://photos.zillowstatic.com/fp/84717aaf43b722f1e1e083c6b8e5f455-cc_ft_960.jpg', 'Los Angeles is known for its entertainment industry, beautiful beaches, and diverse neighborhoods.', 'LAX')")

# Inserimento dei dati per Los Angeles - Esempio 2
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Los Angeles', 'United States', 'https://www.multimediatravel.com/wp-content/uploads/sites/47/2021/12/tour-los-angeles-2022-dall-italia.jpg', 'Explore the famous Hollywood sign and Walk of Fame in Los Angeles.', 'LAX')")

# Inserimento dei dati per London - Esempio 1
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'London', 'United Kingdom', 'https://www.lastrolabio.it/wp-content/uploads/2021/09/visitare-londra.jpg', 'London is the capital city of England, known for its rich history, iconic landmarks, and vibrant cultural scene.', 'LHR')")

# Inserimento dei dati per London - Esempio 2
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'London', 'United Kingdom', 'https://mediaim.expedia.com/destination/1/9c375cff1e843ffe6c8b0f3c1d00a65e.jpg', 'Visit the Tower of London and Buckingham Palace in London.', 'LHR')")

# Inserimento dei dati per London - Esempio 3
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'London', 'United Kingdom', 'https://londonita.com/wp-content/uploads/2020/02/itineraio-city-di-Londra-min.jpg', 'Explore the vibrant markets and historic landmarks of London.', 'LHR')")

# Inserimento dei dati per Copenhagen - Esempio 1
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Copenhagen', 'Denmark', 'https://scontent.ccdn.cloud/image/vivitravels-it/b9e4a4e0-c183-42df-a42a-72be17c20735/maxw-960.jpg', 'Copenhagen is the capital city of Denmark, known for its picturesque canals and colorful buildings.', 'CPH')")

# Inserimento dei dati per Copenhagen - Esempio 2
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Copenhagen', 'Denmark', 'https://www.helpviaggi.com/wp-content/uploads/2017/08/copenaghen-1.jpg', 'Visit the iconic Little Mermaid statue and Nyhavn waterfront in Copenhagen.', 'CPH')")



'''
COLOSSEO https://images.pexels.com/photos/19132522/pexels-photo-19132522/free-photo-of-italia-edifici-arquitectura-viatjar.jpeg?auto=compress&cs=tinysrgb&w=600
VENEZIA https://images.pexels.com/photos/2748019/pexels-photo-2748019.jpeg?auto=compress&cs=tinysrgb&w=600
FIRENZE https://images.pexels.com/photos/21279856/pexels-photo-21279856/free-photo-of-ciutat-fita-edificis-italia.jpeg?auto=compress&cs=tinysrgb&w=600

BARCELLONA https://images.pexels.com/photos/819764/pexels-photo-819764.jpeg?auto=compress&cs=tinysrgb&w=600
MADRID https://images.pexels.com/photos/3757144/pexels-photo-3757144.jpeg?auto=compress&cs=tinysrgb&w=600
SIVIGLIA https://images.pexels.com/photos/16778460/pexels-photo-16778460/free-photo-of-fita-pont-riu-viatjar.jpeg?auto=compress&cs=tinysrgb&w=600

PARIGI https://images.pexels.com/photos/699466/pexels-photo-699466.jpeg?auto=compress&cs=tinysrgb&w=600
NIZZA https://th.bing.com/th/id/R.2abc086422f4cf184c9f8c3195b80e82?rik=bOBj4seixxpxNw&pid=ImgRaw&r=0
LIONE https://images.pexels.com/photos/12204581/pexels-photo-12204581.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1

LONDRA https://th.bing.com/th/id/R.989003cdea6fb3dba534e689c9d35292?rik=2eELKBSQmDup4w&pid=ImgRaw&r=0
MANCHESTER https://th.bing.com/th/id/R.6c9fcb614ed6ca19f4cd0881c47a67a2?rik=%2bg7e3yXt77aDTQ&pid=ImgRaw&r=0
LIVERPOOL https://wallpaperaccess.com/full/2047388.jpg

VIENNA https://s29745.pcdn.co/wp-content/uploads/2019/08/2-Days-in-Vienna-Itinerary-1-1.jpeg
SALISBURGO https://th.bing.com/th/id/R.435a58beaf08556e930ee146ae5a13ff?rik=GTITcvTUZaEFxw&pid=ImgRaw&r=0

LISBONA https://th.bing.com/th/id/R.398ec897817e8d6760fda64b186b060e?rik=DKblE%2fvtNcYW6g&pid=ImgRaw&r=0
PORTO https://th.bing.com/th/id/R.cf19928187bdeb9e1e2c8e35d7b19abe?rik=PKqqDJPzthYzUg&pid=ImgRaw&r=0

AMSTEEREDAM https://th.bing.com/th/id/R.93a410a3f0667172e3966681b86dce0f?rik=I97bC62dt6NBPg&pid=ImgRaw&r=0
ROTTERDAM https://th.bing.com/th/id/R.8c0c6edd968b76637995d5d5c853bce8?rik=jEHC1Peod36fKw&pid=ImgRaw&r=0


ATENE https://images.pexels.com/photos/3224227/pexels-photo-3224227.jpeg
SANTORINI https://lp-cms-production.imgix.net/2021-05/shutterstockRF_1563449509.jpg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850&q=35&dpr=3
MYKONOS https://lp-cms-production.imgix.net/2021-08/shutterstockRF_1541944991.jpg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850&q=20&dpr=5
'''



conn.commit()
