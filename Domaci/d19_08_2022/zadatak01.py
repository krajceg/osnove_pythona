from facebookPost import FacebookPost

fb_post = FacebookPost("Svetolik Kljajic", "Pera Peric",
                       "Ovo je tekst objave", 4, 1)

fb_post.like()
fb_post.like()
fb_post.dislike()

fb_post.share()

fb_post.print()
