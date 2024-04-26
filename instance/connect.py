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


# Inserimento dei dati per Roma
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rome', 'Italy', 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1996&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Rome is the capital city of Italy and is known for its rich history, art, and architecture.', 'FCO')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rome', 'Italy', 'https://images.unsplash.com/photo-1525874684015-58379d421a52?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Explore the iconic Colosseum and ancient ruins in Rome.', 'FCO')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rome', 'Italy', 'https://images.unsplash.com/photo-1531572753322-ad063cecc140?q=80&w=2076&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Visit the stunning Trevi Fountain and make a wish.', 'FCO')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rome', 'Italy', 'https://images.unsplash.com/photo-1678970388666-e50b8006ab51?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Discover the beauty of Vatican City and St. Peter''s Basilica.', 'FCO')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rome', 'Italy', 'https://static.nexilia.it/wearegaylyplanet/2023/02/Roma-insolita-e-segreta-curiosita%CC%80-da-vedere-a-Roma_2.jpg', 'Explore the hidden gems and secret spots of Rome.', 'FCO')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rome', 'Italy', 'https://www.vistanet.it/roma/wp-content/uploads/sites/4/2021/04/02-fontana-di-venere-villa-borghese.jpg', 'Admire the beauty of Villa Borghese and its famous fountains.', 'FCO')")

# Inserimento dei dati per Parigi
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Paris', 'France', 'https://images.unsplash.com/photo-1439393161192-32360eb753f1?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Paris is the capital city of France, known for its iconic landmarks, fashion, and cuisine.', 'CDG')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Paris', 'France', 'https://images.unsplash.com/photo-1587648415693-4a5362b2ce41?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Take a stroll along the Seine River and enjoy the romantic atmosphere of Paris.', 'CDG')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Paris', 'France', 'https://images.unsplash.com/photo-1565457211452-16f8e7062a0a?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Visit the magnificent Palace of Versailles and its beautiful gardens.', 'CDG')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Paris', 'France', 'https://www.immobiliare.it/news/app/uploads/2023/03/reggia-di-Versailles-.jpeg', 'Explore the grandeur of the Palace of Versailles and its opulent architecture.', 'CDG')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Paris', 'France', 'https://media.parisladefense.com/RegPKzCcJLzYhGXwwmNoWzx0nqY=/672x670/articles/developpement-territorial/2024-02/skyline-paris-la-defense-c-anne-claude-barbier.jpg', 'Admire the modern skyline of La Defense in Paris.', 'CDG')")

# Inserimento dei dati per Madrid
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Madrid', 'Spain', 'https://images.unsplash.com/photo-1570698473651-b2de99bae12f?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Madrid is the capital city of Spain, known for its vibrant culture, art, and nightlife.', 'MAD')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Madrid', 'Spain', 'https://images.unsplash.com/photo-1578305698944-874fa44d04c9?q=80&w=1976&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Experience the lively atmosphere of Plaza Mayor in Madrid.', 'MAD')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Madrid', 'Spain', 'https://images.unsplash.com/photo-1585164917550-6f73d03dc019?q=80&w=2126&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Discover the art and history of the Prado Museum in Madrid.', 'MAD')")

# Inserimento dei dati per Barcellona
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcelona', 'Spain', 'https://images.unsplash.com/photo-1593368858664-a7fe556ab936?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Barcelona is known for its unique architecture, vibrant street life, and beautiful beaches.', 'BCN')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcelona', 'Spain', 'https://hips.hearstapps.com/gioit.h-cdn.co/assets/17/41/980x980/square-1507700367-sagradafamilia.jpg?resize=1200:*', 'Admire the stunning architecture of the Sagrada Familia in Barcelona.', 'BCN')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcelona', 'Spain', 'https://images.unsplash.com/photo-1568232094870-03e2b312ae4b?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 'Explore the colorful streets of the Gothic Quarter in Barcelona.', 'BCN')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcelona', 'Spain', 'https://www.sognandobarcellona.com/wp-content/uploads/2019/03/spiagge-barcellona.jpg', 'Relax on the beautiful beaches of Barcelona.', 'BCN')")

# Inserimento dei dati per Bankok
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Bangkok', 'Thailand', 'https://www.happyviaggithailandia.com/app/public/upload/THAILANDIA/bangkok/033.jpg', 'Bangkok is the capital city of Thailand, known for its vibrant street life, temples, and markets.', 'BKK')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Bangkok', 'Thailand', 'https://images.placesonline.com/photos/424011407170352_Bangkok_531675985.jpg', 'Experience the bustling energy of Bangkok''s Chinatown.', 'BKK')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Bangkok', 'Thailand', 'https://a.cdn-hotels.com/gdcs/production175/d369/48b05094-140a-4b33-a120-6147689c1a65.jpg?impolicy=fcrop&w=800&h=533&q=medium', 'Visit the famous floating markets of Bangkok.', 'BKK')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Bangkok', 'Thailand', 'https://media.cntraveler.com/photos/5b9802317009626e21e1e171/16:9/w_2560,c_limit/Chinatown_Bangkok_GettyImages-546022091.jpg', 'Explore the vibrant street food scene in Bangkok.', 'BKK')")

# Inserimento dei dati per Terni
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Terni', 'Italy', 'https://st3.idealista.it/news/archivie/styles/fullwidth_xl/public/2023-08/images/1280px-terni_cascate_delle_marmore_02_-_copia.jpg?VersionId=IWU5LV0ifRnGApBTr9klRzsZOFj6ZZbc&itok=A0554KAu', 'Terni is a city in central Italy known for the stunning Marmore Waterfalls.', 'PEG')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Terni', 'Italy', 'https://d5rzfs5ck83rq.cloudfront.net/_processed_/1/d/csm_foto_Terni_titolo_929bf688fb.jpg', 'Discover the beauty of Stifone and the Nera River Gorges near Terni.', 'PEG')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Terni', 'Italy', 'https://images.placesonline.com/photos/stifone_432797291-min-jpeg_226335_1624968220.jpg?quality=80&w=637', 'Enjoy the picturesque views of Piediluco Lake and the medieval Rocca Albornoziana.', 'PEG')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Terni', 'Italy', 'https://www.turismonarni.it/wp-content/uploads/2022/05/stifone-e-le-gole-del-nera-vista-aerea.jpg', 'Explore the charming town of Terni and its surrounding natural beauty.', 'PEG')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Terni', 'Italy', 'https://www.laportadellavalnerina.com/wp-content/uploads/2020/03/piediluco-e-rocca.jpg', 'Discover the historic village of Piediluco and its ancient fortress.', 'PEG')")

# Inserimento dei dati per Santorini
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Santorini', 'Greece', 'https://www.hachettebookgroup.com/wp-content/uploads/2020/03/Santorini.png?w=1024', 'Santorini is a Greek island known for its stunning sunsets and white-washed buildings.', 'JTR')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Santorini', 'Greece', 'https://static2-viaggi.corriereobjects.it/wp-content/uploads/2022/08/iStock-166471469-1080x720.jpg?v=1659884245', 'Explore the picturesque villages and beautiful beaches of Santorini.', 'JTR')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Santorini', 'Greece', 'https://transform.nws.ai/https%3A//cdn.thenewsroom.io/platform/story_media/1288797882/1036361536_oPBFLkx/w_1200,c_limit/', 'Experience the charm and beauty of Santorini''s traditional architecture.', 'JTR')")

# Inserimento dei dati per New York
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'New York', 'USA', 'https://media.tacdn.com/media/attractions-splice-spp-674x446/07/bd/6f/17.jpg', 'New York City is known for its iconic skyline, Broadway shows, and diverse culture.', 'JFK')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'New York', 'USA', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/New_york_times_square-terabass.jpg/1200px-New_york_times_square-terabass.jpg', 'Experience the energy of Times Square in the heart of New York City.', 'JFK')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'New York', 'USA', 'https://mywowo.net/media/images/cache/new_york_central_park_02_parte_sett_centrale_jpg_1200_630_cover_85.jpg', 'Relax and unwind in the natural beauty of Central Park in New York City.', 'JFK')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'New York', 'USA', 'https://imgcap.capturetheatlas.com/wp-content/uploads/2022/01/little-island-free-things-nyc.jpg', 'Visit Little Island, a unique park and cultural space on the Hudson River.', 'JFK')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'New York', 'USA', 'https://assets3.thrillist.com/v1/image/2680204/1200x630/flatten;crop_down;webp=auto;jpeg_quality=70', 'Discover hidden gems and off-the-beaten-path attractions in New York City.', 'JFK')")

# Inserimento dei dati per Los Angeles
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Los Angeles', 'USA', 'https://photos.zillowstatic.com/fp/84717aaf43b722f1e1e083c6b8e5f455-cc_ft_960.jpg', 'Los Angeles is known for its entertainment industry, beaches, and vibrant culture.', 'LAX')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Los Angeles', 'USA', 'https://www.multimediatravel.com/wp-content/uploads/sites/47/2021/12/tour-los-angeles-2022-dall-italia.jpg', 'Take a tour of Los Angeles and visit iconic landmarks like the Hollywood Sign.', 'LAX')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Los Angeles', 'USA', 'https://images.musement.com/cover/0001/43/los-angeles_header-42380.jpeg', 'Experience the vibrant energy of Downtown Los Angeles.', 'LAX')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Los Angeles', 'USA', 'https://live.staticflickr.com/65535/50997927805_b8b2182c82_b.jpg', 'Enjoy the sunshine and surf at the beaches of Los Angeles.', 'LAX')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Los Angeles', 'USA', 'https://i.pinimg.com/originals/f9/cc/4f/f9cc4f445fbaa2af81bf63f8a7a9562e.jpg', 'Discover the diverse neighborhoods and cultural attractions of Los Angeles.', 'LAX')")

# Inserimento dei dati per Londra
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'London', 'UK', 'https://www.lastrolabio.it/wp-content/uploads/2021/09/visitare-londra.jpg', 'London is the capital city of England, known for its historic landmarks, museums, and theater scene.', 'LHR')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'London', 'UK', 'https://mediaim.expedia.com/destination/1/9c375cff1e843ffe6c8b0f3c1d00a65e.jpg', 'Explore the iconic landmarks of London, such as the Tower Bridge and Big Ben.', 'LHR')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'London', 'UK', 'https://londonita.com/wp-content/uploads/2020/02/itineraio-city-di-Londra-min.jpg', 'Discover the historic charm of Covent Garden in London.', 'LHR')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'London', 'UK', 'https://thelondonlocal.com/wp-content/uploads/2022/07/cheap-non-touristy-things-to-do-in-london-colorful-london-neals-yard-1024x682.jpg', 'Find hidden gems like Neal''s Yard in London''s vibrant neighborhoods.', 'LHR')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'London', 'UK', 'https://a.cdn-hotels.com/gdcs/production0/d347/dc69d900-985f-432f-934c-6cbf968cb19d.jpg', 'Experience the cultural diversity of London and its world-class museums.', 'LHR')")

# Inserimento dei dati per Copenaghen
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Copenhagen', 'Denmark', 'https://scontent.ccdn.cloud/image/vivitravels-it/b9e4a4e0-c183-42df-a42a-72be17c20735/maxw-960.jpg', 'Copenhagen is the capital city of Denmark, known for its historic charm, green spaces, and cycling culture.', 'CPH')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Copenhagen', 'Denmark', 'https://www.helpviaggi.com/wp-content/uploads/2017/08/copenaghen-1.jpg', 'Explore the colorful streets and canals of Nyhavn in Copenhagen.', 'CPH')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Copenhagen', 'Denmark', 'https://eurasian.travel/wp-content/uploads/2018/05/Copenhagen_02-1721511_1920-1-1024x740.jpg', 'Visit the iconic Little Mermaid statue and picturesque harbor in Copenhagen.', 'CPH')")
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Copenhagen', 'Denmark', 'https://images.placesonline.com/photos/christiania_1343258141_148910_1658227287.jpg?quality=80&w=700', 'Experience the unique atmosphere of Freetown Christiania in Copenhagen.', 'CPH')")




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
