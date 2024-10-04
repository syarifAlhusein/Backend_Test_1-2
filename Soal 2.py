def display_numbers(n, rules):
    output = []
    for i in range(1, n + 1):
        value = ""
        if i % 3 == 0:
            value += "cat"
        if i % 5 == 0:
            value += "kitty"
        if i in rules:
            value += rules[i]
        if not value:
            value = str(i)
        output.append(value)
    print(", ".join(output))

def add_rule(rules, angka, output):
    rules[angka] = output

# Menentukan jumlah angka hingga n
n = int(input("Masukkan angka n: "))

# Aturan awal
rules = {}

# Menambahkan aturan default
add_rule(rules, 13, "dog")

# Menambahkan aturan baru dari input pengguna hanya sekali
angka = int(input("Masukkan angka untuk aturan (atau tekan 0 untuk melewati): "))
if angka != 0:
    output = input("Masukkan output untuk aturan: ")
    add_rule(rules, angka, output)

# Menampilkan angka dengan aturan
display_numbers(n, rules)
