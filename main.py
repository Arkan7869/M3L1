from flask import Flask
import random 

app = Flask(__name__)

tech_fact = ['Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten','Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan','Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja']
ALAMAT = ['6666' ,'7654' ,'9879' ,'3672', '5490' ,'4444']

@app.route("/")
def hello_world():
    return '<h1>Hello, World! <a href="/tech_fact">View interesting facts</a></h1>    <a href="/ALAMAT">View generator password</a></h1>'
@app.route("/tech_fact")
def techfact():
    return f'<p>{random.choice(tech_fact)}</p>'



@app.route("/ALAMAT")
def alamat():
    return f'<p>{random.choice(ALAMAT)}</p>'

app.run(debug=True)
