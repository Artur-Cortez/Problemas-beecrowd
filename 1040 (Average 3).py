n1,n2,n3,n4 = map(float,input().split())
media = (n1*2+n2*3+n3*4+n4*1)/10
print(f'Media: {media:.1f}')
if media>=7.0:
    print("Aluno aprovado.")
elif media<5.0:
    print("Aluno reprovado.")
elif media>=5.0 and media<7.0:
    print("Aluno em exame.")
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    exame = (media + exame)/2
    if exame>=5.0:
        print("Aluno aprovado.")
        print(f'Media final: {exame:.1f}')
    else:
        print("Aluno reprovado.")
        print(f'Media final: {exame:.1f}')