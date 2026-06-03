from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def operacion(request):
    contenido={}
    if request.method=='POST':
        texto=request.POST["numeros"]
        listatexto=texto.split(",")
        numeros=list(map(lambda x: int(x), listatexto))
        totalsuma=sum(numeros)
        promedio=totalsuma/len(numeros)
        mayor=max(numeros)
        menor=min(numeros)
        pares=list(filter(lambda x: x%2==0, numeros))
        impares=list(filter(lambda x: x%2!=0, numeros))
        cuadrados=list(map(lambda x: x**2, numeros))
        multiplosDe3=list(filter(lambda x: x%3==0, numeros))
        contenido = {
    "numeros": numeros,
    "suma": totalsuma,
    "promedio": promedio,
    "mayor": mayor,
    "menor": menor,
    "pares": pares,
    "impares": impares,
    "cuadrados": cuadrados,
    "multiplosDe3": multiplosDe3
}
    return render(request, "base.html", contenido )