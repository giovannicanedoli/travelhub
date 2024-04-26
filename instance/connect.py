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
# Per Venezia, Italia (Marco Polo Airport - VCE)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Venezia', 'Italia', 'https://images.pexels.com/photos/2748019/pexels-photo-2748019.jpeg?auto=compress&cs=tinysrgb&w=600', 'Venezia, la città dei canali, incanta i visitatori con i suoi romantici ponti, i palazzi storici e le gondole che navigano lungo i canali.', 'VCE');")

# Per Firenze, Italia (Aeroporto di Firenze-Peretola - FLR)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Firenze', 'Italia', 'https://images.pexels.com/photos/21279856/pexels-photo-21279856/free-photo-of-ciutat-fita-edificis-italia.jpeg?auto=compress&cs=tinysrgb&w=600', 'Firenze, culla del Rinascimento, vanta capolavori artistici, una magnifica architettura e una deliziosa cucina toscana.', 'FLR');")

# Per Barcellona, Spagna (Aeroporto di Barcellona-El Prat - BCN)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Barcellona', 'Spagna', 'https://images.pexels.com/photos/819764/pexels-photo-819764.jpeg?auto=compress&cs=tinysrgb&w=600', 'Barcellona, una città cosmopolita e vibrante, affascina con le sue opere di Gaudí, le spiagge vivaci e la sua ricca cultura.', 'BCN');")

# Per Madrid, Spagna (Aeroporto di Madrid-Barajas Adolfo Suárez - MAD)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Madrid', 'Spagna', 'https://images.pexels.com/photos/3757144/pexels-photo-3757144.jpeg?auto=compress&cs=tinysrgb&w=600', 'Madrid, la capitale spagnola, è famosa per i suoi musei di fama mondiale, la sua movimentata vita notturna e le sue deliziose tapas.', 'MAD');")

# Per Siviglia, Spagna (Aeroporto di Siviglia-San Pablo - SVQ)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Siviglia', 'Spagna', 'https://images.pexels.com/photos/16778460/pexels-photo-16778460/free-photo-of-fita-pont-riu-viatjar.jpeg?auto=compress&cs=tinysrgb&w=600', 'Siviglia, con la sua affascinante architettura moresca, il flamenco appassionato e il caldo sole andaluso, incanta i visitatori di tutto il mondo.', 'SVQ');")

# Per Parigi, Francia (Aeroporto di Parigi-Charles de Gaulle - CDG)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Parigi', 'Francia', 'https://images.pexels.com/photos/699466/pexels-photo-699466.jpeg?auto=compress&cs=tinysrgb&w=600', 'Parigi, la città dell''amore, è famosa per la sua eleganza, i suoi monumenti iconici e la sua rinomata cucina francese.', 'CDG');")

# Per Nizza, Francia (Aeroporto di Nizza Costa Azzurra - NCE)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Nizza', 'Francia', 'https://th.bing.com/th/id/R.2abc086422f4cf184c9f8c3195b80e82?rik=bOBj4seixxpxNw&pid=ImgRaw&r=0', 'Nizza, situata sulla splendida Costa Azzurra, è conosciuta per le sue spiagge incantevoli, il suo clima mediterraneo e la sua eleganza raffinata.', 'NCE');")

# Per Lione, Francia (Aeroporto di Lione Saint-Exupéry - LYS)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Lione', 'Francia', 'https://images.pexels.com/photos/12204581/pexels-photo-12204581.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'Lione, con la sua ricca storia, la sua deliziosa gastronomia e la sua atmosfera vivace, è una delle città più affascinanti della Francia.', 'LYS');")

# Per Londra, Regno Unito (Aeroporto di Londra-Heathrow - LHR)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Londra', 'Regno Unito', 'https://th.bing.com/th/id/R.989003cdea6fb3dba534e689c9d35292?rik=2eELKBSQmDup4w&pid=ImgRaw&r=0', 'Londra, una metropoli cosmopolita, offre una miscela affascinante di storia antica, cultura contemporanea e vibrante vita urbana.', 'LHR');")

# Per Manchester, Regno Unito (Aeroporto di Manchester - MAN)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Manchester', 'Regno Unito', 'https://th.bing.com/th/id/R.6c9fcb614ed6ca19f4cd0881c47a67a2?rik=%2bg7e3yXt77aDTQ&pid=ImgRaw&r=0', 'Manchester, una città dinamica e creativa, è rinomata per la sua vivace scena musicale, i suoi club di calcio e la sua architettura industriale.', 'MAN');")

# Per Liverpool, Regno Unito (Aeroporto di Liverpool John Lennon - LPL)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Liverpool', 'Regno Unito', 'https://wallpaperaccess.com/full/2047388.jpg', 'Liverpool, città natale dei Beatles, vanta una ricca storia musicale, un''iconica waterfront e una vivace cultura.' , 'LPL');")

# Per Vienna, Austria (Aeroporto di Vienna-Schwechat - VIE)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Vienna', 'Austria', 'https://s29745.pcdn.co/wp-content/uploads/2019/08/2-Days-in-Vienna-Itinerary-1-1.jpeg', 'Vienna, la città della musica classica, è celebre per i suoi sontuosi palazzi imperiali, i suoi caffè storici e la sua scena culturale vibrante.', 'VIE');")

# Per Salisburgo, Austria (Aeroporto di Salisburgo-W. A. Mozart - SZG)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Salisburgo', 'Austria', 'https://th.bing.com/th/id/R.435a58beaf08556e930ee146ae5a13ff?rik=GTITcvTUZaEFxw&pid=ImgRaw&r=0', 'Salisburgo, città natale di Mozart, è rinomata per la sua architettura barocca, i suoi paesaggi alpini e il suo patrimonio musicale.', 'SZG');")

# Per Lisbona, Portogallo (Aeroporto di Lisbona-Portela - LIS)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Lisbona', 'Portogallo', 'https://th.bing.com/th/id/R.398ec897817e8d6760fda64b186b060e?rik=DKblE%2fvtNcYW6g&pid=ImgRaw&r=0', 'Lisbona, la capitale portoghese, affascina con le sue strade tortuose, le sue affascinanti colline e il suo affascinante mix di antico e moderno.', 'LIS');")

# Per Porto, Portogallo (Aeroporto di Porto-Francisco Sá Carneiro - OPO)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Porto', 'Portogallo', 'https://th.bing.com/th/id/R.cf19928187bdeb9e1e2c8e35d7b19abe?rik=PKqqDJPzthYzUg&pid=ImgRaw&r=0', 'Porto, famosa per il suo vino porto, i suoi pittoreschi vicoli e i suoi imponenti ponti, è una delle città più affascinanti del Portogallo.', 'OPO');")

# Per Amsterdam, Paesi Bassi (Aeroporto di Amsterdam-Schiphol - AMS)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Amsterdam', 'Paesi Bassi', 'https://th.bing.com/th/id/R.93a410a3f0667172e3966681b86dce0f?rik=I97bC62dt6NBPg&pid=ImgRaw&r=0', 'Amsterdam, con i suoi pittoreschi canali, i suoi musei eclettici e la sua vivace vita notturna, è una delle città più affascinanti d''Europa.', 'AMS');")

# Per Rotterdam, Paesi Bassi (Aeroporto di Rotterdam-Haag - RTM)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Rotterdam', 'Paesi Bassi', 'https://th.bing.com/th/id/R.8c0c6edd968b76637995d5d5c853bce8?rik=jEHC1Peod36fKw&pid=ImgRaw&r=0', 'Rotterdam, città portuale dinamica, è famosa per la sua architettura innovativa, i suoi vivaci mercati e la sua scena artistica.' , 'RTM');")

# Per Atene, Grecia (Aeroporto di Atene-Elefthérios Venizélos - ATH)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Atene', 'Grecia', 'https://images.pexels.com/photos/3224227/pexels-photo-3224227.jpeg', 'Atene, la culla della civiltà occidentale, vanta un ricco patrimonio archeologico, una vivace vita notturna e una deliziosa cucina mediterranea.', 'ATH');")

# Per Santorini, Grecia (Aeroporto di Santorini - JTR)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Santorini', 'Grecia', 'https://lp-cms-production.imgix.net/2021-05/shutterstockRF_1563449509.jpg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850&q=35&dpr=3', 'Santorini, con i suoi incantevoli tramonti, i suoi villaggi bianchi e blu e le sue spiagge vulcaniche, è una delle isole più belle della Grecia.', 'JTR');")

# Per Mykonos, Grecia (Aeroporto di Mykonos - JMK)
c.execute("INSERT INTO cities (like_messi, save_messi, nome, paese, photo, description, iata) VALUES (0, 0, 'Mykonos', 'Grecia', 'https://lp-cms-production.imgix.net/2021-05/0d787c5e1f6f4c9e7269c39e52752fd1-mykonos.jpg?auto=format&fit=crop&sharp=10&vib=20&ixlib=react-8.6.4&w=850&q=35&dpr=3', 'Mykonos, famosa per le sue spiagge di sabbia dorata, la sua vita notturna e il suo caratteristico labirinto di stradine, è una delle isole più alla moda della Grecia.', 'JMK');")



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

'''
roma colosseo https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1996&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
roma fontana di trevi https://images.unsplash.com/photo-1525874684015-58379d421a52?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
roma piazza san pietro https://images.unsplash.com/photo-1531572753322-ad063cecc140?q=80&w=2076&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
roma fori romani https://images.unsplash.com/photo-1678970388666-e50b8006ab51?q=80&w=2069&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D

parigi torre eiffel https://images.unsplash.com/photo-1439393161192-32360eb753f1?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
parigi louvre https://images.unsplash.com/photo-1587648415693-4a5362b2ce41?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
parigi https://images.unsplash.com/photo-1565457211452-16f8e7062a0a?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
parigi reggia di versailles https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Versailles-FacadeJardin.jpg/640px-Versailles-FacadeJardin.jpg


madrid ? https://images.unsplash.com/photo-1570698473651-b2de99bae12f?q=80&w=1936&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
madrid ? https://images.unsplash.com/photo-1578305698944-874fa44d04c9?q=80&w=1976&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
madrid ? https://images.unsplash.com/photo-1585164917550-6f73d03dc019?q=80&w=2126&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D

barcellona parco guell https://images.unsplash.com/photo-1593368858664-a7fe556ab936?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
barcellona sagrada familia https://hips.hearstapps.com/gioit.h-cdn.co/assets/17/41/980x980/square-1507700367-sagradafamilia.jpg?resize=1200:*
barcellona la pedrera https://images.unsplash.com/photo-1568232094870-03e2b312ae4b?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D



'''






conn.commit()

