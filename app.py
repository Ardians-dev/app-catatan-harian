from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = 'apaaja123'

catatan = []
catatan_id = 0


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/catatan', methods=['GET', 'POST'])
def daftar_catatan():    
    return render_template('catatan.html', catatan=catatan)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    global catatan_id
    if request.method == 'POST':
        judul = request.form['judul']
        isi_catatan = request.form['isi_catatan']
        if not judul or not isi_catatan:
            flash('form tidak boleh kosong', 'error')
            redirect('/tambah')
        catatan.append({'id': catatan_id, 'judul': judul, 'isi_catatan': isi_catatan})
        catatan_id += 1
        flash('catatan berhasil ditambahkan', 'success')
        return redirect('/catatan')
    return render_template('tambah.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    catat = next((n for n in catatan if n['id'] == id), None)
    if catat is None:
        flash('gagal cuy', 'error')
        redirect('/catatan')
    if request.method == 'POST':
        catat['judul'] = request.form['judul']
        catat['isi_catatan'] = request.form['isi_catatan']
        flash('catatan berhasil diubah', 'success')
        redirect('/catatan')
    return render_template('edit.html', catat=catat)

@app.route('/delete/<int:id>')
def delete(id):
    global catatan
    catatan = [n for n in catatan if n['id'] != id]
    flash('catatan berhasil dihapus', 'success')
    return redirect('/catatan')

if __name__ == '__main__':
    app.run(debug=True)