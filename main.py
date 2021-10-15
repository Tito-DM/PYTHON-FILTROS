
a = [0]*10;
b = [1,2,6,2,8,9];
a.extend(b)
print(len(a));
a.extend([4,2,6,8,6]);
print(a);
print(a.index(2));
a.remove(6);
print(a);
#nº de * em que o 8 aparece
print(a.count(8));
#remover ultimo elemento
a.pop();
print(a);


