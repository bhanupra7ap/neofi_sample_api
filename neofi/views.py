from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Note, SharedNote, NoteVersion
from .serializers import UserSerializer, NoteSerializer, SharedNoteSerializer, NoteVersionSerializer
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')

@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer])  
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
      
        return Response("GET method not allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer]) 
def login(request):
    if request.method == 'POST':
      
        pass
    elif request.method == 'GET':
      
        return Response("GET method not allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer]) 
def create_note(request):
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
     
        return Response("GET method not allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@renderer_classes([JSONRenderer]) 
def get_note(request, id):
    if request.method == 'GET':
        try:
            note = Note.objects.get(id=id)
            if request.user == note.owner:
                serializer = NoteSerializer(note)
                return Response(serializer.data)
            elif request.user.sharednote_set.filter(note=note).exists():
                serializer = NoteSerializer(note)
                return Response(serializer.data)
            else:
                return Response("You do not have permission to view this note.", status=status.HTTP_403_FORBIDDEN)
        except Note.DoesNotExist:
            return Response("Note does not exist.", status=status.HTTP_404_NOT_FOUND)

@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer])  
def share_note(request):
    if request.method == 'POST':
        serializer = SharedNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
     
        return Response("GET method not allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT', 'GET'])
@renderer_classes([JSONRenderer]) 
def update_note(request, id):
    if request.method == 'PUT':
        try:
            note = Note.objects.get(id=id)
            if request.user == note.owner:
                serializer = NoteSerializer(note, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("You do not have permission to update this note.", status=status.HTTP_403_FORBIDDEN)
        except Note.DoesNotExist:
            return Response("Note does not exist.", status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'GET':
        return Response("GET method not allowed.", status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
@renderer_classes([JSONRenderer]) 
def get_note_version_history(request, id):
    if request.method == 'GET':
        try:
            note = Note.objects.get(id=id)
            if request.user == note.owner:
                versions = NoteVersion.objects.filter(note=note)
                serializer = NoteVersionSerializer(versions, many=True)
                return Response(serializer.data)
            else:
                return Response("You do not have permission to view version history for this note.", status=status.HTTP_403_FORBIDDEN)
        except Note.DoesNotExist:
            return Response("Note does not exist.", status=status.HTTP_404_NOT_FOUND)

