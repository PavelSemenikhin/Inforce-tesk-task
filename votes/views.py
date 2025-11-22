from django.http import HttpRequest
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from votes import services
from votes.models import Vote
from votes.serializers import VoteCreateSerializer, VoteReadSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()

    def get_permissions(self):
        if self.action in ["create"]:
            return [permissions.IsAuthenticated()]
        return [permissions.IsAdminUser()]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VoteReadSerializer
        return VoteCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        menu = serializer.validated_data["menu"]
        vote = services.create_vote_for_user(user, menu)
        serializer.instance = vote


class VoteResultApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request: HttpRequest) -> Response:
        results = services.get_vote_result()
        return Response(results)


class WinnerApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: HttpRequest) -> Response:
        winner = services.get_today_winner()

        if winner is None:
            return Response({"detail": "No votes today"}, status=200)
        return Response(winner)
