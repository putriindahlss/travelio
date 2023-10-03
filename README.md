<h1>Link Adaptable</h1>

https://travelio.adaptable.app/
Putri Indah Lestari
2206814412 
PBP E

<details>
<summary>Tugas 2</summary>
Implementasi Model-View-Template (MVT) pada Django
    
<h1>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)</h1>

Langkah 1: Membuat direktori dengan nama travelio di git dan menambahkan dependencies. Setelah itu saya membuat proyek Django dengan nama travelio dengan perintah django-admin startproject travelio .

Langkah 2: Membuat aplikasi main di proyek Django. Setelah menjalankan perintah di langkah 1, terbentuk direktori main. Lalu, jalankan python manage.py startapp main dan tambahkan 'main' ke list INSTALLED_APPS di settings.py (berdasarkan tutorial).
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'main', 
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Langkah 3: Routing di proyek dengan membuat berkas urls.py di direktori main.
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```

Setelah itu, buka urls.py di direktori travelio. Import fungsi include from django.url agar adaptable bisa diakses.
```python
from django.contrib import admin
from django.urls import path
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

Langkah 4: Membuat model di aplikasi main dan mengisi dengan atribut name, amount, dan description, lalu migrasi model.
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()

```

Langkah 5: Mengimpor fungsi render di views.py dan menambahkan fungsi untuk dikembalikan ke template HTML.
```python
def show_main(request):
    context = {
        'name': 'Putri Indah Lestari',
        'class' : 'PBP E'
    }

    return render(request, "main.html", context)
```

Langkah 6: Melakukan git add commpit push di repositori travelio. Lalu, melakukan deployment aplikasi pada adaptable.

<h1>Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</h1>

<h2>Bagan di bawah berisi request client ke web aplikasi berbasis Django. Panah yang mulai dari client menunjukan request client. Panah yang menuju client menunjukkan response.</h2>

[![Add-a-little-bit-of-body-text.png](https://i.postimg.cc/YqH85Q6T/Add-a-little-bit-of-body-text.png)](https://postimg.cc/jCMzNwkh)

<h1>Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</h1>

Virtual environment adalah lingkungan isolasi dalam pengembangan softwase (web Django) yang tujuannya untuk:
- Isolasi dependensi: Venv memungkinkan mengelola dependensi proyek secara terpisah. Hal ini penting ketika kita bekerja pada proyek yang rawan terjadi konflik. 
- Keamanan: Venc dapat menghindari perubahan atau penyusupan berkas diluar kendali.
- Kontrol versi: Kita dapat membuat daftar dependensi proyek dan mengontrol versi yang digunakan untuk mereproduksi lingkungan pengembangan, uji, dan produksi.

Kita juga bisa membuat website berbasis Django tanpa venv, namun tidak dianjurkan karena tidak memiliki kelebihan-kelebihan di atas dan membuat pengerjaan menjadi lebih rumit. Maka dari itu, kita dianjurkan menggunakan venv dalam proyek pengembangan Django.

<h1>Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.</h1>
MVC (Model View Controller), MVT (Model View Template), MVVM (Model View ViewModel) merupakan design arsitektur dalam pengembangan software. Berikut ini adalah penjelasan mengenai masing-masing pola dan perbedaannya:
1. Model View Controller (MVC)
- Model: Mengelola data aplikasi dan menjalankan logika bisnis.
- View: Menampilkan data dan informasi model ke pengguna 
- Controller: Menghubungkan dan mengontrol model dan view, mengatur alur aplikasi, dan menerima masukan pengguna.

2. Model View Template (MVT)
- Model: Mengelola data dan dan menjalankan logika bisnis.
- View: Menampilkan data ke pengguna.
- Template: Mengatur cara data yang ditampilkan dalam view. Berisi HTML yang bisa disisipkan data dari model.

3. Model View ViewModel (MVVM)
- Model: Mengelola data dan dan menjalankan logika bisnis.
- View: Menampilkan data ke pengguna.
- ViewModel: Perantara model dan view, mengubah data dari model jadi format yang bisa ditampilkan oleh view, menangani tindakan pengguna yang diteruskan ke model.

Perbedaan ketiganya adalah cara mengatur interaksi antara model, view, dan pengontrol. Di mana MVC merupakan pola yang sudah digunakan dalam berbagai kerangka kerja web, MVT adalah variasi Django dengan template untuk tampilan, sedangkan MVVM digunakan dalam pengembangan aplikasi desktop dan aplikasi berbasis interface yang kompleks.
</details>

<details>
<summary>Tugas 3</summary>
Implementasi Form dan Data Delivery pada Django
    
<h1>Apa perbedaan antara form POST dan form GET dalam Django?</h1>

- Form POST: Mengirim data melalui permintaan HTTP POST dengan mengirimkan formulir pendaftaran atau mengirim data yang akan disimpan ke server kemudian menerima kembali responsnya. Data yang dikirim melalui POST cenderung lebih aman karena tidak terlihat dalam URL (cocok untuk data sensitif, seperti password). 
POST tidak memiliki batasan ukuran data yang ketat, sehingga lebih cocok untuk mengirim data yang besar. 
- Form GET: Mengirim data melalui URL, yang terlihat dalam tautan dan biasanya digunakan untuk mengirim data yang tidak sensitif. 
GET memiliki batasan ukuran data yang lebih kecil, tergantung pada server dan browser. GET lebih tidak aman karena data dapat terlihat oleh siapa saja yang melihat URL dan dapat dibagikan sebagai tautan.

<h1>Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?</h1>

Dalam konteks pengiriman data, berikut adalah perbedaan utama dari XML, JSON, dan HTML:
- XML (eXtensible Markup Language): XML adalah format teks yang digunakan untuk menyusun dan mengirim data dalam struktur hierarkis/pohon. Biasanya digunakan untuk menyimpan dan berbagi data antar aplikasi, seperti web service dan pembuatan dokumen. XML bisa digunakan dalam C++, Java, atau Python. Kesimpulannya, XML fokus pada struktur data.

- JSON (JavaScript Object Notation): JSON adalah format teks yang mudah dibaca manusia maupun mesin yang digunakan untuk pertukaran data. JSON memiliki struktur data yang mirip objek JavaScript dan sering digunakan dalam pengembangan web dan API. Kesimpulannya, JSON fokus mentransfer data dengan struktur yang mudah dibaca.

- HTML (HyperText Markup Language): HTML adalah bahasa markup untuk membuat aplikasi dan halaman web. HTML digunakan untuk menampilkan data, mengubah teks menjadi gambar, dan bagaimana dokumen diakses di browser. Tetapi, HTML tidak dirancang untuk pertukaran data melalui jaringan seperti XML atau JSON. Kesimpulannya, HTML fokus bagaimana penyajian data.

<h1>Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?</h1>

JSON sering digunakan dalam pertukaran daya antara aplikasi dan web modern karena sifatnya yang:

- Ringan: JSON adalah format teks yang ringan, mudah dibaca, mudah dikirim, dan efisien untuk aplikasi web.

- Mudah Dibaca: JSON mudah dibaca oleh bahasa manusia dan komputer, sehingga mudah untuk dipahami dan dimanipulasi datanya.

- Bahasa Agnostik: JSON dapat digunakan dengan berbagai bahasa pemrograman. Hal ini berguna dalam pertukaran data antar platform.

- Struktur Data Sederhana: JSON memiliki struktur data yang sederhana dan mudah dipahami, tidak seperti format lainnya.

- Fleksibilitas dalam Representasi Data: JSON memungkinkan representasi fleksibel dari berbagai jenis data seperti tipe data string dan integer, serta struktur yang lebih kompleks seperti objek dan array.

<h1> Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h1>

a. Buat Input Form untuk Menambahkan Objek pada App Sebelumnya
- Langkah pertama membuat berkas baru di direktori main (forms.py) yang berisi:
```python
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "description"]
```
- Modifikasi (views.py) dengan mengimport modul dan fungsi create_product
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)
```
- Mengubah fungsi show_main
- Menambahkan path di bawah ke urlpattern
```python
path('create-product', create_product, name='create_product'),
```
- Membuat berkas HTML (create_product.html) di direktori main/templates yang berisi:
```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```
b. Menambahkan 5 Fungsi Views (melihat objek yang sudah ditambahkan).
- Dengan format HTML, XML, JSON, XML by ID, dan JSON by ID.
- Import
```python
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
```
- Buat fungsi create_product untuk menampilkan data produk di HTML.
- Megubah fungsi show_main pada berkas views.py
```python
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Putri Indah Lestari', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)
```
- Menambah fungsi show_xml dan show_json untuk mengembalikan data dalam bentuk XML dan JSON
```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Menambah fungsi show_xml_by_id dan show_json_by_id
```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
c. Membuat Routing URL Tiap Views 
- Import fungsi ke urls.py di folder main yang sudah dibuat di atas
```python
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
```
- Tambahkan path ke urlpatterns untuk akses fungsi yang sudah diimpor.

d. Mengakses URL dengan Postman
- Send request dengan method get di Postman pakai:
- http://localhost:8000
  [![Screenshot-2023-09-18-141442.png](https://i.postimg.cc/rmt7HcC7/Screenshot-2023-09-18-141442.png)](https://postimg.cc/mzBdcvnS)

  [![Screenshot-2023-09-20-091821.png](https://i.postimg.cc/HWZ6kSw2/Screenshot-2023-09-20-091821.png)](https://postimg.cc/qgKsmxZh)

  [![Screenshot-2023-09-20-091833.png](https://i.postimg.cc/5NQSNfN4/Screenshot-2023-09-20-091833.png)](https://postimg.cc/3d7vt5vV)

  [![Screenshot-2023-09-20-091847.png](https://i.postimg.cc/VNgjH64R/Screenshot-2023-09-20-091847.png)](https://postimg.cc/mcczPTvz)

  [![Screenshot-2023-09-20-091856.png](https://i.postimg.cc/Y9S1cHsw/Screenshot-2023-09-20-091856.png)](https://postimg.cc/WDQDrQV9)
  
- http://localhost:8000/xml
  [![Screenshot-2023-09-18-141548.png](https://i.postimg.cc/1tpJ6zKR/Screenshot-2023-09-18-141548.png)](https://postimg.cc/WF1GcTKx)
  
- http://localhost:8000/xml/1
  [![Screenshot-2023-09-18-141717.png](https://i.postimg.cc/LXdxnPL0/Screenshot-2023-09-18-141717.png)](https://postimg.cc/CZNG2zvj)
  
- http://localhost:8000/json
  [![Screenshot-2023-09-18-141744.png](https://i.postimg.cc/WbsfG0KB/Screenshot-2023-09-18-141744.png)](https://postimg.cc/Wtfnjqs8)
  
- http://localhost:8000/json/1
  [![Screenshot-2023-09-18-141803.png](https://i.postimg.cc/jS5g9tRv/Screenshot-2023-09-18-141803.png)](https://postimg.cc/3dsF0M4D)

e. BONUS
- Menambahkan kode di bawah pada main.html
  [![Screenshot-2023-09-19-141818.png](https://i.postimg.cc/kXPKBtwL/Screenshot-2023-09-19-141818.png)](https://postimg.cc/SjVJPRBG)
  
```html
<h2>{{ products.count }} saved item(s) in this app</h2>
```
</details>

<details>
<summary>Tugas 4</summary>
Implementasi Autentikasi, Session, dan Cookies pada Django

<h1>Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?</h1>

Django UserCreationForm merupakan formulir bawaan Django untuk mempermudah pembuatan akun pengguna dalam aplikasi web dengan Django. Berikut kelebihan dan kekurangannya:
a. Kelebihan
- Tidak rumit dalam proses pendaftarannya karena mudah digunakan
- Memiliki validasi bawaan untuk memastikan data pengguna sesuai dengan persyaratan yang ditentukan.
- Form berintegrasi langsung dengan sistem otentikasi sehingga pengguna yang terdaftar mudah mengakses web.

b. Kekurangan
- Kurang fleksibel ketika menyesuaikan atribut tambahan pada model pengguna.
- Tampilan interface harus disesuaikan supaya lebih menarik.

<h1>Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?</h1>

Autentikasi dan Otorisasi penting karena keduanya membantu melindungi keamanan dan integritas webyang kita buat. Autentikasi dapat memastikan hanya pengguna terdaftar yang dapat mengakses web, sedangkan Otorisasi akan mengontrol atau membatasi akses ke bagian sensitif web.

Perbedaannya adalah:
a. Autentikasi: Proses verifikasi identitas pengguna dengan memeriksa nama pengguna dan kata sandi yang dimasukkan. Lalu sistem akan memastikan hanya pengguna terdaftar yang dapat login atau mengakses web.

b. Otorisasi: Proses yang menentukan apa yang diizinkan atau dilarang bagi pengguna yang telah terautentikasi. Hal ini dilakukan untuk membatasi akses ke bagian sensitif web.

<h1>Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?</h1>

Cookies adalah sepotong data kecil yang dikirim server ke browser web pengguna lalu browser akan menyimpan cookie tersebut dan mengirimkannya kembali ke server yang sama dengan permintaan selanjutnya.

Django menggunakan cookies untuk menyimpan dan mengelola data sesi pengguna, seperti preferensi atau status login. Data ini akan disimpan di server dan diidentifikasi oleh ID sesi di dalam cookie. Jadi, setiap pengguna berhasil login, Django akan membuat cookie sesi unik untuk pengguna tersebut. Cookie ini berisi ID sesi yang digunakan oleh Django untuk mengidentifikasi pengguna.

<h1>Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?</h1>

Secara default pengembangan web, penggunaan cookies aman dan sangat bermanfaat jika dikelola dengan baik. Namun, kita juga harus waspada karena cookies berpotensi melacak perilaku pengguna dan mengumpulkan informasi pribadi, data login, dan riwayat pencarian. Kalau webnya rentan, penyerang akan memanipulasi dan mengambil alih sesi pengguna. Hal ini akan mengancam keamanan data dan informasi pengguna.

Untuk itu, kita dapat meminimalisir risiko dengan menggunakan HTTPS untuk melindungi cookie dari peretas, menerapkan kebijakan privasi agar pengguna paham bagaimana data mereka digunakan, dan menghapus cookies yang tidak diperlukan secara teratur. 

<h1>Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</h1>
Langkah 1: Implementasi fungsi registrasi, login, dan logout dengan menambahkan import di views.py dalam direktori main.
```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
```

lalu membuat fungsi register dengan parameter request.
```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

kemudian membuat register.html di main/templates seperti ini.
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "login">
    
    <h1>Register</h1>  

        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

lalu import fungsi register ke urls.py dan menambahkan path url ke urlpatterns.
```python
from main.views import register
```
```python
path('register/', register, name='register'),
```

Langkah 2: Implementasi fungsi login_user di views.py (import authenticate terlebih dahulu)
```python
from django.contrib.auth import authenticate, login
```

```python
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

kemudian membuat login.html di main/templates
```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

jangan lupa import login_user dan tambahkan urlpatterns
```python
from main.views import login_user
```
```python
path('login/', login_user, name='login'),
```

Langkah 3: Implementasi fungsi logout di views.py, diawali dengan membuat fungsi logout_user dengan parameter request dan import juga.
```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

```python
from django.contrib.auth import logout
```

lalu menambahkan button logout di main.html
```html
<a href="{% url 'main:logout' %}">
        <button>
            Logout
        </button>
    </a>
```

tahap terakhir, buka urls.py dan import fungsi logout_user di atas dan menambahkan path di urlpatterns
```python
from main.views import logout_user
```
```python
path('logout/', logout_user, name='logout'),
```

Langkah 4: Buat 2 akun dengan 3 dummy data
- Menjalankan python manage.py runserver pada direktori lokal. 
- Buka http://localhost:8000/, lalu register dengan username vina_voli dan rifda. 
- Setelah akun berhasil dibuat, login pada masing-masing akun, lalu saya menambahkan tiga dummy data dengan klik tombol Add New Product.

Langkah 5: Menghubungkan model item dengan user. Pertama membuka models.py di main dan import user.
```python
from django.contrib.auth.models import User
```

lalu menambahkan model product 
```python
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

kemudian mengubah bagian if pada fungsi create_product di views.py
```python
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
```

lalu mengubah variabel product di show_main agar produk yang ditampilkan sesuai dengan pengguna yang sedang login
```python
def show_main(request):
    products = Product.objects.filter(user=request.user)
```

lalu jalankan python manage.py makemigration dan python manage.py migrate karena saya memodifikasi model.

Langkah 6: Menampilkan detail pengguna yang log in dengan mengganti value name pada fungsi show_main di views.py menjadi
```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,

    }
```

lalu, menerapkan cookies untuk data last login di halaman main dengan cara mengimpor di views.py
```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

saya juga menambahkan cookie last_login untuk melihat terakhir kali login pengguna
```python
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

tambahkan juga pada fungsi logout_user dan fungsi show_main
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

```python
def show_main(request):
    products = Product.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'class': 'PBP E', # Kelas PBP kamu
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

```

jangan lupa menambah baris kode berikut di main.html untuk melihat data last login
```html
<h5>Sesi terakhir login: {{ last_login }}</h5>
```

<h1>BONUS</h1>
Implementasi bonus dengan membuat tiga fungsi berikut di views.py

```python
def add_amount(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.amount >= 0:
        product.amount += 1
        product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrement_amount(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.amount > 0:
        product.amount -= 1
        product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user == request.user:
        product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))
```

lalu tambahkan pathnya juga di urls.py.
```python
path('increment-amount/<int:id>/', add_amount, name='increment_amount'),
path('decrement-amount/<int:id>/', decrement_amount, name='decrement_amount'),
path('delete-product/<int:id>/', delete_product, name='delete_product'),
```

dan jangan lupa impor add_amount, decrement_amount, delete_product.

<h2>Tampilannya sebagai berikut</h2>
[![Screenshot-2023-09-26-155136.png](https://i.postimg.cc/4dcmsbZN/Screenshot-2023-09-26-155136.png)](https://postimg.cc/1n99KFfL)

</details>

<details>
<summary>Tugas 5</summary>
Desain Web menggunakan HTML, CSS dan Framework CSS

<h1>Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.</h1>
Element selector memilih elemen HTML berdasarkan nama tag yang sebaiknya digunakan ketika kita ingin menerapkan gaya yang konsisten dan seragam untuk elemen yang sama di seluruh halaman web. 
Contohnya, selector p akan memilih semua elemen <p> di dokumen. 

Element selector berguna untuk mengatur gaya umum untuk elemen tertentu, seperti ukuran font, margin, warna font, padding, dll. 

<h1>Jelaskan HTML5 Tag yang kamu ketahui.</h1>
HTML Tag merupakan emelen dasar yang berisi instruksi ke browser bagaimana menampilkan konten dalam pembuatan halaman web. HTML5 merupakan versi terbaru dan lebih lengkap dari HTML untuk mengembangkan halaman web yang lebih modern. Beberapa di antaranya:
1. '<nav>' : Untuk mengelompokkan tautan navigasi.
2. '<video>': Untuk menampilkan dan memutar video di halaman web.
3. '<time>':  Untuk menunjukkan tanggal atau waktu dalam format tertentu.
4. '<details>' dan '<summary>': Untuk membuat konten yang dapat dibuka dan ditutup, seperti yang saya gunakan pada tugas ini.
5. '<audio>' : Untuk menampilkan dan memutar audio di halaman web.
6. '<canvas>' : Menentukan area grafis yang dapat digambar dengan menggunakan skrip (biasanya JavaScript), seperti membuat grafik, animasi, game, dll.
7. '<figure>' : Menentukan konten mandiri yang biasanya memiliki keterangan, seperti gambar, diagram, kutipan, dll.
8. '<article>' : Menentukan konten mandiri yang dapat berdiri sendiri atau didistribusikan secara terpisah, seperti artikel blog, berita, komentar, dll.

<h1>Jelaskan perbedaan antara margin dan padding.</h1>
Margin dan Padding merupakan konsep dalam CSS untuk mengatur tata letak dan tampilan pada elemen html di web. Secara garis besar, margin mengatur ruang di luar batas elemen (border), sementara padding mengatur ruang di dalam batas elemen (border):

a. MARGIN
- Untuk mengatur jarak antar elemen di sekitarnya/ diluar kontainer yang mengelilinginya, contoh: mengatur jarak antara satu kotak dengan kotak lain.
- Tidak memiliki background color.

b. PADDING
- Untuk mengatur jarak antar elemen dalam kontainer/border yang mengelilinginya, contoh: mengatur jarak antara isi sebuah kotak dengan batas kotak itu sendiri.
- Bisa memiliki background color.

<h1>Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?</h1>
Berikut adalah perbedaan antara framework CSS Tailwind dan Bootstrap:

a. CSS Tailwind
- Framework yang menyediakan kelas utilitas yang dapat diterapkan langsung pada elemen HTML untuk mengatur tampilan elemen dengan menggabungkan kelas-kelas untuk membuat sesuai kebutuhan.
- Sangat fleksibel, tapi untuk customize tampilan yang detail perlu menuliskan banyak kelas.
- Memiliki kode yang lebih ringan kalau kita hanya menggunakan kelas yang diperlukan sehingga ukurannya kecil dan waktu untuk memuatnya lebih cepat.

b. Bootstrap
- Komponen UI sudah dirancang, tinggal menggabungkan komponen Bootstrap langsung tanpa menulis kode CSS tambahan.
- Lebih cocok dalam pembuatan proyek dengan design yang berbeda.
- Memiliki lebih banyak kode CSS sehingga perlu ukuran yang besar dan waktu yang lama.

Sebaiknya kita menggunakan Tailwind saat ingin customize desain yang unik dan mendetail, ingin menghindari default style dari Bootstrap, ini juga digunakan kalau kita mengerti tentang CSS dengan baik.
Penggunaan Bootstrap sebaiknya digunakan ketika ingin desain yang siap pakai dan cepat, tidak keberatan menggunakan style default Bootstap. Biasanya digunakan ketika kita tidak memiliki pengetahuan dan pengalaman terkait desain UI.

<h1>Implementasi Checklist</h1>

<h1>BONUS</h1>

</details>

