""" kanom calculator """
def snack():
    """ main """
    kanom = []
    cap = []
    rec = []
    n = int(input())
    for i in range(n):
        kanom.append(float(input()))
        cap.append(float(input()))
    for i in range(n):
        rec.append(cap[i]/kanom[i])
    print(f"{kanom[rec.index(max(rec))]:.2f} {cap[rec.index(max(rec))]:.2f}")
snack()
