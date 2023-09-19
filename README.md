1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Langkah 1: Membuat direktori dengan nama travelio di git dan menambahkan dependencies. Setelah itu saya membuat proyek Django dengan nama travelio dengan perintah django-admin startproject travelio .

Langkah 2: Membuat aplikasi main di proyek Django. Setelah menjalankan perintah di langkah 1, terbentuk direktori main. Lalu, jalankan python manage.py startapp main dan tambahkan 'main' ke list INSTALLED_APPS di settings.py (berdasarkan tutorial).

Langkah 3: Routing di proyek dengan membuat berkas urls.py di direktori main. Setelah itu, buka urls.py di direktori travelio. Import fungsi include from django.url agar adaptable bisa diakses.

Langkah 4: Membuat model di aplikasi main dan mengisi dengan atribut name, amount, dan description.

Langkah 5: Mengimpor fungsi render dan menambahkan fungsi untuk dikembalikan ke template HTML.

Langkah 6: Melakukan git add commpit push di repositori travelio. Lalu, melakukan deployment aplikasi pada adaptable.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
[![Add-a-little-bit-of-body-text.png](https://i.postimg.cc/YqH85Q6T/Add-a-little-bit-of-body-text.png)](https://postimg.cc/jCMzNwkh)

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Virtualk environment adalah lingkungan isolasi dalam pengembangan softwase (web Django) yang tujuannya untuk:
- Isolasi dependensi: Venv memungkinkan mengelola dependensi proyek secara terpisah. Hal ini penting ketika kita bekerja pada proyek yang rawan terjadi konflik. 
- Keamanan: Venc dapat menghindari perubahan atau penyusupan berkas diluar kendali.
- Kontrol versi: Kita dapat membuat daftar dependensi proyek dan mengontrol versi yang digunakan untuk mereproduksi lingkungan pengembangan, uji, dan produksi.

Kita juga bisa membuat website berbasis Django tanpa venv, namun tidak dianjurkan karena tidak memiliki kelebihan-kelebihan di atas dan membuat pengerjaan menjadi lebih rumit. Maka dari itu, kita dianjurkan menggunakan venv dalam proyek pengembangan Django.


4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
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

Tugas 3
1. Apa perbedaan antara form POST dan form GET dalam Django?
- Form POST: Mengirim data melalui permintaan HTTP POST dengan mengirimkan formulir pendaftaran atau mengirim data yang akan disimpan ke server kemudian menerima kembali responsnya. Data yang dikirim melalui POST cenderung lebih aman karena tidak terlihat dalam URL (cocok untuk data sensitif, seperti password). 
POST tidak memiliki batasan ukuran data yang ketat, sehingga lebih cocok untuk mengirim data yang besar. 
- Form GET: Mengirim data melalui URL, yang terlihat dalam tautan dan biasanya digunakan untuk mengirim data yang tidak sensitif. 
GET memiliki batasan ukuran data yang lebih kecil, tergantung pada server dan browser. GET lebih tidak aman karena data dapat terlihat oleh siapa saja yang melihat URL dan dapat dibagikan sebagai tautan.

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
Dalam konteks pengiriman data, berikut adalah perbedaan utama dari XML, JSON, dan HTML:
- XML (eXtensible Markup Language): XML adalah format teks yang digunakan untuk menyusun dan mengirim data dalam struktur hierarkis/pohon. Biasanya digunakan untuk menyimpan dan berbagi data antar aplikasi, seperti web service dan pembuatan dokumen. XML bisa digunakan dalam C++, Java, atau Python. Kesimpulannya, XML fokus pada struktur data.

- JSON (JavaScript Object Notation): JSON adalah format teks yang mudah dibaca manusia maupun mesin yang digunakan untuk pertukaran data. JSON memiliki struktur data yang mirip objek JavaScript dan sering digunakan dalam pengembangan web dan API. Kesimpulannya, JSON fokus mentransfer data dengan struktur yang mudah dibaca.

- HTML (HyperText Markup Language): HTML adalah bahasa markup untuk membuat aplikasi dan halaman web. HTML digunakan untuk menampilkan data, mengubah teks menjadi gambar, dan bagaimana dokumen diakses di browser. Tetapi, HTML tidak dirancang untuk pertukaran data melalui jaringan seperti XML atau JSON. Kesimpulannya, HTML fokus bagaimana penyajian data.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
JSON sering digunakan dalam pertukaran daya antara aplikasi dan web modern karena sifatnya yang:

- Ringan: JSON adalah format teks yang ringan, mudah dibaca, mudah dikirim, dan efisien untuk aplikasi web.

- Mudah Dibaca: JSON mudah dibaca oleh bahasa manusia dan komputer, sehingga mudah untuk dipahami dan dimanipulasi datanya.

- Bahasa Agnostik: JSON dapat digunakan dengan berbagai bahasa pemrograman. Hal ini berguna dalam pertukaran data antar platform.

- Struktur Data Sederhana: JSON memiliki struktur data yang sederhana dan mudah dipahami, tidak seperti format lainnya.

- Fleksibilitas dalam Representasi Data: JSON memungkinkan representasi fleksibel dari berbagai jenis data, seperti tipe data string dan integer, serta struktur yang lebih kompleks seperti objek dan array.

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Buat Input Form untuk Menambahkan Objek pada App Sebelumnya
- Langkah pertama membuat berkas baru di direktori main (forms.py) yang berisi:
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "amount", "description"]

- Modifikasi (views.py) dengan mengimport modul dan fungsi create_product.
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

- Mengubah fungsi show_main
- Menambahkan path di bawah ke urlpattern
path('create-product', create_product, name='create_product'),
- Membuat berkas HTML (create_product.html) di direktori main/templates yang berisi:
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

b. Menambahkan 5 Fungsi Views (melihat objek yang sudah ditambahkan).
- Dengan format HTML, XML, JSON, XML by ID, dan JSON by ID.
- Import 
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
- Buat fungsi create_product untuk menampilkan data produk di HTML.
- Megubah fungsi show_main pada berkas views.py
def show_main(request):
    products = Product.objects.all()

    context = {
        'name': 'Putri Indah Lestari', # Nama kamu
        'class': 'PBP E', # Kelas PBP kamu
        'products': products
    }

    return render(request, "main.html", context)
- Menambah fungsi show_xml dan show_json untuk mengembalikan data dalam bentuk XML dan JSON
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
- Menambah fungsi show_xml_by_id dan show_json_by_id
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

c. Membuat Routing URL Tiap Views 
- Import fungsi ke urls.py di folder main yang sudah dibuat di atas 
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
- Tambahkan path ke urlpatterns untuk akses fungsi yang sudah diimpor.

d. Mengakses URL dengan Postman
- Send request dengan method get di Postman pakai"
- http://localhost:8000
- http://localhost:8000/xml
- http://localhost:8000/xml/1
- http://localhost:8000/json 
- http://localhost:8000/json/1

e. BONUS
- Menambahkan kode di bawah pada main.html
<h2>{{ products.count }} saved item(s) in this app</h2>
