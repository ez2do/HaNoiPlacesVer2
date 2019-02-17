from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Place, Base

engine = create_engine('sqlite:///places.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

p1 = Place(name='Ho Guom', description='Good place to walk, eat ice cream and watch butt', rate_times = 0, total_point = 0, img_path='img/6 (2).jpg', type='lake', rating = 0)
p2 = Place(name='Thanh Nien Road', description='Also have good ice scream, kick duck boat is a good try, very luxury restaurant on the lake but I don\'t care, "the more curve, the more danger" is suitable for this road', rate_times = 0, total_point = 0, img_path='img/Hanoi.jpg', type='road', rating = 0)
p3 = Place(name='Ho Tay', description='Large, running a round the lake per day is the good warm up, suitable for many activities from exercise, fishing, "kicking tone" for couples and try new grass or herbal for young man.', rate_times = 0, total_point = 0, img_path='img/The-West-Lake-ha-noi-viet-nam.jpg', type='lake', rating = 0)
p4 = Place(name='Nha Hat Lon', description='Look gorgerous outside but always closed, just well acting as background for many photos, also using to host some big event like "new year eve", "mid-autumn",... After that, nilon-bag is all the remaining.', rate_times = 0, total_point = 0, img_path='img/FRENCH-QUARTER-1.jpg', type='historical building', rating = 0)
p5 = Place(name='Chua 1 Cot', description='Never come here, fill in later but very impressed by its unique style', rate_times = 0, total_point = 0, img_path='img/hanoi-travel-guide-from-a-to-z-amazingthingsinvietnam30.jpg', type='pagoda', rating = 0)
p6 = Place(name='Cau Nhat Tan', description='Built by Japan. No need to talk more about it, every thinngs Japan made is great, especially their movies.', rate_times = 0, total_point = 0, img_path='img/Thuc hien nhiem vu.jpg', type='bridge', rating = 0)
p7 = Place(name='Vuon Bach Thao', description='Just heard about it but not come here, seem to be a good place to provide more oxygen.', rate_times = 0, total_point = 0, img_path='img/five-ideal-places-to-take-photos-in-hanoi-3aa3.jpg', type='park', rating = 0)
p8 = Place(name='Cafe Mai Nha', description='Randomly find on the Internet. Good place to counting stars', rate_times = 0, total_point = 0, img_path='img/Top-7-places-with-a-beautiful-rooftop-in-Hanoi-1.jpg', type='cafe', rating = 0)
p9 = Place(name='Tran Duy Hung Street', description='No need any more descriptions, its name say everything', rate_times = 0, total_point = 0, img_path='img/lo-anh-meo-pho-dung-tran-duy-hung-vay-khach-hoa-ra-choi-thach-th-950c10.jpg', type='street', rating = 0)

places = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
for p in places:
	session.add(p)
session.commit()

print("All done")
