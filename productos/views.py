from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import productoSerializers
from . models import Producto

@api_view(['POST'])
def crear_producto(request):
    serializer=productoSerializers(data=request.data)
   
    if serializer.is_valid():
        serializer.save()
        return Response("producto creado")
    return Response({'mensaje':'error'}, status=400)

@api_view(['GET'])
def ver_producto(request):
    producto=Producto.objects.all()
    serializer=productoSerializers(producto, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def ver_producto_id(request, id):
    producto=Producto.objects.get(id=id)
    serializer=productoSerializers(producto)
    return Response(serializer.data, status=200)

@api_view(['PUT'])
def actualizar_producto(request, id):
    producto=Producto.objects.get(id=id)
    if producto is None:
        return Response({'mensaje':'producto no encontrado'}, status=404)
    serializer=productoSerializers(producto, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("producto actualizado")
    return Response({'error'}, status=500)

@api_view(['DELETE'])
def eliminar_producto( request, id):
    producto= Producto.objects.get(id=id)
    producto.delete()
    return Response({'mensaje':'producto eliminado'}, status=200)