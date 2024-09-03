from django.shortcuts import get_object_or_404
from .models import Question
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializer import QuestionSerializer

class QuestionView(generics.GenericAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, pk, partial):
        question = get_object_or_404(Question, pk=pk, user=request.user)
        serializer = self.serializer_class(question, request.data, partial=partial)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors})
        
        serializer.save(user=request.user)
        return Response({"data": request.data}, status=status.HTTP_200_OK)
    
    def detail(self, request, pk):
        question = get_object_or_404(Question, pk=pk, user=request.user)
        serializer = self.serializer_class(question)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request):
        questions = Question.objects.all()
        serializer = self.serializer_class(questions, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)
    
    def get(self, request, pk=None):
        if pk is None:
            return self.list(request)
        else:
            return self.detail(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk, partial=False)
    
    def patch(self, pk, request):
        return self.update(request, pk, partial=True)
    
    def delete(self, request, pk):
      get_object_or_404(Question, pk=pk, user=request.user).delete()
      return Response(status=status.HTTP_200_OK)
