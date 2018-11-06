
# coding: utf-8

# In[1]:


# NIM/Nama  : 16518110/Kendrik Emkel Ginting
# Tanggal   : 4 November 2018
# Deskripsi : Pekerjaan Rumah H05 Problem 1

# Program Problem 1
# Spesifikasi: Menyelesaikan Problem 1

# Kamus
# df : dataframe database

# Algoritma
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stei-c-2.csv")


# In[2]:


# 1. Banyaknya data
print(len(df))
# 8848


# In[3]:


# 2. Pie chart banyaknya mahasiswa tiap fakultas.
(df["fakultas"].value_counts()).plot(kind = "pie", title ="Banyak Mahasiswa")
plt.show()


# In[4]:


# 3. Pie chart banyaknya mahasiswa FTSL berdasarkan tingkat
df2 = df[df["fakultas"] == "FTSL"]
df2["tingkat"].value_counts().plot(kind="Pie", title = "Mahasiswa FTSL")


# In[5]:


# 4. Histogram dengan IP sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y, gunakan pertambahan 0.5
df["ip"].value_counts().plot(kind = "hist", bins = [1, 1.5, 2, 2.5, 3, 3.5, 4],title = "IP Mahasiswa", rwidth = 0.8)
plt.show()


# In[6]:


# 5. Berdasar plot sebelumnya, range ip mana yang paling banyak diperoleh?

# Range IP yang paling banyak diperoleh adalah 1.0 - 1.5


# In[7]:


# 6. Stacked bar chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa tiap fakultas sebagai stacked sumbu y
df3 = df.groupby(["tingkat", "fakultas"])["nama"].size().unstack()
df3.plot(kind = "bar", y = ["FTMD", "FTSL", "SITHR", "STEI"], stacked = True)


# In[8]:


# 7. Berdasar plot sebelumnya, angkatan ke berapa STEI jumlah mahasiswanya paling sedikit?

# Angkatan STEI yang jumlah mahasiswanya paling sedikit adalah angkatan 2018


# In[9]:


# 8. Line chart dengan tingkat sebagai sumbu x dan jumlah mahasiswa sebagai sumbu y
(df["tingkat"].value_counts().sort_index()).plot(kind = "line", title = "Mahasiswa tiap Angkatan")
plt.show()


# In[10]:


# 9. Line chart seperti soal sebelumnya, namun terdapat 4 garis, masing-masing untuk tiap fakultas
df3.plot(kind="line", y=["FTSL", "FTMD", "SITHR", "STEI"], title = "Grafik Mahasiswa per Fakultas")
plt.show()


# In[11]:


# 10. Berdasar plot sebelumnya, fakultas manakah yang jumlah mahasiswanya terus bertambah?

# Fakultas yang jumlah mahasiswanya terus bertambah adalah SITHR


# In[12]:


# 11. Berdasar plot sebelumnya, fakultas manakah yang jumlah mahasiswanya terus berkurang?

# Fakultas yang jumlah mahasiswany terus berkurang adalah STEI

