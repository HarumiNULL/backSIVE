from django.utils import timezone
from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO
from permissions import IsAdminUser
from api.models import Optical, User  # Asegúrate de importar tu modelo Optical
from rest_framework import status, generics

class createReport(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request, *args, **kwargs):
        opticals = Optical.objects.all().select_related('city')
        
        total_opticals = opticals.count()
        
        print(f"DEBUG: Total de ópticas encontradas: {len(opticals)}") 
        print(f"DEBUG: Primera óptica (si existe): {opticals.first()}")
        
        name_admin = request.user.get_full_name()
        context = {
            'titulo': "Reporte Consolidado de Ópticas Registradas",
            'nombre_admin': name_admin,
            'opticas': opticals,
            'total_opticas': total_opticals,
            'fecha_generacion': timezone.now(),
        }
        
        html_string = render_to_string('reportOptical.html', context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte_opticas_consolidado.pdf"'
        response['Content-Disposition'] = 'attachment; filename="reporte_opticas_consolidado.pdf"'
        buffer = BytesIO()
     # pisa.pisaDocument toma el HTML y lo convierte, escribiendo el resultado en el buffer
        pisa_status = pisa.pisaDocument(
            BytesIO(html_string.encode("UTF-8")), # El HTML a convertir
            buffer, # El archivo de salida (en memoria)
            link_callback=lambda uri, rel: request.build_absolute_uri(uri) # Función para resolver rutas estáticas
        )
        # Si no hubo errores, escribir el contenido del buffer en la respuesta
        if not pisa_status.err:
            response.write(buffer.getvalue())
            return response
        
        # Si hubo un error en la conversión
        return HttpResponse('Tuvimos algunos errores al generar el PDF: %s' % pisa_status.err, status=status.HTTP_500_INTERNAL_SERVER_ERROR)