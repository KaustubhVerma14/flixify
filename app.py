from flask import Flask, render_template, request
app=Flask(__name__)

movies=[
    
    {'id':"chhaava", 'title' : 'Chhaava', 'image':'Chhaava_film_poster.jpeg', 'description':"""Chhaava is a 2025 Indian Hindi-language
     historical action film based on the life of Sambhaji Maharaj, the second ruler of the Maratha Empire, who is
     played by Vicky Kaushal. An adaptation of the Marathi novel Chhava by Shivaji Sawant, it is directed by Laxman
     Utekar and produced by Dinesh Vijan under Maddock Films. The cast also includes Akshaye Khanna and Rashmika Mandanna.""",
     'trailer_url':"https://www.youtube.com/embed/77vRyWNqZjM"},
    
    {'id': "kabir_singh", 'title' : 'Kabir Singh', 'image':'kabir-singh.jpg', 'description':"""Kabir Singh is a 2019 Indian Hindi-language
     romantic drama film co-written, co-edited and directed by Sandeep Reddy Vanga and jointly produced by Bhushan 
    Kumar and Krishan Kumar under T-Series Films and Murad Khetani and Ashwin Varde under Cine1 Studios. A remake
     of Vanga's own Telugu film Arjun Reddy (2017), it stars Shahid Kapoor in the title role as a doctor who spirals
     into self-destruction when his girlfriend, played by Kiara Advani, marries someone else.""", 'trailer_url':
     "https://www.youtube.com/embed/RiANSSgCuJk"},
    
    {'id':"interstellar", 'title' : 'Interstellar', 'image':'interstellar.jpg', 'description':"""Interstellar is a 2014 epic science fiction
     film directed by Christopher Nolan, who co-wrote the screenplay with his brother Jonathan. It features an
     ensemble cast led by Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, and 
    Michael Caine. Set in a dystopian future where Earth is suffering from catastrophic blight and famine, the film
     follows a group of astronauts who travel through a wormhole near Saturn in search of a new home for mankind.""",
     'trailer_url':"https://www.youtube.com/embed/zSWdZVtXT7E"},
    
    {'id':"the_conjuring", 'title' : 'The Conjuring', 'image':'the_conjuring.jpeg', 'description':"""Based on a true story, The Conjuring is
      a 2013 American supernatural horror film directed by James Wan and written by Chad Hayes and Carey W. Hayes. It is the inaugural
     film in The Conjuring Universe franchise. Patrick Wilson and Vera Farmiga star as Ed and Lorraine Warren,
     paranormal investigators and authors associated with prominent cases of haunting. The Warrens come to the
     assistance of the Perron family, who experienced increasingly disturbing events in their newly occupied 
    farmhouse in Rhode Island in 1971.""", 'trailer_url':"https://www.youtube.com/embed/ejMMn0t58Lc"},

    {'id':"laila_majnu", 'title' : 'Laila Majnu', 'image':'laila_majnu.jpeg', 'description':"""Laila Majnu is a 2018 Indian Hindi-language
     romantic drama film starring Avinash Tiwary and newcomer Tripti Dimri. It is directed by Sajid Ali, presented
     by Imtiaz Ali and co-produced by Ekta Kapoor, Shobha Kapoor and Preety Ali. A contemporary retelling of the
     legendary Arabic tragedy Layla and Majnun, it follows two star-crossed lovers, Laila (Dimri) and Qais Bhatt
     (Tiwary) who are unable to unite as they face opposition from their families. However, when fate intervenes, 
     Laila marries another man while Qais goes to London. They reunite after four years, but end up waiting for each
     other.""", 'trailer_url':"https://www.youtube.com/embed/Cv-6cAHanZ8"},
    
    {'id':"animal", 'title' : 'Animal', 'image':'animal.jpeg', 'description':"""Animal is a 2023 Indian Hindi-language action drama
      film co-written, directed and edited by Sandeep Reddy Vanga and produced by T-Series Films, Bhadrakali Pictures 
     and Cine1 Studios. The film stars Ranbir Kapoor, Anil Kapoor, Bobby Deol, Rashmika Mandanna and Triptii Dimri.
      The film follows Ranvijay "Vijay" Singh, the son of a powerful industrialist, and his troubled relationship 
     with his father, which gets further jeopardized as he undergoes a brutal transformation and sets out on a path
      of vengeance and destruction after an assassination attempt on his father.""", 'trailer_url':"https://www.youtube.com/embed/8FkLRUJj-o0"},
    
    {'id':"avatar", 'title' : 'Avatar', 'image':'avatar.jpeg', 'description':"""Avatar is a 2009 epic science fiction film co-produced,
      co-edited, written, and directed by James Cameron. It features an ensemble cast including Sam Worthington, Zoe
      Saldana, Stephen Lang, Michelle Rodriguez, and Sigourney Weaver. The first installment in the Avatar film series,
      it is set in the mid-22nd century, when humans are colonizing Pandora, a lush habitable moon of a gas giant in
      the Alpha Centauri star system, in order to mine the valuable unobtanium, a room-temperature superconductor
     mineral. The expansion of the mining colony threatens the continued existence of a local tribe of Na'vi, a
      humanoid species indigenous to Pandora. The title of the film refers to a genetically engineered Na'vi body
      operated from the brain of a remotely located human that is used to interact with the natives of Pandora
      called an "Avatar".""", 'trailer_url':"https://www.youtube.com/embed/5PSNL1qE6VY"},
    
    {'id':"veronica", 'title' : 'Veronica', 'image':'veronica.jpeg', 'description':"""Based on a true story, Veronica is a 2017 Spanish supernatural horror
      film directed by Paco Plaza which stars Sandra Escacena alongside Claudia Placer, Bruna González, Iván Chavero
      and Ana Torrent. It is loosely based on true events from a 1991 Vallecas case in which Estefanía Gutiérrez
      Lázaro died mysteriously after séance using a ouija board.""", 'trailer_url':"https://www.youtube.com/embed/-FUm6t-rfEs"},
    
    {'id':"the_exorcist", 'title' : 'The Exorcist', 'image':'the_exorcist.jpeg', 'description':"""Based on a true story, The Exorcist is a 1973 American
      supernatural horror film directed by William Friedkin from a screenplay by William Peter Blatty, based on his
      1971 novel by the same name. The film stars Ellen Burstyn, Max von Sydow, Jason Miller, and Linda Blair, and 
     follows the demonic possession of a young girl and the attempt to rescue her through an exorcism by two 
     Catholic priests. The Exorcist is considered to be one the most horrifying movies ever made.""", 'trailer_url':
     "https://www.youtube.com/embed/BU2eYAO31Cc"},
    
    {'id':"inception", 'title' : 'Inception', 'image':'inception.jpeg', 'description': """Inception is a 2010 science fiction action
      heist film written and directed by Christopher Nolan, who also produced it with Emma Thomas, his wife. The film
      stars Leonardo DiCaprio as a professional thief who steals information by infiltrating the subconscious of his 
     targets. He is offered a chance to have his criminal history erased as payment for the implantation of another
      person's idea into a target's subconscious. The ensemble cast includes Ken Watanabe, Joseph Gordon-Levitt, 
     Marion Cotillard, Elliot Page, Tom Hardy, Cillian Murphy, Tom Berenger, Dileep Rao, and Michael Caine.""", 
     'trailer_url':"https://www.youtube.com/embed/YoHD9XEInc0"},
    
    {'id':"shutter_island", 'title' : 'Shutter Island', 'image':'shutter_island.jpeg', 'description':"""Shutter Island is a 2010 American
      neo-noir psychological horror film directed by Martin Scorsese. It is adapted by Laeta Kalogridis from the 2003
      novel of the same name by Dennis Lehane, about a Deputy U.S. Marshall who comes to Shutter Island to investigate
      a psychiatric facility after one of the patients goes missing. It stars Leonardo DiCaprio and Mark Ruffalo, with
      Ben Kingsley, Max von Sydow and Michelle Williams in supporting roles.""", 'trailer_url':"https://www.youtube.com/embed/v8yrZSkKxTA"},
    
    {'id':"the_shawshank_redemption", 'title' : 'The Shawshank Redemption', 'image':'shawshank_redemption.jpeg', 'description':"""The Shawshank 
     Redemption is a 1994 American prison drama film written and directed by Frank Darabont, based on the 1982 
     Stephen King novella Rita Hayworth and Shawshank Redemption. The film tells the story of banker Andy Dufresne 
     (Tim Robbins), who is sentenced to life in Shawshank State Penitentiary for the murders of his wife and her lover,
      despite his claims of innocence. Over the following two decades, he befriends a fellow prisoner, contraband 
     smuggler Ellis "Red" Redding (Morgan Freeman), and becomes instrumental in a money laundering operation led by 
     the prison warden Samuel Norton (Bob Gunton). William Sadler, Clancy Brown, Gil Bellows, and James Whitmore
      appear in supporting roles.""", 'trailer_url':"https://www.youtube.com/embed/PLl99DlL6b4"},
    
    {'id':"evil_dead_rise", 'title' : 'Evil Dead Rise', 'image':'evil_dead_rise.jpg', 'description': """Evil Dead Rise is a 2023 American 
     supernatural horror film written and directed by Lee Cronin. It is the second standalone entry and the fifth 
     installment in the Evil Dead film series. The film stars Lily Sullivan and Alyssa Sutherland as two estranged 
     sisters trying to survive and save their family from deadites. Morgan Davies, Gabrielle Echols, and Nell Fisher
      (in her film debut) appear in supporting roles.""", 'trailer_url':"https://www.youtube.com/embed/smTK_AeAPHs"},
    
    {'id':"rockstar", 'title' : 'Rockstar', 'image':'rockstar.jpeg', 'description':"""Rockstar is a 2011 Indian Hindi-language musical
      romantic drama film written and directed by Imtiaz Ali. The film stars Ranbir Kapoor and Nargis Fakhri in lead 
     roles, with Aditi Rao Hydari, Piyush Mishra, Shernaz Patel, Kumud Mishra, Sanjana Sanghi, Aakash Dahiya and Shammi
      Kapoor in pivotal supporting roles. The soundtrack was composed by A. R. Rahman. The film marks the posthumous 
     screen appearance of Shammi Kapoor, following his death on 14 August 2011.""", 'trailer_url':"https://www.youtube.com/embed/bD5FShPZdpw"},
    
    {'id':"jab_we_met", 'title' : 'Jab We Met', 'image':'jab_we_met.jpeg', 'description':"""Jab We Met is a 2007 Indian Hindi-language
      romantic comedy film written and directed by Imtiaz Ali and produced by Dhilin Mehta under his banner Shree 
     Ashtavinayak Cine Vision. The film stars Shahid Kapoor and Kareena Kapoor with Tarun Arora, Saumya Tandon and
      Dara Singh in supporting roles.""", 'trailer_url':"https://www.youtube.com/embed/VoaKuOjez9k"},
    
    {'id':"oppenheimer", 'title' : 'Oppenheimer', 'image':'oppenheimer.jpeg', 'description':"""Oppenheimer is a 2023 epic biographical 
     drama film written, produced, and directed by Christopher Nolan. It follows the life of J. Robert Oppenheimer,
      the American theoretical physicist who helped develop the first nuclear weapons during World War II. Based on 
     the 2005 biography American Prometheus by Kai Bird and Martin J. Sherwin, the film dramatizes Oppenheimer's 
     studies, his direction of the Los Alamos Laboratory and his 1954 security hearing. Cillian Murphy stars as
      Oppenheimer, alongside Robert Downey Jr. as the United States Atomic Energy Commission member Lewis Strauss. 
     The ensemble supporting cast includes Emily Blunt, Matt Damon, Florence Pugh, Josh Hartnett, Casey Affleck, 
     Rami Malek, and Kenneth Branagh.""", 'trailer_url':"https://www.youtube.com/embed/uYPbbksJxIg"},
    
    {'id':"peaky_blinders", 'title' : 'Peaky Blinders', 'image':'peaky_blinders.jpeg', 'description':"""Peaky Blinders is a British period
      crime drama television series created by Steven Knight. Set in Birmingham, it follows the exploits of the Peaky
      Blinders crime gang in the direct aftermath of the First World War. The fictional gang is loosely based on a real
      urban youth gang active in the city from the 1880s to the 1920s.The series features an ensemble cast led by
      Cillian Murphy, starring as Tommy Shelby, Helen McCrory as Elizabeth "Polly" Gray, Paul Anderson as Arthur
      Shelby, Sophie Rundle as Ada Shelby, and Joe Cole as John Shelby, the gang's senior members.""", 'trailer_url':
      "https://www.youtube.com/embed/oVzVdvGIC7U"},
    
    {'id':"annabelle", 'title' : 'Annabelle', 'image':'annabelle.jpeg', 'description':"""Based on a true story, Annabelle is a 2014 American supernatural 
     horror film directed by John R. Leonetti, written by Gary Dauberman and produced by Peter Safran and James Wan. 
     It stars Annabelle Wallis, Ward Horton, and Alfre Woodard. Principal photography began in January 2014 in Los 
     Angeles. It premiered at the TCL Chinese Theatre in Los Angeles on September 29, 2014, and was theatrically 
     released in the United States on October 3, 2014, by Warner Bros. Pictures and New Line Cinema. The film was 
     inspired by a story of a doll named Annabelle by Ed and Lorraine Warren. It is a spin-off and prequel to the 2013 
     film The Conjuring, and the second installment overall in The Conjuring Universe and was announced shortly after 
     the release of that movie because of its worldwide box office success and positive reception of the depiction of 
     the doll.""", 'trailer_url':"https://www.youtube.com/embed/paFgQNPGlsg?"},
    
    {'id':"the_curse_of_la_llorona", 'title' : 'The Curse of La Llorona', 'image':'the_curse_of_la_llorona.jpeg','description':"""Based on a real legend followed in the Latin American countries, The Curse of La 
     Llorona (also known as The Curse of the Weeping Woman in some markets) is a 2019 American supernatural horror 
     film directed by Michael Chaves, in his feature directorial debut, and written by Mikki Daughtry and Tobias 
     Iaconis. Based on the Latin American folklore of La Llorona, the film stars Linda Cardellini, Raymond Cruz, and 
     Patricia Velásquez, and follows a mother in 1973 Los Angeles who must save her children from a malevolent spirit 
     trying to steal them. The film was produced by James Wan through his Atomic Monster banner and, though not 
     considered an installment in the franchise, takes place within The Conjuring Universe.""", 'trailer_url':
     "https://www.youtube.com/embed/uOV-xMYQ7sk"},
    
    {'id':"phir_hera_pheri", 'title' : 'Phir Hera Pheri', 'image':'phir_hera_pheri.jpeg', 'description':"""Phir Hera Pheri is a 2006 Indian
      Hindi-language heist comedy drama written and directed by Neeraj Vora. The film serves as the sequel to Hera 
     Pheri (2000) and the second installment of the Hera Pheri franchise. The film stars an ensemble cast of Akshay 
     Kumar, Suniel Shetty, Paresh Rawal (reprising their roles from the previous film), Bipasha Basu, Rimi Sen, Sharat
      Saxena, Johnny Lever, Rajpal Yadav, Milind Gunaji, Manoj Joshi and Razak Khan. Following the events of the previous
      film, a twist of fate changes the lives of Raju (Kumar), Shyam (Shetty) and Babu (Rawal) when they get cheated by
      a fraudster, Anuradha (Basu). They must now find another way to repay the money borrowed from a dreaded gangster, 
     Tiwari (Saxena).""", 'trailer_url':"https://www.youtube.com/embed/1rJQQCZcq2s"},

     {'id':"bhool_bhulaiyaa", 'title' : 'Bhool Bhulaiyaa', 'image':'bhool_bhulaiyaa.jpeg', 'description':"""Bhool Bhulaiyaa is a 2007 Indian
       Hindi-language psychological horror comedy film directed by Priyadarshan from a screenplay by Neeraj Vora and
       produced by T Series. It is a remake of the 1993 Malayalam-language film Manichitrathazhu written by Madhu Muttam
       and directed by Fazil, which is based on a 19th-century tragedy that happened at Madhu's Alummoottil tharavad 
      (an old traditional mansion) in Muttom (near Haripad) in central Travancore. The film stars Akshay Kumar, Vidya 
      Balan, Shiney Ahuja, and Ameesha Patel, alongside Paresh Rawal, Rajpal Yadav, Manoj Joshi, Asrani and Vikram 
      Gokhale. The film score and soundtrack were composed by Ranjit Barot and Pritam respectively, with lyrics written 
      by Sameer and Sayeed Quadri.""", 'trailer_url':"https://www.youtube.com/embed/ss-7iGf1xE8"},

      {'id':"bhool_bhulaiyaa_2", 'title' : 'Bhool Bhulaiyaa 2', 'image':'Bhool_Bhulaiyaa2.jpg', 'description':"""Bhool Bhulaiyaa 2 is a 2022
        Indian Hindi-language supernatural horror comedy film directed by Anees Bazmee, written by Aakash Kaushik and 
       Farhad Samji, and produced by T-Series Films and Cine1 Studios. It is a standalone sequel to the 2007 film Bhool 
       Bhulaiyaa (2007). The film stars Tabu, Kartik Aaryan, and Kiara Advani, and follows Ruhaan Randhawa, who has to 
       pose as a fraud psychic to deal with the return of Manjulika, a malevolent spirit hell-bent on vengeance against 
       the Thakur family.""", 'trailer_url':"https://www.youtube.com/embed/P2KRKxAb2ek"},

      {'id':"bhool_bhulaiyaa_3", 'title' : 'Bhool Bhulaiyaa 3', 'image':'bhool_bhulaiyaa3.jpg', 'description':"""Bhool Bhulaiyaa 3 is a 2024
        Indian Hindi-language comedy horror film directed by Anees Bazmee, written by Aakash Kaushik, and produced by
        T-Series Films and Cine1 Studios. It serves as the third installment of the eponymous franchise after Bhool 
       Bhulaiyaa (2007) and Bhool Bhulaiyaa 2 (2022). It stars Kartik Aaryan, Vidya Balan, Madhuri Dixit and Triptii 
       Dimri, and is set in Kolkata.""", 'trailer_url':"https://www.youtube.com/embed/6YMY62tMLUA"},

      {'id':"zindagi_na_milegi_dobara", 'title' : 'Zindagi Na Milegi Dobara', 'image':'Zindagi_Na_Milegi_Dobara.jpg', 'description':"""Zindagi Na 
       Milegi Dobara, is a 2011 Indian Hindi-language road comedy drama film directed by Zoya Akhtar and produced by 
       Farhan Akhtar and Ritesh Sidhwani under Excel Entertainment. The film stars an ensemble cast of Hrithik Roshan, 
       Abhay Deol, Farhan Akhtar, Katrina Kaif, and Kalki Koechlin. The film's story follows three childhood friends, 
       Arjun, Kabir, and Imran, who reunite for a three-week road trip. They set off to Spain and meet Laila, who falls in 
       love with Arjun and helps him overcome his compulsion to work. Kabir and his fiancée Natasha experience significant 
       misunderstandings, while Imran wishes to meet his biological father, an artist.""", 'trailer_url':"https://www.youtube.com/embed/FJrpcDgC3zU"},

       {'id':"brahmastra", 'title' : 'Brahmastra', 'image':'brahmastra.jpg', 'description':"""Brahmastra: Part One – Shiva is a 2022 Indian 
        Hindi-language fantasy action-adventure film written and directed by Ayan Mukerji and produced by Karan Johar, 
        Apoorva Mehta, Hiroo Yash Johar, Namit Malhotra and Mukerji (in his debut production) – under Dharma Productions, 
        Starlight Pictures and Prime Focus in association with Star Studios, along with Ranbir Kapoor and Marijke DeSouza. 
        The film serves as the first instalment of a planned trilogy, which is itself planned to be part of a cinematic 
        universe titled Āstraverse, and stars an ensemble cast including Amitabh Bachchan, Ranbir Kapoor, Alia Bhatt, 
        Mouni Roy and Nagarjuna with Shah Rukh Khan in a special appearance. Drawing inspiration from tales in Hindu 
        mythology, the story follows Shiva, an orphaned musician with pyrokinetic powers who discovers that he is an astra, 
        a weapon of enormous energy. He attempts to prevent the strongest of the astras, the Brahmāstra, from falling 
        into the hands of dark forces that share a history with him.""", 'trailer_url':"https://www.youtube.com/embed/BUjXzrgntcY"},

        {'id':"joker", 'title' : 'Joker', 'image':'joker.jpg', 'description':"""Joker is a 2019 American psychological thriller 
         film directed by Todd Phillips from a screenplay he co-wrote with Scott Silver. Based on DC Comics characters, 
         it stars Joaquin Phoenix and provides an alternative origin story for the Joker. The film follows Arthur Fleck, a 
         failed clown and aspiring stand-up comedian whose descent into mental illness and nihilism inspires a violent 
         countercultural revolution against the wealthy in a decaying Gotham City. Robert De Niro, Zazie Beetz, and Frances 
         Conroy appear in supporting roles. Distributed by Warner Bros. Pictures, Joker was produced by Warner Bros. 
         Pictures and DC Films in association with Village Roadshow Pictures, Bron Creative and Joint Effort.""", 
         'trailer_url':"https://www.youtube.com/embed/zAGVQLHvwOY"},

         {'id':"joker_folie_à_deux", 'title' : 'Joker: Folie à Deux', 'image':'joker2.jpg', 'description':"""Joker: Folie à Deux is a 2024 
          American jukebox musical legal drama film directed by Todd Phillips from a screenplay he co-wrote with 
          Scott Silver. Based on DC Comics characters, it is the sequel to Joker (2019) and stars Joaquin Phoenix 
          reprising his role as Arthur Fleck / Joker, alongside Lady Gaga as Harley "Lee" Quinzel. The supporting 
          cast includes Brendan Gleeson, Catherine Keener, Zazie Beetz, Steve Coogan, Harry Lawtey, and Leigh Gill. 
          In the film, Arthur awaits trial for his crimes at Arkham State Hospital where he develops a romantic 
          relationship with another inmate.""", 'trailer_url':"https://www.youtube.com/embed/_OKAwz2MsJs"}
] 

@app.route('/')
def home():
    query= request.args.get('query','').lower()
    if query:
        filtered_movies = [movie for movie in movies if query in movie.get('title','').lower()]
    else:
        filtered_movies = movies
    return render_template('index.html', movies=filtered_movies)

@app.route('/movie/<movie_id>')
def movie_detail(movie_id):
    movie = next((m for m in movies if m['id'] == movie_id), None)
    if movie:
        return render_template('movie.html',movie=movie)
    else:
        return "Movie not found", 404
    

if __name__=='__main__':
    app.run(debug=True)
