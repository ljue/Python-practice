import re
import os
import random

# Задание-1:
# Вывести символы в нижнем регистре, которые окружают 1 или более символа в верхнем регистре.
# Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
r1 = []
r2 = []

p1 = re.compile('[a-z][A-Z]+[a-z]')
p2 = re.compile('([a-z])[A-Z]+([a-z])')
p3 = re.compile('([a-z])[A-Z]+[a-z]')
p4 = re.compile('[A-Z]')
dline = line

while p1.search(dline):
       tmp = p1.search(dline)
       r1.append(tmp.group())
       dline = dline[tmp.end()-1:]
       if p4.match(dline[1:]):
              r2.append(p3.findall(r1[-1]))
       else:
              r2.append(p2.findall(r1[-1]))

print(r1)
print(r2)
print()


r3 = []
for i, x in enumerate(line):
       if line[i].islower():
              if i!=len(line)-1 and line[i+1].isupper() or i!=0 and line[i-1].isupper():
                     r3.append(line[i])


print(r3)
print()

# Задание-2:
# Вывести символы в верхнем регистре, которые окружают ровно два символа в нижнем регистре слева
# и два символа в верхнем регистре справа. Решить задачу двумя способами: с помощью re и без.
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalp' \
       'PLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzKTUfSYtBydXaVIpxWjNKgXANv' \
       'IoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkp' \
       'YOlqXEFIxPqqqgAWdJsOvqppOfyIVjXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSA' \
       'fJMchgBWAsGnBnWetekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAb' \
       'fCvzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXbJrwTRNyA' \
       'xDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCCEUZShGofaFpuespaZWLFN' \
       'IsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUf' \
       'lwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZC' \
       'nZjLeMiFlxnPkqfJFbCfKCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxy' \
       'GPvbnhWHuXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXi' \
       'UWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

r1 = []
r2 = []
# p1 = re.compile('[A-Z]+[a-z]{2}([A-z])[A-Z]{2}[a-z]+')
# r1 = p1.findall(line_2)
#
# print(r1)
# print()

p1 = re.compile('[A-Z]+[a-z]{2}([A-Z])[A-Z]{2}[a-z]+')
dline = line_2

while p1.search(dline):
       tmp = p1.search(dline)
       r1.append(tmp.group())
       dline = dline[tmp.end()-4:]
       r2.append(p1.findall(r1[-1]))

print(r2)
print()





r3 = []

for i, x in enumerate(line_2):
       if len(line_2) > 5 and line_2[i].isupper():
              if i == 2 and line_2[0].islower() and line_2[1].islower() and line_2[3].isupper() and \
                      line_2[4].isupper() and line_2[5].islower() or \
                     i == len(line_2)-3 and line_2[i-2].islower() and line_2[i-1].islower() and line_2[i+1].isupper() \
                                      and line_2[i+2].isupper() and line_2[i-3].isupper() or \
                            i > 2 and i < len(line_2) - 3 and line_2[i-3].isupper() and line_2[i - 2].islower() and \
                                              line_2[i - 1].islower() and line_2[i + 1].isupper() and \
                                      line_2[i + 2].isupper() and line_2[i+3].islower():
                     r3.append(line_2[i])
       if len(line_2) == 5 and line_2[i].isupper():
              if line_2[0].islower() and line_2[1].islower() and line_2[3].isupper() and line_2[4].isupper():
                     r3.append(line_2[2])

print(r3)
print()

# Задача-3:
# Напишите скрипт заполняющий указанный файл (самомстоятельно задайте имя файла) произвольными целыми
# цифрами, в результате в файле должно быть 2500-значное произвольное число
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле

path = os.path.join('digits.txt')
f = open(path, 'w', encoding='UTF-8')
for i in range(2500):
       f.write(str(random.randint(0,9)))
f.close()

k=0
kstr=''
sumk=0
sumkstr=''
f = open(path, 'r', encoding='UTF-8')
for line in f:
       for i,x in enumerate(line):
              if i < len(line)-1 and line[i+1] == line[i]:
                     k += 1
                     if k == 1:
                            k+=1
                            kstr += line[i]+line[i+1]
                     else:
                            kstr += line[i + 1]
                     if k>sumk:
                            sumk = k
                            sumkstr = kstr
              else:
                     k=0
                     kstr=''
print(sumk,sumkstr)

f.close()