
# coding: utf-8

# In[1]:


# NIM/Nama  : 16518110/Kendrik Emkel Ginting
# Tanggal   : 3 November 2018 (Updated 4 November 2018)
# Deskripsi : Pekerjaan Rumah H05 Problem 1

# Program Problem 1
# Spesifikasi: Menyelesaikan Problem 1

# Kamus
# df : dataframe database

# Algoritma
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stei-c-1.csv")


# In[2]:


# 1. Banyaknya data
print(len(df))
# 9641


# In[3]:


# 2. Pie chart banyaknya mahasiswa tiap kendaraan yang digunakan untuk berangkat ke kampus.
(df["kendaraan"].value_counts()).plot(kind = "pie", title ="Kendaraan ke Kampus")
plt.show()


# In[4]:


# 3. Pie chart banyaknya mahasiswa tiap tingkat yang berjalan kaki.
df2 = df.groupby(["tingkat","kendaraan"])["nama"].size().unstack()
df2["jalan kaki"].plot(kind = "pie", title = "Jalan Kaki tiap Angkatan")
plt.show()


# In[5]:


# 4. Histogram dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
(df["tingkat"]).plot(kind = "hist", bins=[2015, 2016, 2017, 2018, 2019], title = "Mahasiswa tiap Angkatan", rwidth = 0.8)
plt.show()


# In[6]:


# 5. Berdasar plot sebelumnya, angkatan berapa yang jumlah mahasiswanya paling banyak?

# Angkatan 2016


# In[7]:


# 6. Stacked bar chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa tiap kendaraan sebagai stacked sumbu y
df2.plot(kind="bar",stacked=True)
plt.show()


# In[8]:


# 7. Berdasar plot sebelumnya, sebutkan trend kendaraan transportasi tiap tingkat!

# Semakin baru angkatan, pengguna angkot dan pejalan kaki semakin banyak, sedangkan pengguna mobil dan motor semakin sedikit


# In[9]:


# 8. Line chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
(df["tingkat"].value_counts().sort_index()).plot(kind = "line", title = "Mahasiswa tiap Angkatan")
plt.show()


# In[10]:


# 9. Line chart seperti soal sebelumnya, namun terdapat 4 garis, masing-masing untuk tiap kendaraan
df2.plot(kind="line", y=["angkot", "jalan kaki", "motor", "mobil"], title = "Grafik Kendaraan")
plt.show()


# In[11]:


# 10. Berdasar plot sebelumnya, apa kendaraan yang penggemarnya terus bertambah?

# Kendaraan yang penggemarnya terus bertambah adalah Jalan Kaki dan angkot


# In[12]:


# 11. Berdasar plot sebelumnya, apa kendaraan yang penggemarnya terus menurun?

# Kendaraan yang penggemarnya terus menurun adalah mobil dan motor

