import os, json, base64, getpass, hashlib
from cryptography.fernet import Fernet

MASTER_FILE = "master.key"
DATA_FILE = "passwords.enc"
KEY_FILE = "secret.key"

def load_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        open(KEY_FILE, "wb").write(key)
    return open(KEY_FILE, "rb").read()

def get_fernet():
    return Fernet(load_key())

def set_master():
    if not os.path.exists(MASTER_FILE):
        print("Set Master Password (First Time)")
        m = getpass.getpass("New Master Password: ")
        open(MASTER_FILE, "w").write(hashlib.sha256(m.encode()).hexdigest())
        print("[+] Master set\n")

def verify_master():
    if not os.path.exists(MASTER_FILE): return True
    m = getpass.getpass("Enter Master Password: ")
    saved = open(MASTER_FILE).read()
    if hashlib.sha256(m.encode()).hexdigest() == saved:
        return True
    print("[-] Wrong Master Password!"); return False

def load_data():
    if not os.path.exists(DATA_FILE): return {}
    try:
        f = get_fernet()
        dec = f.decrypt(open(DATA_FILE, "rb").read())
        return json.loads(dec)
    except: return {}

def save_data(data):
    f = get_fernet()
    enc = f.encrypt(json.dumps(data).encode())
    open(DATA_FILE, "wb").write(enc)

def add():
    d=load_data()
    site=input("Website/App: ").lower()
    user=input("Username: ")
    pwd=input("Password: ")
    d[site]={"username":user,"password":pwd}
    save_data(d); print("[+] Added")

def retrieve():
    d=load_data()
    q=input("Search site: ").lower()
    for site in d:
        if q in site:
            print(f"\nSite: {site} | User: {d[site]['username']} | Pass: {d[site]['password']}")

def view():
    d=load_data()
    if not d: print("No passwords"); return
    for s,v in d.items(): print(f"{s} -> {v['username']} : {v['password']}")

def delete():
    d=load_data()
    site=input("Delete site: ").lower()
    if site in d: del d[site]; save_data(d); print("Deleted")
    else: print("Not found")

def main():
    set_master()
    if not verify_master(): return
    while True:
        print("\n1.Add 2.Search/Retrieve 3.View All 4.Delete 5.Exit")
        ch=input("Choice: ")
        if ch=='1': add()
        elif ch=='2': retrieve()
        elif ch=='3': view()
        elif ch=='4': delete()
        elif ch=='5': break

if __name__=="__main__": main()