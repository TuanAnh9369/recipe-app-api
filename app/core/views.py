"""
Core views for app.
"""
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(['GET'])
# def health_check(request):
#     """Health check view."""
#     return Response({'healthy': True})

from rest_framework import generics, status
from rest_framework.response import Response


class HealthCheckView(generics.GenericAPIView):
    """Health check view."""
    def get(self, request):
        """Return 200 OK."""
        return Response({'healthy': 'ok'}, status=status.HTTP_200_OK)
