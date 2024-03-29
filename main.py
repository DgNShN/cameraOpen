import tkinter as tk

# Engellenen numaraları ve mesajları saklamak için dosyalar
blocked_numbers_file = "blocked_numbers.txt"
blocked_messages_file = "blocked_messages.txt"

# Mesajları engellemek için kütüphane
from sms import SMS

def block_message(number):
  """
  Bir telefon numarasından gelen mesajları engeller.
  """

  # Mesaj engelleme listesine ekleyin
  with open(blocked_messages_file, "a") as f:
    f.write(number + "\n")

  # Mesajı engelleyin
  sms.block(number)

def is_number_blocked(number):
  """
  Bir telefon numarasının engellenip engellenmediğini kontrol eder.
  """
  with open(blocked_numbers_file, "r") as f:
    for line in f:
      if number == line.strip():
        return True
  return False

def is_message_blocked(number):
  """
  Bir telefon numarasından gelen mesajların engellenip engellenmediğini kontrol eder.
  """
  with open(blocked_messages_file, "r") as f:
    for line in f:
      if number == line.strip():
        return True
  return False

def block_number(number):
  """
  Bir telefon numarasını engeller.
  """

  # Engellenen numaralar listesine ekleyin
  with open(blocked_numbers_file, "a") as f:
    f.write(number + "\n")

  # Mesaj engelleme listesine ekleyin
  with open(blocked_messages_file, "a") as f:
    f.write(number + "\n")

  # Engellenen numaralardan gelen aramaları engelleyin
  # (Bu kod işletim sistemine bağlıdır)

  # Mesajı engelleyin
  sms.block(number)

def show_blocked():
  """
  Engellenen numaraları ve mesajları gösterir.
  """

  # Engellenen numaraları ve mesajları listede gösterin
  blocked_list.delete(0, tk.END)

  with open(blocked_numbers_file, "r") as f:
    for line in f:
      blocked_list.insert(tk.END, line.strip())

  with open(blocked_messages_file, "r") as f:
    for line in f:
      blocked_list.insert(tk.END, line.strip())

def on_select(index):
  """
  Listedeki bir öğeye tıklandığında çağrılır.
  """

  # Seçilen öğenin indeksini alın
  # Seçilen öğeyi silin
  blocked_list.delete(index)

  # Seçilen öğeyi dosyalardan silin
  # (Bu kod işletim sistemine bağlıdır)

def main():

  # Pencereyi oluşturun
  window = tk.Tk()

  # Pencereyi boyutlandırın ve widget'ları yerleştirin
  window.geometry("400x300")

  # Numara engelleme için metin giriş alanı ve buton
  number_entry = tk.Entry(window)
  block_number_button = tk.Button(window, text="Numarayı Engelle", command=block_number)

  # Mesaj engelleme için metin giriş alanı ve buton
  message_entry = tk.Entry(window)
  block_message_button = tk.Button(window, text="Mesajı Engelle", command=block_message)

  # Engellenen numaraları ve mesajları göstermek için liste
  blocked_list = tk.Listbox(window)

  # Listeye tıklama olayı
  blocked_list.bind("<Double-Button-1>", on_select)

  # Widget'ları pencereye yerleştirin
  number_entry.pack()
  block_number_button.pack()
  message_entry.pack()
  block_message_button.pack()
  blocked_list.pack()

  # Pencereyi çalıştırın
  window.mainloop()

if __name__ == "__main__":
  main()
