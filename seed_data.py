from SocialTravel.models import Post
for _ in range(0,100):
    Post(carousel_caption_title= "un carousel title",
        carousel_caption_description="Un carousle description",
        heading="Mi viaje",
        description="una descripcion",     
    ).save()

