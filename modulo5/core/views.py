from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Tarefa
from .serializers import TarefaSerializer
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)

class ListaTarefasAPIView(APIView):
    def get(self, request, format=None):
        user_id = request.query_params.get('user_id')
        if user_id:
            tarefas = Tarefa.objects.filter(user_id=user_id)
        else:
            tarefas = Tarefa.objects.all()
            
        serializer = TarefaSerializer(tarefas, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        try:
            serializer = TarefaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Tarefa criada: {serializer.data['id']}")
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            logger.warning(f"Validação falhou: {serializer.errors}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        except IntegrityError as e:
            # Erro de constraint no banco (ex: UNIQUE)
            return Response(
                {'error': 'Violação de integridade no banco de dados.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            # Erro inesperado
            logger.error(f"Erro ao criar tarefa: {str(e)}")
            return Response(
                {'error': 'Erro interno do servidor.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
class ContagemTarefasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = total - concluidas
        return Response({
        'total': total,
        'concluidas': concluidas,
        'pendentes': pendentes
})

class EstatisticasTarefasAPIView(APIView):
    def get(self, request):
        total = Tarefa.objects.count()
        concluidas = Tarefa.objects.filter(concluida=True).count()
        pendentes = Tarefa.objects.filter(concluida=False).count()
        
        taxa_conclusao = concluidas / total if total > 0 else 0
        
        return Response({
        'total': total,
        'concluidas': concluidas,
        'pendentes': pendentes,
        'taxa_conclusao': round(taxa_conclusao, 2)
        })