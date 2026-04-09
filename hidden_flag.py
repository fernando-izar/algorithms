import hashlib


final_text = ""
with open("server_logs.txt", "r") as file:
    for line in file:
        if line.startswith("SERVER") or line.startswith("-"):
            continue
        md5_hash = hashlib.md5(line.encode()).hexdigest()
        if "a" <= md5_hash[-1].lower() <= "f":
            continue
        letter = md5_hash[-1]
        if "0" <= md5_hash[-1] <= "9":
            final_text += line[4]

print(final_text)

# import hashlib

# result = []

# with open("server_logs.txt", "r") as f:
#     for line in f:
#         # ignorar linhas que começam com SERVER ou -
#         if line.startswith("SERVER") or line.startswith("-"):
#             continue

#         # calcular MD5 da linha inteira (incluindo \n)
#         md5 = hashlib.md5(line.encode()).hexdigest()

#         # pegar último caractere do hash
#         last = md5[-1]

#         # manter apenas se terminar em número
#         if last.isdigit():  # 0–9
#             result.append(line[4])  # índice 4 (5º caractere)

# # juntar caracteres
# flag = "".join(result)

# print(flag)
