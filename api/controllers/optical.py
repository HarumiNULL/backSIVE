from rest_framework import generics, status, permissions
from rest_framework.response import Response
from api.services import OpticalService
from api.models import Optical
from api.serializers import OpticalSerializers # asegúrate de tener este serializer

class OpticalController(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = OpticalSerializers
    queryset = Optical.objects.all()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = OpticalService() 

    # GET → listar todas o una por id
    def get(self, request, *args, **kwargs):
        id_optical = kwargs.get('pk', None)
        if id_optical:
            optical = self.service.repository.get_optical_by_id(id_optical)
            if not optical:
                return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
            serializer = self.serializer_class(optical)
            return Response(serializer.data)
        else:
            opticals = self.service.list_optical()
            serializer = self.serializer_class(opticals, many=True)
            return Response(serializer.data)

    # POST → crear nueva óptica
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                optical = self.service.create_optical(serializer.validated_data)
                return Response(self.serializer_class(optical).data, status=status.HTTP_201_CREATED)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT → actualizar óptica existente
    def put(self, request, pk, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, partial=True)
        if serializer.is_valid():
            try:
                optical = self.service.update_optical(pk, serializer.validated_data)
                if not optical:
                    return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
                return Response(self.serializer_class(optical).data)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE → eliminar óptica
    def delete(self, request, pk, *args, **kwargs):
        try:
            deleted = self.service.delete_optical(pk)
            if deleted:
                return Response(status=status.HTTP_204_NO_CONTENT)
            return Response({"error": "Óptica no encontrada"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
