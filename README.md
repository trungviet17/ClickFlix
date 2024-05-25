# ClickFlix

<p align='center'>
<img src="https://img.shields.io/badge/Django-239120?logo=django&logoColor=white" />
<img src="https://img.shields.io/badge/Python-239120?logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SQL%20Server-CC2927?logo=microsoft-sql-server&logoColor=white" />
<img src="https://img.shields.io/badge/html5-E34F26?logo=html5&logoColor=white" />
<img src="https://img.shields.io/badge/css3-1572B6?logo=css3&logoColor=white" />
<img src="https://img.shields.io/badge/bootstrap-563D7C?logo=bootstrap&logoColor=white" />
<img src="https://img.shields.io/badge/Github-181717?logo=github&logoColor=white" />

</p>


<hr class="dotted">
Bạn là một "mọt phim" chính hiệu? Bạn luôn tìm kiếm những bộ phim hay và mới nhất để xem? Vậy thì bạn không thể bỏ qua ClickFlix, trang web bán phim uy tín hàng đầu Việt Nam.

Với kho phim khổng lồ, đa dạng thể loại, chất lượng hình ảnh và âm thanh tuyệt hảo, cùng mức giá cạnh tranh và nhiều ưu đãi hấp dẫn, ClickFlix mang đến cho bạn trải nghiệm xem phim trực tuyến tuyệt vời nhất.
## About this Project:

Đây là bài tập lớn môn Thực hành phát triển hệ thống Học Máy (AIT3004_1) với chủ đề trang web mua bán, xem phim trực tuyến.

Đây là hệ thống được xây dựng bằng Django, nó chứa tập dữ liệu với hơn 30000 phim và 50000 thông tin về diễn viên được lấy từ trang web [TMDB](https://www.themoviedb.org/) .

Hệ thống cho phép người dùng đăng nhập, đăng ký, xem phim, xem thông tin chi tiết về phim, xem thông tin chi tiết về phim. Cung cấp giao diện dựa trên bootstrap, html, CSS. Đồng thời bao gồm hệ thống đề xuất dựa trên nội dung tìm kiếm của người dùng

Connect with me at:




## Thông tin phiên bản sử dụng:

```
django==5.0.6
python-dotenv==1.0.1
django-jazzmin==3.0.0
django-extensions==3.2.3
pandas==2.2.2
scikit-learn==1.5.0
stripe==9.8.0
tqdm==4.66.4
pre-commit==3.7.1
mysqlclient==2.2.4
```

## Cách sử dụng:

Cloning the Repository:

```
$ git clone https://github.com/fl4viooliveira/django_ecommerce.git

$ cd django_ecommerce

```

Install thư viện venv để tạo môi trường ảo trong python:

```
$ pip install virtualenv

$ virtualenv env

```

Kích hoạt môi trường ảo:

trên Windows:
```
env\Scripts\activate

```
trên Mac OS / Linux:
```
$ source env/bin/activate

```

Cài đặt những thu viện cần thiết :

```
$ cd myclickflix
$ pip install -r requirements.txt

```

Tạo một file .env trong thư mục myclickflix  để thiết lập tất cả các thư viện cần thiết. Khi đặt giá trị cho các biến môi trường, không được sử dụng khoảng trắng sau dấu "=".

```
EMAIL_CLICKFLIX_PASSWORD =
STRIPE_PUBLISHABLE_KEY =
STRIPE_SECRET_KEY =

```

Chạy lệnh sau để khởi động:

```
$ python manage.py makemigrations

$ python manage.py migrate

```
Khởi tạo super user:

```
$ python manage.py createsuperuser admin-name

```

Chạy server:

```
$ python manage.py runserver

```

## Contributing

Dự án nhóm bao gồm 4 thành viên sau :

<table>
<tr>
<td align="center" valign="top" width="14.28%"><a href="https://github.com/trungviet17"><img src="https://avatars.githubusercontent.com/u/113108053?v=4" width="100px;" /><br /><sub><b>Nguyễn Ngô Việt Trung</b></sub></a><br/></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/NguyenTuoc2807"><img src="https://avatars.githubusercontent.com/u/126454793?v=4" width="100px;" alt="Jeroen Engels"/><br /><sub><b>Nguyễn Đức Tước</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/quangster"><img src="https://avatars.githubusercontent.com/u/111344095?v=4" width="100px;" alt="Jake Bolam"/><br /><sub><b>Bùi Duy Quảng</b></sub></a><br /></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/CarolFiuf"><img src="https://avatars.githubusercontent.com/u/120015543?v=4" width="100px;" alt="Tyler Benning"/><br /><sub><b>Nguyễn Tiến Trung</b></sub></a><br /></td>
</tr>
</table>

## License

<a href="https://github.com/fl4viooliveira/django_ecommerce/blob/master/LICENSE">
    <img alt="NPM" src="https://img.shields.io/npm/l/license?style=for-the-badge">
</a>&nbsp;&nbsp;

 [LICENSE.md](https://github.com/fl4viooliveira/django_ecommerce/blob/master/LICENSE) file for details.
