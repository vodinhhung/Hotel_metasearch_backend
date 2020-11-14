from hotel.models import Root, User, Like, View

# Like or Unlike the hotel of a user
def save_like(hotel_id, user_id):
    action = 0
    user = User.objects.get(social_id = user_id)

    if not Like.objects.filter(root_id = hotel_id, user_id=user.index).exists():
        like = Like(
            root_id = hotel_id,
            user_id = user.index,
            status = 1
        )
        like.save()
        action = 1
    else:
        like = Like.objects.get(
            root_id = hotel_id,
            user_id = user.index
        )
        
        if like.status == 1:
            like.status = 0
        else:
            like.status = 1
            action = 1
        
        like.save()
    
    return [True, action]

def save_view(hotel_id, user_id):
    user = User.objects.get(social_id = user_id)

    # Insert view to database
    if View.objects.filter(root_id = hotel_id, user_id = user.index).exists():
        view = View.objects.filter(
            root_id = hotel_id,
            user_id = user.index
        )
        view.delete()
    
    view = View(
        root_id = hotel_id,
        user_id = user.index
    )
    view.save()

    return True