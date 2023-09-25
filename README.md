<h1>Link Adaptable</h1>

https://travelio.adaptable.app/
Putri Indah Lestari
2206814412 
PBP E

<details>
<summary>Tugas 2</summary>
    
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


<h1>BONUS</h1>

</details>
