from decimal import Decimal
from django.conf import settings
from main.models import Movie


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Duyệt item trong cart và lấy phim từ trong cơ sở dữ liệu
        """
        movie_ids = self.cart.keys()
        all_movie = Movie.objects.filter(id__in=movie_ids)
        sub_cart = self.cart.copy()

        for movie in all_movie:
            sub_cart[str(movie.id)]["movie"] = movie

        for item in sub_cart.values():
            item["price"] = Decimal(item["price"])
            yield item

    def __len__(self):
        # Lấy chiều dìa
        return len(self.cart.values())

    def get_total_price(self):
        return sum([Decimal(item["price"]) for item in self.cart.values()])

    def clear(self):

        del self.session[settings.CART_SESSION_ID]
        self.save()

    def add(self, movie):

        movie_id = str(movie.id)

        if movie_id not in self.cart:
            self.cart[movie_id] = {"price": str(movie.price)}

        self.save()

    def save(self):
        """Lưu thông tin sản phẩm"""
        self.session.modified = True

    def remove(self, movie):
        """Xóa sản phẩm ra khỏi giỏ hàng"""
        movie_id = str(movie.id)

        if movie_id in self.cart:
            del self.cart[movie_id]
        self.save()
