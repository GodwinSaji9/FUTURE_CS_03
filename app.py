from flask import Flask, render_template, request, send_file
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# -------------------- PATH SETUP --------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ENCRYPTED_FOLDER = os.path.join(BASE_DIR, "encrypted_files")
DECRYPTED_FOLDER = os.path.join(BASE_DIR, "decrypted_files")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

# -------------------- APP SETUP --------------------
app = Flask(__name__)

# -------------------- AES KEY --------------------
# For internship demo purposes (document this in README)
AES_KEY = get_random_bytes(32)  # 256-bit AES key

# -------------------- ENCRYPTION --------------------
def encrypt_file(input_path, output_path):
    with open(input_path, "rb") as f:
        data = f.read()

    cipher = AES.new(AES_KEY, AES.MODE_CBC)
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))

    with open(output_path, "wb") as f:
        f.write(cipher.iv + encrypted_data)

# -------------------- DECRYPTION --------------------
def decrypt_file(input_path, output_path):
    with open(input_path, "rb") as f:
        data = f.read()

    iv = data[:16]
    encrypted_data = data[16:]

    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    with open(output_path, "wb") as f:
        f.write(decrypted_data)

# -------------------- ROUTES --------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    file = request.files["file"]
    filename = file.filename

    temp_path = os.path.join(UPLOAD_FOLDER, filename)
    encrypted_path = os.path.join(ENCRYPTED_FOLDER, filename + ".enc")

    file.save(temp_path)
    encrypt_file(temp_path, encrypted_path)
    os.remove(temp_path)

    return render_template("index.html", uploaded_file=filename)

    return "File uploaded and encrypted successfully"

@app.route("/download/<filename>")
def download_file(filename):
    encrypted_path = os.path.join(ENCRYPTED_FOLDER, filename + ".enc")
    decrypted_path = os.path.join(DECRYPTED_FOLDER, filename)

    if not os.path.exists(encrypted_path):
        return "Encrypted file not found", 404

    decrypt_file(encrypted_path, decrypted_path)
    return send_file(decrypted_path, as_attachment=True)

# -------------------- RUN --------------------
if __name__ == "__main__":
    app.run(debug=True)

