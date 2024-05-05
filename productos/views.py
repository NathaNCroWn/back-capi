from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import productoSerializers
from . models import Producto

@api_view(['POST'])
def crear_producto(request):
    serializer=productoSerializers(data=request.data)
   
    if serializer.is_valid():
        serializer.save()
        return Response({'mensaje':'producto creado'}, status=201)
    return Response({'mensaje':'error'}, status=400)

@api_view(['GET'])
def ver_producto(request):
    producto=Producto.objects.all()
    serializer=productoSerializers(producto, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def actualizar_producto(request, id):
    producto=Producto.objects.get(id=id)
    serializer=productoSerializers(producto, data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response({'mesaje':'producto actualizado'}, status=200)
    return Response({'mensaje':'prodcuto no encontrado'}, status=404)

@api_view(['DELETE'])
def eliminar_producto(id):
    producto= Producto.objects.get(id=id)
    producto.delete()
    return Response({'mensaje':'producto eliminado'}, status=200)