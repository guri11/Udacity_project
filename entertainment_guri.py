import fresh_tomatoes
import media


alien_Covenant = media.Movie('Alien:Covenant',
                             'Ridley Scott returns to the universe he created,'
                             ' with ALIEN: COVENANT, a new chapter in his'
                             ' groundbreaking ALIEN franchise. The crew of'
                             ' the colony ship Covenant, bound for a remote'
                             ' planet on the far side of the galaxy, discovers'
                             'what they think is an uncharted paradise, but is'
                             ' actually a dark, dangerous world. When they '
                             'uncover a threat beyond their imagination, they'
                             'must attempt a harrowing escape.',
                             'https://upload.wikimedia.org/wikipedia/en/3/33/'
                             'Alien_Covenant_Teaser_Poster.jpg',
                             'https://www.youtube.com/watch?v=H0VW6sg50Pk')


the_Lego_Batman_Movie = media.Movie('The LEGO Batman Movie',
                                    'There are big changes brewing in Gotham'
                                    ' City, and if he wants to save the city'
                                    ' from The Jokers hostile takeover, Batman'
                                    ' may have to drop the lone vigilante'
                                    ' thing, try to work with others and maybe'
                                    ' just maybe, learn to lighten up.',
                                    'https://upload.wikimedia.org/wikipedia/'
                                    'en/6/61/The_Lego_Batman_Movie_'
                                    'PromotionalPoster.jpg',
                                    'https://www.youtube.com/'
                                    'watch?v=HbwrGI_NbfY')

man_of_steel = media.Movie('Man of Steel',
                           "Man of Steel is a 2013 superhero film featuring"
                           "the DC Comics character Superman. It is a"
                           "British-American venture produced by Legendary "
                           "Pictures, DC Entertainment, Syncopy Inc., and "
                           "Cruel and Unusual Films, and distributed by "
                           "Warner Bros. Pictures. It is the first "
                           "installment in the DC Extended Universe. The film "
                           "is directed by Zack Snyder, written by David S. "
                           "Goyer, and stars Henry Cavill, Amy Adams, "
                           "Michael Shannon, Kevin Costner, Diane Lane,"
                           "Laurence Fishburne, Antje Traue, Ayelet Zurer, "
                           "Christopher Meloni, and Russell Crowe. "
                           "Man of Steel is a reboot of the Superman film "
                           "series that retells the characters origin "
                           "story. In the film, Clark Kent learns that "
                           "he is a superpowered alien from the planet "
                           "Krypton and assumes the role of mankind "
                           "protector as Superman, but finds himself "
                           "having to prevent General Zod from "
                           "destroying humanity.",
                           'https://upload.wikimedia.org/wikipedia/en/8/85/'
                           'ManofSteelFinalPoster.jpg',
                           'https://www.youtube.com/watch?v=T6DJcgm3wNY')

it = media.Movie('IT',
                 'New Line Cinemas horror thriller "IT,"'
                 'directed by Andy Muschietti ("Mama"), is based on the hugely'
                 ' popular Stephen King novel of the same name, which has been'
                 ' terrifying readers for decades. When children begin to'
                 ' disappear in the town of Derry, Maine, a group of young'
                 ' kids are faced with their biggest fears when they square'
                 ' off against an evil clown named Pennywise, whose history'
                 ' of murder and violence dates back for centuries.',
                 'https://upload.wikimedia.org/wikipedia/en/5/5a/'
                 'It_%282017%29_poster.jpg',
                 'https://www.youtube.com/watch?v=xKJmEC5ieOk')

kingsman_the_golden_circle = media.Movie('KINGSMAN: THE GOLDEN CIRCLE',
                                         '"Kingsman: The Secret Service"'
                                         ' introduced the world to Kingsman -'
                                         ' an independent, international '
                                         'intelligence agency operating at the'
                                         'highest level of discretion, whose'
                                         ' ultimate goal is to keep the world'
                                         ' safe. In "Kingsman: The Golden'
                                         ' Circle," our heroes face a new'
                                         ' challenge. When their headquarters'
                                         ' are destroyed and the world is held'
                                         'hostage, their journey leads them to'
                                         ' the discovery of an allied spy'
                                         ' organization in the US called'
                                         'Statesman, dating back to the day'
                                         ' they were both founded. In a new'
                                         ' adventure that tests their agents'
                                         ' strength and wits to the limit, '
                                         'these two elite secret organizations'
                                         ' band together to defeat a ruthless'
                                         ' common enemy, in order to save the'
                                         ' world, something that is becoming a'
                                         ' bit of a habit for Eggsy...',
                                         'https://upload.wikimedia.org/'
                                         'wikipedia/en/f/fb/'
                                         'Kingsman_The_Golden_Circle.png',
                                         'https://www.youtube.com/'
                                         'watch?v=0fvqnGmr9S8')

the_man_who_knew_infinity = media.Movie("The Man Who Knew Infinity",
                                        'The Man Who Knew Infinity is the true'
                                        'story of friendship that forever'
                                        ' changed mathematics. In 1913,'
                                        ' Srinivasa Ramanujan (Dev Patel),'
                                        ' a self-taught Indian mathematics'
                                        ' genius, traveled to Trinity College,'
                                        ' Cambridge, where over the course of'
                                        ' five years, forged a bond with his'
                                        ' mentor, the brilliant and eccentric'
                                        'professor, G.H. Hardy (Jeremy Irons),'
                                        ' and fought against prejudice to '
                                        'reveal his mathematic genius to the '
                                        'world.',
                                        'https://upload.wikimedia.org'
                                        '/wikipedia/en/d/d8/The_Man_Who_Knew_'
                                        'Infinity_%28film%29.jpg',
                                        'https://www.youtube.com/'
                                        'watch?v=NP0lUqNAw3k')

movies = [
          alien_Covenant,
          the_Lego_Batman_Movie,
          man_of_steel, it,
          kingsman_the_golden_circle, the_man_who_knew_infinity]
fresh_tomatoes.open_movies_page(movies)
