import concurrent.futures
import time
from PIL import Image, ImageFilter
import multiprocessing
import concurrent

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    # 'photo-1513938709626-033611b8cc03.jpg',
    # 'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    # 'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()

size = (1200, 1200)

# 1. Basic Method
for img_name in img_names:
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size=size)
    img.save(f'Processed/{img_name}')


# # 2. Using Multiprocessing
# def process_img(img_name):
#     img = Image.open(img_name)
#     img = img.filter(ImageFilter.GaussianBlur(15))
#     img.thumbnail(size=size)
#     img.save(f'Processed/{img_name}')
#     return f'{img_name} has been processed sucessfully'

# processPool = [multiprocessing.Process(target=process_img, args=[img_name]) for img_name in img_names]

# processes = []

# for process in processPool:
#     process.start()
#     processes.append(process)

# for process in processPool:
#     process.join()

# # 3. Using Multiprocessing with concurrent.futures module and context window via with
# def process_img(img_name):
#     img = Image.open(img_name)
#     img = img.filter(ImageFilter.GaussianBlur(15))
#     img.thumbnail(size=size)
#     img.save(f'Processed/{img_name}')
#     return f'{img_name} has been processed sucessfully'

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = [executor.submit(process_img, img_name) for img_name in img_names]
    
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# # 4. Using Multiprocessing with concurrent.futures module via map function
# def process_img(img_name):
#     img = Image.open(img_name)
#     img = img.filter(ImageFilter.GaussianBlur(15))
#     img.thumbnail(size=size)
#     img.save(f'Processed/{img_name}')
#     return f'{img_name} has been processed sucessfully'

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = executor.map(process_img, img_names)
    
#     for res in results:
#         print(res)

t2 = time.perf_counter()
print(f"Finised in {round(t2 - t1,2)} sec...")
